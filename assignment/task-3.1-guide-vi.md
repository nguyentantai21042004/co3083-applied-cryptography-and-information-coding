# Task 3.1: Hướng dẫn Từ đầu đến cuối - Chặn bắt & Phân tích API sử dụng Burp Suite
## Phiên bản Mac M4 với Môi trường Android Containerized

## Tổng quan
Hướng dẫn này cung cấp hướng dẫn từng bước để hoàn thành Task 3.1 của bài tập SMC Exploitation trên Mac M4. Bạn sẽ thiết lập Burp Suite như một proxy man-in-the-middle để chặn bắt và ghi chép tất cả các cuộc gọi API giữa client Android và server sử dụng emulator của Android Studio.

**Điểm:** 0.5
**Mục tiêu:** Chặn bắt và ghi chép tất cả các cuộc gọi API từ giai đoạn Trao đổi Khóa đến giai đoạn Trao đổi Tin nhắn.
**Môi trường:** Mac M4, Android Studio IDE, Docker (tùy chọn cho các tình huống nâng cao)

---

## Điều kiện Tiên quyết

### Yêu cầu Hệ thống
- **Mac M4** (Apple Silicon)
- **macOS Sonoma** hoặc mới hơn
- **Homebrew** đã cài đặt
- Ít nhất **8GB RAM** và **20GB dung lượng đĩa trống**

### Phần mềm Cần thiết

1. **Burp Suite Community Edition cho macOS (ARM64)**
   - Tải xuống: https://portswigger.net/burp/releases/professional-community-2025-8-7?requestededition=community&requestedplatform=
   - Chọn: Phiên bản **macOS (ARM64)** cho chip M4

2. **Android Studio (Apple Silicon)**
   - Tải xuống: https://developer.android.com/studio
   - Chọn: Phiên bản **Mac (ARM64)**
   - Bao gồm Android SDK và emulator ARM64 được tối ưu cho M4

3. **Java Development Kit (JDK)**
   ```bash
   brew install openjdk@17
   ```

4. **Mã nguồn & APK Client SMC**
   - Repository: https://github.com/dangduongminhnhat/Client-Assignment-Advance-Cryptography-and-Coding-Theory
   - Clone vào workspace của bạn:
   ```bash
   cd ~/Workspaces/hcmut/co3083-applied-cryptography-and-information-coding
   git clone https://github.com/dangduongminhnhat/Client-Assignment-Advance-Cryptography-and-Coding-Theory.git smc-client
   ```

### Công cụ Tùy chọn
- **Docker Desktop cho Mac (Apple Silicon)** - cho các tình huống kiểm thử containerized
- **Visual Studio Code** - để phân tích code
- **apktool** - để phân tích và sửa đổi APK
  ```bash
  brew install apktool
  ```

---

## Bước 1: Cài đặt và Cấu hình Burp Suite trên Mac M4

### 1.1 Cài đặt Burp Suite
```bash
# Tải xuống file DMG macOS ARM64
# Mở DMG đã tải xuống và kéo Burp Suite vào Applications

# Khởi chạy từ Applications hoặc qua terminal
open -a "Burp Suite Community Edition"
```

### 1.2 Cấu hình Burp Ban đầu
1. Khởi chạy Burp Suite
2. Chọn **Temporary project** (để bắt đầu nhanh)
3. Sử dụng **Burp defaults** cho cấu hình
4. Click **Start Burp**

### 1.3 Cấu hình Burp Proxy cho localhost
1. Đi đến **Proxy** → **Settings** → **Proxy Listeners**
2. Bạn sẽ thấy một listener trên `127.0.0.1:8080`
3. Vì Android Emulator chạy trên cùng máy, chúng ta sẽ sử dụng địa chỉ đặc biệt:
   - Đối với Android Emulator, `10.0.2.2` trỏ đến `127.0.0.1` của host
   - Giữ listener mặc định `127.0.0.1:8080`

### 1.4 Xuất Chứng chỉ CA của Burp
```bash
# Tạo thư mục cho chứng chỉ
mkdir -p ~/Desktop/burp-setup

# Trong Burp Suite:
# 1. Đi đến Proxy → Settings → Proxy Listeners
# 2. Click "Import / export CA certificate"
# 3. Chọn "Certificate in DER format"
# 4. Lưu vào ~/Desktop/burp-setup/burp-cert.der

# Chuyển đổi DER sang định dạng PEM (cần cho Android system certs)
openssl x509 -inform DER -in ~/Desktop/burp-setup/burp-cert.der \
  -out ~/Desktop/burp-setup/burp-cert.pem

# Lấy hash của chứng chỉ (cần cho cài đặt system cert)
openssl x509 -inform PEM -subject_hash_old -in ~/Desktop/burp-setup/burp-cert.pem | head -1
# Sẽ xuất ra hash như: 9a5ba575

# Đổi tên cert với hash
HASH=$(openssl x509 -inform PEM -subject_hash_old -in ~/Desktop/burp-setup/burp-cert.pem | head -1)
cp ~/Desktop/burp-setup/burp-cert.pem ~/Desktop/burp-setup/${HASH}.0
```

---

## Bước 2: Thiết lập Android Studio và Emulator

### 2.1 Cài đặt Android Studio
```bash
# Tải xuống từ https://developer.android.com/studio
# Cài đặt Android Studio (phiên bản ARM64 cho M4)

# Hoặc qua Homebrew:
brew install --cask android-studio
```

### 2.2 Cấu hình Android Studio
1. Khởi chạy Android Studio
2. Hoàn thành setup wizard:
   - Cài đặt Android SDK
   - Cài đặt Android SDK Platform
   - Cài đặt Android Virtual Device (AVD)

3. Cài đặt các thành phần SDK cần thiết:
   - Mở **Settings/Preferences** → **Appearance & Behavior** → **System Settings** → **Android SDK**
   - Kiểm tra và cài đặt:
     - Android 13.0 (API 33) hoặc cao hơn
     - Android SDK Build-Tools
     - Android SDK Platform-Tools
     - Android SDK Command-line Tools

### 2.3 Tạo Android Emulator ARM64

1. Mở **Device Manager** (trong thanh công cụ Android Studio)
2. Click **Create Device**
3. Chọn một định nghĩa thiết bị (ví dụ: **Pixel 7**)
4. Chọn system image:
   - Chọn kiến trúc **arm64-v8a** (được tối ưu cho M4)
   - Khuyến nghị: **Android 13.0 (API 33)** hoặc **Android 12.0 (API 31)**
   - Tải xuống nếu chưa cài đặt
5. Đặt tên AVD của bạn: `SMC_Test_Device`
6. Hiển thị **Advanced Settings**:
   - Đặt **RAM:** 4096 MB (hoặc cao hơn)
   - Bật **Cold boot**
   - Ghi chú đường dẫn emulator để sử dụng sau

### 2.4 Cấu hình Cài đặt Mạng Emulator

**Phương pháp 1: Khởi chạy với Proxy (Khuyến nghị)**
```bash
# Thiết lập biến môi trường
export ANDROID_HOME=~/Library/Android/sdk
export PATH=$PATH:$ANDROID_HOME/emulator:$ANDROID_HOME/platform-tools

# Khởi chạy emulator với HTTP proxy
emulator -avd SMC_Test_Device \
  -http-proxy 127.0.0.1:8080 \
  -writable-system
```

**Phương pháp 2: Đặt Proxy qua Cài đặt Android**
1. Khởi chạy emulator bình thường từ Android Studio
2. Trong emulator, đi đến **Settings** → **Network & Internet** → **Internet**
3. Nhấn giữ **AndroidWifi**
4. Chọn **Modify network**
5. Mở rộng **Advanced options**
6. Đặt **Proxy** thành **Manual**:
   - **Proxy hostname:** `10.0.2.2` (địa chỉ đặc biệt cho host)
   - **Proxy port:** `8080`
7. Lưu

### 2.5 Cài đặt Chứng chỉ Burp như System Certificate

Từ Android 7.0+, chứng chỉ do người dùng cài đặt không được tin tưởng bởi apps. Chúng ta cần cài đặt chứng chỉ của Burp như một system certificate.

```bash
# Khởi động emulator với phân vùng hệ thống có thể ghi
emulator -avd SMC_Test_Device -writable-system &

# Đợi emulator khởi động hoàn toàn
adb wait-for-device

# Remount phân vùng hệ thống như có thể ghi
adb root
adb remount

# Đẩy chứng chỉ đến thư mục system certificates
# Sử dụng file có tên hash đã tạo trước đó
adb push ~/Desktop/burp-setup/${HASH}.0 /system/etc/security/cacerts/

# Đặt quyền đúng
adb shell chmod 644 /system/etc/security/cacerts/${HASH}.0

# Khởi động lại emulator
adb reboot

# Xác minh cài đặt chứng chỉ sau khi khởi động lại
adb shell ls -la /system/etc/security/cacerts/ | grep ${HASH}
```

### 2.6 Xác minh Kết nối Proxy
```bash
# Trong emulator, mở trình duyệt Chrome
# Điều hướng đến: http://burp

# Bạn sẽ thấy trang chào mừng Burp Suite
# Kiểm tra Burp Suite → Proxy → HTTP history cho request
```

---

## Bước 3: Mở Dự án Client SMC trong Android Studio

### 3.1 Import Dự án
1. Trong Android Studio, chọn **File** → **Open**
2. Điều hướng đến repository đã clone:
   ```
   ~/Workspaces/hcmut/co3083-applied-cryptography-and-information-coding/smc-client
   ```
3. Click **Open**
4. Đợi Gradle sync hoàn tất

### 3.2 Build Dự án
```bash
# Qua Android Studio: Build → Make Project
# Hoặc qua terminal:
cd ~/Workspaces/hcmut/co3083-applied-cryptography-and-information-coding/smc-client
./gradlew assembleDebug
```

### 3.3 Cài đặt APK trên Emulator

**Phương pháp 1: Cài đặt Trực tiếp từ Android Studio**
1. Chọn emulator của bạn từ dropdown thiết bị
2. Click nút **Run** (biểu tượng play màu xanh)
3. App sẽ được build và cài đặt tự động

**Phương pháp 2: Cài đặt Thủ công qua ADB**
```bash
# Tìm APK đã tạo
find . -name "*.apk" -type f

# Cài đặt trên emulator
adb install -r app/build/outputs/apk/debug/app-debug.apk

# Xác minh cài đặt
adb shell pm list packages | grep smc
```

### 3.4 Vô hiệu hóa Certificate Pinning (nếu cần)

Nếu app sử dụng certificate pinning, bạn sẽ cần bypass nó:

**Tùy chọn 1: Sửa đổi network_security_config.xml**
1. Mở dự án trong Android Studio
2. Điều hướng đến `app/src/main/res/xml/network_security_config.xml`
3. Sửa đổi để tin tưởng chứng chỉ người dùng:
```xml
<?xml version="1.0" encoding="utf-8"?>
<network-security-config>
    <base-config>
        <trust-anchors>
            <certificates src="system" />
            <certificates src="user" />
        </trust-anchors>
    </base-config>
</network-security-config>
```
4. Rebuild và cài đặt lại

**Tùy chọn 2: Sử dụng Frida để Bypass Runtime**
```bash
# Cài đặt Frida tools
pip3 install frida-tools

# Tải xuống frida-server cho Android ARM64
# https://github.com/frida/frida/releases

# Đẩy lên emulator
adb push frida-server-*-android-arm64 /data/local/tmp/frida-server
adb shell chmod 755 /data/local/tmp/frida-server
adb shell /data/local/tmp/frida-server &

# Sử dụng script Frida để bypass SSL pinning
frida -U -f com.example.smc -l ssl-pinning-bypass.js
```

### 3.5 Chuẩn bị cho Kiểm thử
1. Ghi chú User ID được phân bổ của bạn từ Google Sheet
2. Cấu hình server endpoint trong cài đặt app
3. Chuẩn bị công cụ phân tích của bạn (text editor, công cụ chụp màn hình)

---

## Bước 4: Chặn bắt Lưu lượng API

### 4.1 Bắt đầu Chặn bắt Burp
1. Trong Burp Suite, đi đến **Proxy** → **Intercept**
2. Đảm bảo **Intercept is on** (nút sẽ hiển thị điều này)
3. Xóa lịch sử trước đó: **Proxy** → **HTTP history** → Right-click → **Clear history**

### 4.2 Khởi chạy Client SMC
1. Mở app SMC trên Android
2. Bắt đầu với quá trình setup/login ban đầu

### 4.3 Chặn bắt Giai đoạn 1: Trao đổi/Bắt tay Khóa Ban đầu
1. Bắt đầu quá trình trao đổi khóa trong app
2. Đối với mỗi request xuất hiện trong Burp:
   - **Chụp màn hình** hiển thị:
     - Tab Request (URL, headers, body)
     - Tab Response (status, headers, body)
   - **Ghi chép những điều sau:**
     - API endpoint URL
     - HTTP method (GET, POST, v.v.)
     - Request headers
     - Request body (nếu có)
     - Response status code
     - Response headers
     - Response body
   - Click **Forward** để gửi request
3. Lưu mỗi request/response đã chặn bắt vào lịch sử Burp

### 4.4 Chặn bắt Giai đoạn 2: Thiết lập Phiên
1. Tiếp tục qua giai đoạn thiết lập phiên
2. Lặp lại quá trình ghi chép cho mỗi cuộc gọi API
3. Chụp màn hình và ghi chú

### 4.5 Chặn bắt Giai đoạn 3: Nhắn tin Được mã hóa
1. Gửi ít nhất 2-3 tin nhắn kiểm thử qua app
2. Chặn bắt và ghi chép mỗi trao đổi tin nhắn
3. Ghi chú bất kỳ khác biệt nào trong các mẫu được mã hóa vs. plaintext

### 4.6 Lưu Phiên Burp
1. **Proxy** → **HTTP history**
2. Chọn tất cả requests liên quan
3. Right-click → **Save items**
4. Lưu như một file để tham khảo

---

## Bước 5: Phân tích và Ghi chép Mỗi Cuộc gọi API

Đối với mỗi cuộc gọi API đã chặn bắt, tạo một mục chi tiết với:

### 5.1 Thông tin Cuộc gọi API
Tạo bảng với các cột sau:

| # | Endpoint | Method | Phase | Purpose |
|---|----------|--------|-------|---------|
| 1 | /api/auth/login | POST | Authentication | User login |
| 2 | /api/keyexchange/init | POST | Key Exchange | Initialize key exchange |
| ... | ... | ... | ... | ... |

### 5.2 Ghi chép Trường Request/Response

Đối với mỗi cuộc gọi API, ghi chép:

**Trường Request:**
```
Endpoint: /api/keyexchange/init
Method: POST
Headers:
  - Content-Type: application/json
  - Authorization: Bearer <token>

Body Parameters:
  - userId: string - Định danh người dùng
  - publicKey: string - Khóa công khai client được mã hóa Base64
  - timestamp: long - Unix timestamp của request
  - nonce: string - Nonce ngẫu nhiên để bảo vệ replay
```

**Trường Response:**
```
Status: 200 OK
Headers:
  - Content-Type: application/json

Body:
  - serverPublicKey: string - Khóa công khai server được mã hóa Base64
  - sessionId: string - Định danh phiên duy nhất
  - signature: string - Chữ ký server trên response
  - timestamp: long - Timestamp server
```

### 5.3 Ánh xạ đến Mã nguồn

Đối với mỗi cuộc gọi API, tìm code tương ứng:

**Ví dụ:**
```
API: POST /api/keyexchange/init

Client Code:
  - File: app/src/main/java/com/example/smc/network/KeyExchangeService.java
  - Method: initiateKeyExchange()
  - Lines: 45-67

Server Code (nếu có sẵn):
  - File: server/src/handlers/keyexchange.js
  - Function: handleKeyExchangeInit()
  - Lines: 23-45
```

---

## Bước 6: Tạo Sản phẩm

### 6.1 Tổ chức Screenshot
Tổ chức screenshots theo giai đoạn:
```
screenshots/
  ├── 01-authentication/
  │   ├── 01-login-request.png
  │   └── 02-login-response.png
  ├── 02-key-exchange/
  │   ├── 01-init-request.png
  │   ├── 02-init-response.png
  │   └── ...
  └── 03-messaging/
      ├── 01-send-message-request.png
      └── 02-send-message-response.png
```

### 6.2 Tạo Báo cáo Ghi chép

Tạo một tài liệu với cấu trúc sau:

```markdown
# Task 3.1: Báo cáo Chặn bắt & Phân tích API

## 1. Tóm tắt Thiết lập
- Phiên bản Burp Suite: ...
- Thiết bị/emulator Android: ...
- Ngày kiểm thử: ...
- User ID đã sử dụng: ...

## 2. Tóm tắt Cuộc gọi API đã Chặn bắt

### 2.1 Giai đoạn Xác thực
#### API 1: Đăng nhập Người dùng
- **Screenshot:** [screenshots/01-authentication/01-login-request.png]
- **Endpoint:** POST /api/auth/login
- **Trường Request:**
  - username: string - Định danh người dùng
  - password: string - Mật khẩu người dùng (đã hash)
  - deviceId: string - Định danh thiết bị
- **Trường Response:**
  - token: string - JWT authentication token
  - userId: string - User ID
  - expiresIn: number - Thời gian hết hạn token
- **Vị trí Code:**
  - Client: AuthService.java:23-45
  - Server: auth.controller.js:67-89

### 2.2 Giai đoạn Trao đổi Khóa
#### API 2: Khởi tạo Trao đổi Khóa
[Ghi chép chi tiết tương tự]

### 2.3 Giai đoạn Nhắn tin
#### API 3: Gửi Tin nhắn Được mã hóa
[Ghi chép chi tiết tương tự]

## 3. Bảng Ánh xạ Cuộc gọi API

| # | Endpoint | Method | Request Fields | Response Fields | Code Location |
|---|----------|--------|----------------|-----------------|---------------|
| 1 | /api/auth/login | POST | username, password | token, userId | AuthService.java:23 |
| 2 | /api/keyexchange/init | POST | userId, publicKey | serverPublicKey, sessionId | KeyExchangeService.java:45 |
| ... | ... | ... | ... | ... | ... |

## 4. Giải thích Trường

### 4.1 Trường Xác thực
- **username:** ...
- **token:** ...

### 4.2 Trường Trao đổi Khóa
- **publicKey:** ...
- **serverPublicKey:** ...

### 4.3 Trường Nhắn tin
- **encryptedMessage:** ...
- **signature:** ...

## 5. Ánh xạ Mã nguồn

[Ánh xạ chi tiết của mỗi API đến các file và số dòng cụ thể]
```

---

## Bước 7: Danh sách Kiểm tra Xác minh

Trước khi nộp, xác minh bạn có:

- [ ] Screenshots Burp Suite cho TẤT CẢ cuộc gọi API
- [ ] Screenshots rõ ràng, dễ đọc hiển thị cả request và response
- [ ] Đã ghi chép mọi trường trong requests và responses
- [ ] Đã giải thích mục đích của mỗi trường
- [ ] Đã ánh xạ mỗi cuộc gọi API đến vị trí mã nguồn
- [ ] Đã tổ chức screenshots trong cấu trúc thư mục rõ ràng
- [ ] Đã tạo bảng tóm tắt toàn diện
- [ ] Đã bao gồm cả giai đoạn xác thực và nhắn tin
- [ ] Đã xác minh tất cả tham chiếu code trỏ đến file/dòng đúng
- [ ] Đã đọc lại ghi chép để rõ ràng và chính xác

---

## Vấn đề Thường gặp và Giải pháp (Dành riêng cho Mac M4)

### Vấn đề 1: Emulator không khởi động hoặc crash
**Giải pháp:**
```bash
# Kiểm tra nếu virtualization được bật
sysctl kern.hv_support
# Nên trả về: kern.hv_support: 1

# Xóa cache emulator
rm -rf ~/.android/avd/SMC_Test_Device.avd/cache/*

# Khởi chạy với logging chi tiết hơn
emulator -avd SMC_Test_Device -verbose -show-kernel

# Nếu vẫn thất bại, thử tạo AVD mới với API level khác
```

### Vấn đề 2: ADB không nhận diện emulator
**Giải pháp:**
```bash
# Kill và khởi động lại ADB server
adb kill-server
adb start-server

# Liệt kê thiết bị đã kết nối
adb devices

# Nếu emulator hiển thị là offline
adb reconnect

# Kiểm tra PATH bao gồm Android SDK
echo $ANDROID_HOME
export ANDROID_HOME=~/Library/Android/sdk
export PATH=$PATH:$ANDROID_HOME/platform-tools
```

### Vấn đề 3: Cài đặt chứng chỉ thất bại trên emulator
**Giải pháp:**
```bash
# Đảm bảo emulator được khởi chạy với -writable-system
emulator -list-avds
emulator -avd SMC_Test_Device -writable-system -no-snapshot-load &

# Thử chế độ SELinux permissive thủ công
adb root
adb shell setenforce 0
adb remount

# Đẩy lại chứng chỉ
HASH=$(openssl x509 -inform PEM -subject_hash_old -in ~/Desktop/burp-setup/burp-cert.pem | head -1)
adb push ~/Desktop/burp-setup/${HASH}.0 /system/etc/security/cacerts/
adb shell chmod 644 /system/etc/security/cacerts/${HASH}.0
adb reboot
```

### Vấn đề 4: Burp không chặn bắt lưu lượng
**Giải pháp:**
```bash
# Kiểm tra cài đặt proxy trong emulator
adb shell settings get global http_proxy

# Đặt proxy thủ công
adb shell settings put global http_proxy 10.0.2.2:8080

# Xác minh Burp đang lắng nghe
lsof -i :8080

# Kiểm tra firewall macOS không chặn
# System Settings → Network → Firewall → Allow Burp Suite

# Kiểm thử kết nối
adb shell curl -x 10.0.2.2:8080 http://example.com
```

### Vấn đề 5: Build Gradle thất bại trong Android Studio
**Giải pháp:**
```bash
# Clean và rebuild
./gradlew clean
./gradlew assembleDebug --stacktrace

# Kiểm tra phiên bản Java
java -version
# Nên là Java 17

# Nếu có vấn đề JDK:
export JAVA_HOME=$(/usr/libexec/java_home -v 17)

# Xóa cache Gradle
rm -rf ~/.gradle/caches/
```

### Vấn đề 6: SSL pinning vẫn chặn lưu lượng
**Giải pháp:**
```bash
# Sử dụng objection để bypass tự động
pip3 install objection

# Khởi động objection
objection -g com.example.smc explore

# Trong console objection:
android sslpinning disable

# Hoặc sử dụng script Frida
frida -U -f com.example.smc --no-pause -l universal-ssl-pinning-bypass.js
```

### Vấn đề 7: Không tìm thấy vị trí code
**Giải pháp:**
```bash
# Sử dụng ripgrep để tìm kiếm nhanh
brew install ripgrep

# Tìm kiếm API endpoints
cd ~/Workspaces/hcmut/co3083-applied-cryptography-and-information-coding/smc-client
rg "api/keyexchange" -A 5 -B 5

# Tìm kiếm các lớp mạng
rg "OkHttp|Retrofit|HttpClient" --type java

# Tìm kiếm tên trường JSON
rg "publicKey|serverPublicKey" --type java

# Sử dụng Find in Path của Android Studio (Cmd+Shift+F)
```

---

## Mẹo Dành riêng cho Mac M4

### Tối ưu Hiệu suất
```bash
# Cấp nhiều tài nguyên hơn cho emulator
emulator -avd SMC_Test_Device \
  -memory 4096 \
  -cores 4 \
  -gpu auto \
  -writable-system \
  -http-proxy 127.0.0.1:8080
```

### Công cụ Screenshot cho Mac
```bash
# Screenshot tích hợp
# Cmd+Shift+4 để chọn vùng
# Cmd+Shift+5 cho tùy chọn nâng cao

# Hoặc sử dụng lệnh screencapture
screencapture -i ~/Desktop/burp-screenshots/screenshot-$(date +%Y%m%d-%H%M%S).png
```

### Script Tự động hóa Quy trình
```bash
# Tạo script khởi động: ~/Desktop/burp-setup/start-testing.sh
#!/bin/bash

# Khởi động Burp Suite
open -a "Burp Suite Community Edition"
sleep 5

# Thiết lập môi trường
export ANDROID_HOME=~/Library/Android/sdk
export PATH=$PATH:$ANDROID_HOME/emulator:$ANDROID_HOME/platform-tools

# Khởi động emulator
emulator -avd SMC_Test_Device \
  -writable-system \
  -http-proxy 127.0.0.1:8080 \
  -memory 4096 &

# Đợi boot
adb wait-for-device
echo "Emulator ready!"

# Đặt proxy (dự phòng)
adb shell settings put global http_proxy 10.0.2.2:8080

echo "Setup complete. Ready for testing."
```

Làm cho nó có thể thực thi:
```bash
chmod +x ~/Desktop/burp-setup/start-testing.sh
```

---

## Docker Alternative (Nâng cao)

Để tiếp cận hoàn toàn containerized:

### Sử dụng Docker với Android Emulator

```bash
# Pull Docker image Android emulator
docker pull budtmo/docker-android:emulator_12.0

# Chạy container với Burp proxy
docker run -d \
  --name android-emulator \
  -p 5555:5555 \
  -p 5554:5554 \
  -e EMULATOR_DEVICE="Samsung Galaxy S10" \
  -e WEB_VNC=true \
  -e PROXY_HOST=host.docker.internal \
  -e PROXY_PORT=8080 \
  budtmo/docker-android:emulator_12.0

# Kết nối đến emulator
adb connect localhost:5555

# Truy cập qua VNC tại http://localhost:6080
```

**Lưu ý:** Docker emulator trên M4 có thể có giới hạn hiệu suất. Emulator ARM64 native của Android Studio được khuyến nghị.

---

## Định dạng Sản phẩm Mong đợi

Nộp một tài liệu chứa:

1. **Trang Bìa:**
   - Tên task: Task 3.1 - Chặn bắt & Phân tích API
   - Tên/nhóm của bạn
   - Ngày
   - Môi trường: Mac M4, Android Studio, Burp Suite

2. **Mục lục**

3. **Giới thiệu:**
   - Môi trường kiểm thử: Mac M4, emulator ARM64
   - Công cụ đã sử dụng: Phiên bản Burp Suite, phiên bản Android Studio
   - Tóm tắt thiết lập: cấu hình emulator, thiết lập proxy

4. **Ghi chép API:**
   - Đối với mỗi cuộc gọi API (được tổ chức theo giai đoạn):
     - Screenshots (Burp request + response)
     - Giải thích từng trường
     - Ánh xạ vị trí code

5. **Bảng Tóm tắt:**
   - Danh sách hoàn chỉnh tất cả APIs đã chặn bắt

6. **Phân tích Mã nguồn:**
   - Cách requests được xây dựng trong code
   - Cách responses được xử lý
   - Trao đổi khóa và các thao tác crypto

7. **Phụ lục:**
   - Chi tiết cấu hình Burp
   - Thông số kỹ thuật emulator
   - Các lệnh đã sử dụng
   - Thách thức gặp phải và giải pháp

---

## Ước tính Thời gian (Mac M4)

- Cài đặt Android Studio và thiết lập: 1 giờ
- Cài đặt Burp Suite: 15 phút
- Tạo và cấu hình emulator: 30 phút
- Cài đặt chứng chỉ và kiểm thử proxy: 45 phút
- Clone và build client SMC: 30 phút
- Chặn bắt và ghi chép APIs: 2-3 giờ
- Ánh xạ đến mã nguồn: 2-3 giờ
- Tạo ghi chép cuối cùng: 2-3 giờ

**Tổng: 9-12 giờ**

---

## Tham khảo Lệnh Hữu ích

### Lệnh ADB
```bash
# Liệt kê thiết bị
adb devices

# Quyền root
adb root

# Remount hệ thống
adb remount

# Cài đặt APK
adb install -r app.apk

# Gỡ cài đặt app
adb uninstall com.example.smc

# Xem logs
adb logcat | grep "TAG"

# Screenshot
adb exec-out screencap -p > screenshot.png

# Liệt kê packages
adb shell pm list packages | grep smc
```

### Lệnh Emulator
```bash
# Liệt kê AVDs
emulator -list-avds

# Khởi động emulator
emulator -avd SMC_Test_Device

# Với tùy chọn
emulator -avd SMC_Test_Device -writable-system -http-proxy 127.0.0.1:8080

# Kill tất cả emulators
adb emu kill
```

### Lệnh Gradle
```bash
# Clean build
./gradlew clean

# Build debug APK
./gradlew assembleDebug

# Liệt kê tasks
./gradlew tasks

# Build với logs
./gradlew assembleDebug --info
```

---

## Tài nguyên

### Dành riêng cho Mac M4
- Android Studio cho Mac ARM64: https://developer.android.com/studio
- Burp Suite cho Mac ARM64: https://portswigger.net/burp/releases
- Homebrew: https://brew.sh

### Tài nguyên Chung
- Tài liệu Burp Suite: https://portswigger.net/burp/documentation
- Android SSL Pinning Bypass: https://github.com/ac-pm/Inspeckage
- Frida SSL Pinning Bypass: https://codeshare.frida.re/@pcipolloni/universal-android-ssl-pinning-bypass-with-frida/
- Android Emulator Networking: https://developer.android.com/studio/run/emulator-networking
- Tham khảo ADB: https://developer.android.com/tools/adb

### Công cụ
- Objection: https://github.com/sensepost/objection
- Frida: https://frida.re
- APKTool: https://ibotpeaches.github.io/Apktool/
- ripgrep: https://github.com/BurntSushi/ripgrep

---

## Danh sách Kiểm tra Bắt đầu Nhanh

- [ ] Cài đặt Homebrew
- [ ] Cài đặt Java 17 qua Homebrew
- [ ] Tải xuống và cài đặt Android Studio (ARM64)
- [ ] Tải xuống và cài đặt Burp Suite (ARM64)
- [ ] Tạo Android emulator (arm64-v8a)
- [ ] Xuất chứng chỉ Burp
- [ ] Chuyển đổi chứng chỉ sang định dạng đúng
- [ ] Khởi động emulator với hệ thống có thể ghi
- [ ] Cài đặt chứng chỉ như system cert
- [ ] Cấu hình cài đặt proxy
- [ ] Clone repository client SMC
- [ ] Build client SMC trong Android Studio
- [ ] Cài đặt app trên emulator
- [ ] Xác minh Burp chặn bắt lưu lượng
- [ ] Bắt đầu chặn bắt API

---

Chúc may mắn với Task 3.1 trên Mac M4 của bạn!

