# Task 3.1: Hiểu biết Khái niệm - Bức tranh Tổng thể

## Mục lục
1. [Chúng ta đang thực sự làm gì?](#chúng-ta-đang-thực-sự-làm-gì)
2. [Kiến trúc: Mọi thứ Kết hợp với nhau như thế nào](#kiến-trúc-mọi-thứ-kết-hợp-với-nhau-như-thế-nào)
3. [Phân tích Sâu về Các Thành phần](#phân-tích-sâu-về-các-thành-phần)
4. [Luồng Dữ liệu](#luồng-dữ-liệu)
5. [Tại sao Mỗi Bước lại Quan trọng](#tại-sao-mỗi-bước-lại-quan-trọng)
6. [Mô hình Tư duy](#mô-hình-tư-duy)
7. [Những Hiểu lầm Thường gặp](#những-hiểu-lầm-thường-gặp)

---

## Chúng ta đang thực sự làm gì?

### Mục tiêu Cốt lõi
Bạn đang trở thành một **chuyên gia phân tích bảo mật** điều tra cách thức hoạt động của một hệ thống nhắn tin an toàn bằng cách:
1. **Quan sát** giao tiếp giữa client và server
2. **Ghi chép** dữ liệu được trao đổi
3. **Hiểu** cách các cơ chế bảo mật hoạt động
4. **Chuẩn bị** để tìm lỗ hổng (Task 3.2 và 3.3)

### Ví dụ Thực tế
Hãy nghĩ về nó như sau:

**Tình huống:** Bạn là một thanh tra bưu điện điều tra cách thức hoạt động của hệ thống thư tín an toàn.

- **Client (Ứng dụng Android)** = Một người gửi thư
- **Server** = Bưu điện nhận thư
- **Burp Suite** = Bạn, ngồi ở giữa, kiểm tra từng lá thư
- **Mạng** = Tuyến đường giao thư
- **API Calls** = Từng lá thư được gửi qua lại
- **Mã hóa** = Phong bì và niêm phong bảo vệ nội dung

Bạn đang chặn bắt và đọc những lá thư này (có sự cho phép!) để hiểu:
- Thông tin nào đang được trao đổi?
- Các niêm phong (mã hóa) được áp dụng như thế nào?
- Đâu có thể có điểm yếu?

---

## Kiến trúc: Mọi thứ Kết hợp với nhau như thế nào

### Sơ đồ Bức tranh Tổng thể

```
┌─────────────────────────────────────────────────────────────┐
│                      MAC M4 CỦA BẠN                          │
│                                                              │
│  ┌──────────────┐         ┌──────────────┐                 │
│  │   Android    │         │     Burp     │                  │
│  │   Emulator   │◄───────►│    Suite     │                  │
│  │              │  Proxy   │  (Proxy tại  │                  │
│  │  ┌────────┐  │ Config   │  127.0.0.1   │                  │
│  │  │  SMC   │  │         │   :8080)     │                  │
│  │  │  App   │  │         │              │                  │
│  │  └────────┘  │         │  ┌────────┐  │                  │
│  │              │         │  │Chặn bắt│ │                  │
│  │  10.0.2.2    │         │  │ & Ghi   │ │                  │
│  │  :8080       │         │  └────────┘  │                  │
│  └──────────────┘         └──────────────┘                  │
│         │                         │                          │
│         └─────────────┬───────────┘                          │
│                       │                                      │
│                       ▼                                      │
│              Kết nối Internet                                │
└──────────────────────────┬───────────────────────────────────┘
                           │
                           │ HTTPS/HTTP
                           │
                           ▼
                  ┌─────────────────┐
                  │   SMC Server    │
                  │   (Từ xa)       │
                  │                 │
                  │  - Xử lý auth  │
                  │  - Trao đổi khóa│
                  │  - Tin nhắn     │
                  └─────────────────┘
```

### Vai trò của Các Thành phần

| Thành phần | Vai trò | Tại sao Nó Tồn tại |
|-----------|------|---------------|
| **Ứng dụng SMC Android** | Client đang được kiểm thử | Đây là những gì bạn đang phân tích - "đối tượng" |
| **Android Emulator** | Thiết bị Android ảo | Chạy ứng dụng trong môi trường được kiểm soát mà bạn có thể thao tác |
| **Burp Suite** | Proxy Man-in-the-Middle | Chặn bắt và ghi log tất cả lưu lượng giữa app và server |
| **SMC Server** | Ứng dụng backend | Xử lý xác thực, trao đổi khóa, nhắn tin |
| **Mac M4 của bạn** | Máy chủ | Chạy tất cả các thành phần local |

---

## Phân tích Sâu về Các Thành phần

### 1. Android Emulator - Môi trường Được Kiểm soát

#### Nó là gì
Một điện thoại Android ảo chạy trên Mac của bạn, sử dụng kiến trúc ARM64 (native cho chip M4).

#### Tại sao Chúng ta Sử dụng Nó (Thay vì Điện thoại Thật)
- **Kiểm soát Hoàn toàn:** Có thể sửa đổi file hệ thống (cài đặt chứng chỉ như system certs)
- **Quyền Root:** Có thể sử dụng `adb root` để có quyền superuser
- **Hệ thống Có thể Ghi:** Có thể sửa đổi phân vùng `/system` mà trên thiết bị thật là read-only
- **Không có Ràng buộc Vật lý:** Không cần cáp USB, dễ reset, có thể có nhiều instance
- **Thân thiện với Nhà phát triển:** Dễ tích hợp với Android Studio, công cụ debug

#### Nó Làm gì trong Thiết lập của Chúng ta
1. Chạy ứng dụng SMC
2. Định tuyến tất cả lưu lượng mạng qua Burp proxy (10.0.2.2:8080)
3. Tin tưởng chứng chỉ của Burp (sau khi chúng ta cài đặt nó như system cert)
4. Hoạt động như thể nó là một điện thoại Android thật từ góc nhìn của ứng dụng

#### Địa chỉ Đặc biệt: 10.0.2.2
Đây là một địa chỉ đặc biệt trong Android emulator:
- `10.0.2.2` = Máy chủ của bạn (Mac M4)
- `127.0.0.1` bên trong emulator = Chính emulator đó
- Vì vậy khi app kết nối đến `10.0.2.2:8080`, nó đến Burp trên Mac của bạn

**Tại sao không sử dụng IP thật của Mac?**
- Không cần cấu hình mạng
- Hoạt động offline
- Nhất quán qua các môi trường mạng khác nhau
- Thiết lập đơn giản hơn

---

### 2. Burp Suite - Proxy Chặn bắt

#### Nó là gì
Một công cụ kiểm thử bảo mật ngồi giữa client và server, hoạt động như một "man-in-the-middle."

#### Khái niệm: Man-in-the-Middle (MITM)

```
Luồng Bình thường:
Client ──────────────────────► Server
       (lưu lượng được mã hóa)

Với Burp Suite:
Client ──────► Burp Suite ──────► Server
       giải mã           mã hóa

Những gì Burp thấy:
- Request được giải mã từ client
- Phiên bản được mã hóa gửi đến server
- Response được mã hóa từ server
- Phiên bản được giải mã gửi đến client
```

#### Tại sao Điều này Hoạt động (Mẹo Chứng chỉ)

**Vấn đề:**
- Ứng dụng sử dụng HTTPS (giao tiếp được mã hóa)
- HTTPS ngăn chặn các cuộc tấn công man-in-the-middle bằng chứng chỉ
- Server có chứng chỉ hợp pháp được ký bởi Certificate Authority (CA) đáng tin cậy

**Giải pháp:**
- Cài đặt chứng chỉ của Burp trên Android như một CA "đáng tin cậy"
- Bây giờ Android tin tưởng chứng chỉ của Burp
- Burp tạo chứng chỉ giả cho mỗi kết nối
- Android nghĩ Burp là server thật

**Quy trình:**
```
1. App muốn nói chuyện với server.example.com
2. App kết nối đến Burp (nghĩ đó là server)
3. Burp hiển thị chứng chỉ cho server.example.com (được ký bởi CA của Burp)
4. Android kiểm tra: "Chứng chỉ này có được ký bởi CA đáng tin cậy không?"
5. Android thấy CA của Burp trong system certificates: "Có, đáng tin cậy!"
6. App chấp nhận kết nối
7. Burp bây giờ thấy tất cả lưu lượng ở dạng plaintext
8. Burp tạo kết nối thật đến server.example.com
9. Burp chuyển tiếp các request được giải mã (mã hóa lại cho server thật)
```

#### Tại sao Cài đặt như System Certificate?

**Bảo mật Android 7.0+:**
- Chứng chỉ do người dùng cài đặt: Chỉ được tin tưởng bởi trình duyệt, không phải apps
- System certificates: Được tin tưởng bởi tất cả apps

**Nhu cầu của Chúng ta:**
- Ứng dụng SMC cần tin tưởng chứng chỉ của Burp
- Phải cài đặt trong `/system/etc/security/cacerts/`
- Yêu cầu quyền root và phân vùng hệ thống có thể ghi
- Đó là lý do chúng ta sử dụng cờ `-writable-system`

#### Những gì Burp Chặn bắt
- **HTTP History:** Mọi request và response
- **Headers:** Siêu dữ liệu về request (loại nội dung, auth tokens, v.v.)
- **Body:** Dữ liệu thực tế được gửi (JSON, XML, v.v.)
- **Timing:** Khi nào mỗi request được thực hiện
- **TLS Info:** Chi tiết chứng chỉ, cipher suites

---

### 3. Ứng dụng SMC - Đối tượng

#### Nó là gì
Một ứng dụng Android triển khai Thành phần Nhắn tin An toàn (Secure Messaging Component - SMC) với:
- Xác thực người dùng
- Trao đổi khóa mật mã
- Nhắn tin được mã hóa

#### Ba Giai đoạn Chúng ta đang Nghiên cứu

```
Giai đoạn 1: Xác thực
┌─────────┐              ┌─────────┐
│  App    │─────login───►│ Server  │
│         │◄───token────│         │
└─────────┘              └─────────┘
Mục đích: Chứng minh danh tính, lấy access token

Giai đoạn 2: Trao đổi Khóa
┌─────────┐              ┌─────────┐
│  App    │──client_pk──►│ Server  │
│         │◄─server_pk───│         │
└─────────┘              └─────────┘
Mục đích: Thiết lập shared secret cho mã hóa

Giai đoạn 3: Nhắn tin An toàn
┌─────────┐              ┌─────────┐
│  App    │─encrypted_msg►│ Server  │
│         │◄encrypted_msg─│         │
└─────────┘              └─────────┘
Mục đích: Trao đổi tin nhắn được mã hóa
```

#### Tại sao Chúng ta Nghiên cứu Mã nguồn
Ứng dụng là mã nguồn mở, vì vậy chúng ta có thể:
1. **Ánh xạ network calls đến code:** "API call này đến từ dòng 45 trong KeyExchange.java"
2. **Hiểu các thao tác crypto:** Xem cách khóa được tạo, cách mã hóa hoạt động
3. **Tìm lỗ hổng triển khai:** Tìm kiếm các lỗi trong code
4. **Xác minh quan sát của chúng ta:** Xác nhận những gì chúng ta thấy trong Burp khớp với code

---

### 4. SMC Server - Mục tiêu

#### Nó là gì
Một server từ xa (được cung cấp bởi giảng viên của bạn) mà:
- Xác thực người dùng
- Thực hiện trao đổi khóa
- Lưu trữ và chuyển tiếp tin nhắn được mã hóa

#### Tại sao Chúng ta Không Kiểm soát Nó
Điều này mô phỏng một tình huống thực tế:
- Bạn đang kiểm thử một client chống lại một server sản xuất
- Bạn có thể quan sát, nhưng không thể sửa đổi hành vi server
- Buộc bạn hiểu giao thức từ góc nhìn của client
- Làm cho việc khai thác thực tế hơn (cho Task 3.3)

#### Những gì Nó Tiết lộ
RESTful API endpoints như:
- `POST /api/auth/login`
- `POST /api/keyexchange/init`
- `POST /api/message/send`
- v.v.

---

## Luồng Dữ liệu

### Luồng Hoàn chỉnh: Gửi Tin nhắn Đầu tiên của Bạn

Hãy theo dõi một tin nhắn "Hello" qua toàn bộ hệ thống:

#### Bước 1: App Tạo Request
```java
// Trong ứng dụng Android (dòng 67 của MessageService.java)
POST /api/message/send
Headers:
  Authorization: Bearer eyJhbGc...
  Content-Type: application/json
Body:
  {
    "recipientId": "user123",
    "encryptedMessage": "a3d8f92b...",
    "signature": "9f2e3a..."
  }
```

#### Bước 2: Emulator Định tuyến đến Burp
```
App nghĩ nó đang gửi đến: https://smc-server.com/api/message/send
Thực tế gửi đến: 10.0.2.2:8080 (Burp trên Mac của bạn)
Cấu hình proxy của emulator chuyển hướng tất cả lưu lượng qua Burp
```

#### Bước 3: Burp Chặn bắt
```
Burp nhận kết nối HTTPS được mã hóa
Burp giải mã bằng chứng chỉ của nó (mà Android tin tưởng)
Burp hiển thị cho bạn plaintext:
  - URL: https://smc-server.com/api/message/send
  - Method: POST
  - Headers: [danh sách headers]
  - Body: {"recipientId":"user123",...}
```

#### Bước 4: Bạn Ghi chép Nó
```
Đã chụp màn hình
Các trường đã được ghi chép:
  - recipientId: string - ID người dùng của người nhận tin nhắn
  - encryptedMessage: base64 - Tin nhắn được mã hóa với shared key
  - signature: base64 - Chữ ký HMAC cho xác thực
```

#### Bước 5: Burp Chuyển tiếp đến Server Thật
```
Burp tạo kết nối HTTPS mới đến server thật
Gửi request giống hệt (mã hóa lại với cert của server)
Server không biết Burp đang ở giữa
```

#### Bước 6: Server Phản hồi
```
Server xử lý request:
  - Xác thực chữ ký
  - Lưu trữ tin nhắn được mã hóa
  - Trả về response thành công

Response:
{
  "status": "success",
  "messageId": "msg_789",
  "timestamp": 1234567890
}
```

#### Bước 7: Burp Chặn bắt Response
```
Burp nhận response được mã hóa từ server
Burp giải mã nó
Burp hiển thị cho bạn plaintext response
Bạn ghi chép nó
```

#### Bước 8: Burp Trả về App
```
Burp mã hóa lại response (với chứng chỉ của nó)
Gửi đến emulator
App nhận response
App nghĩ nó đã nói chuyện trực tiếp với server
```

#### Bước 9: Bạn Ánh xạ đến Code
```
Tìm kiếm codebase cho "/api/message/send"
Tìm MessageService.java:67
Ghi chép vị trí code
Hiểu cách request được xây dựng
Xem cách response được xử lý
```

---

## Tại sao Mỗi Bước lại Quan trọng

### Tại sao Cài đặt Android Studio?
**Câu trả lời Ngắn gọn:** Để build, chạy và phân tích ứng dụng SMC.

**Lý do Sâu:**
- Bạn cần **mã nguồn** để hiểu triển khai
- Bạn cần **build APK** từ mã nguồn (để đảm bảo đó là phiên bản đúng)
- Bạn cần **công cụ IDE** để tìm kiếm code, debug, hiểu cấu trúc
- Bạn cần **công cụ Android SDK** (adb, emulator) đi kèm

**Không có Nó:**
- Bạn có thể tải APK đã build sẵn, nhưng không thể phân tích mã nguồn
- Bạn không thể sửa đổi ứng dụng nếu cần
- Bạn sẽ bỏ lỡ hiểu biết về cách crypto được triển khai

---

### Tại sao Tạo ARM64 Emulator?
**Câu trả lời Ngắn gọn:** Để chạy ứng dụng trong môi trường được kiểm soát.

**Lý do Sâu:**
- **Kiến trúc ARM64** khớp với chip M4 = hiệu suất tốt hơn (không có x86 translation)
- **Emulator** cung cấp quyền root = có thể cài đặt system certificates
- **Hệ thống có thể ghi** = có thể sửa đổi các phân vùng read-only
- **Không có thiết bị vật lý** = thuận tiện hơn, có thể lặp lại, có thể reset

**Không có Nó:**
- Thiết bị vật lý: khó root hơn, không thể dễ dàng reset, rủi ro brick
- x86 emulator: chậm hơn trên M4, overhead translation
- Không có emulator: không thể dễ dàng chặn bắt lưu lượng, kiểm soát hạn chế

---

### Tại sao Cấu hình Proxy Settings?
**Câu trả lời Ngắn gọn:** Để định tuyến tất cả lưu lượng app qua Burp.

**Lý do Sâu:**
Định tuyến lưu lượng mạng:
```
Mặc định:
App → Android OS → Network Interface → Internet → Server

Với Proxy:
App → Android OS → Proxy Config → Burp (10.0.2.2:8080) → Server
```

**Hai Phương pháp:**

1. **Emulator Launch Flag** (`-http-proxy 127.0.0.1:8080`)
   - Đặt proxy toàn cục cho toàn bộ emulator
   - Hoạt động cho tất cả apps
   - Áp dụng ở cấp độ emulator

2. **WiFi Proxy Settings**
   - Đặt proxy cho kết nối WiFi
   - Cài đặt cấp người dùng
   - Giống như những gì bạn sẽ làm trên điện thoại thật

**Không có Nó:**
- Lưu lượng đi trực tiếp đến server
- Burp không thấy gì
- Không thể chặn bắt hoặc phân tích

---

### Tại sao Cài đặt Burp Certificate như System Certificate?
**Câu trả lời Ngắn gọn:** Để app tin tưởng chứng chỉ giả của Burp.

**Lý do Sâu:**

**Chuỗi Tin cậy:**
```
1. App muốn kết nối HTTPS
2. Burp trình bày chứng chỉ cho server
3. Chứng chỉ được ký bởi CA của Burp
4. Android kiểm tra: "Tôi có tin tưởng CA này không?"
5. Tìm trong /system/etc/security/cacerts/
6. Tìm thấy CA của Burp: "Có, đáng tin cậy!"
7. Kết nối được phép
```

**Chứng chỉ Người dùng vs Hệ thống:**
```
Chứng chỉ Người dùng (/data/misc/user/0/cacerts-added/)
  - Được cài đặt bởi người dùng
  - Được tin tưởng bởi: Trình duyệt, một số apps
  - KHÔNG được tin tưởng bởi: Hầu hết apps (Android 7+)

System Certificates (/system/etc/security/cacerts/)
  - Được cài đặt sẵn với Android
  - Được tin tưởng bởi: TẤT CẢ apps
  - Yêu cầu: Quyền root để cài đặt
```

**Tại sao Tên File Hash?**
```bash
# Chứng chỉ: 9a5ba575.0
# 9a5ba575 = hash của certificate subject
# .0 = chứng chỉ đầu tiên với hash này (có thể là .1, .2, v.v.)

# Android tra cứu chứng chỉ theo hash để tối ưu hiệu suất
# Thay vì đọc tất cả certs, nó tính hash và tìm file đó
```

**Không có Nó:**
- App từ chối chứng chỉ của Burp
- Lỗi SSL/TLS: "Untrusted certificate"
- Không có lưu lượng được chặn bắt (kết nối thất bại)

---

### Tại sao Sử dụng Cờ `-writable-system`?
**Câu trả lời Ngắn gọn:** Để sửa đổi phân vùng hệ thống read-only.

**Lý do Sâu:**

**Bố cục Phân vùng Android:**
```
/data      - Đọc/Ghi - Dữ liệu người dùng, dữ liệu app
/sdcard    - Đọc/Ghi - File người dùng
/system    - Chỉ Đọc - File hệ thống, apps, chứng chỉ
```

**Vấn đề:**
- Cần cài đặt chứng chỉ trong `/system/etc/security/cacerts/`
- `/system` được mount read-only để bảo mật
- Không thể ghi vào nó bình thường

**Giải pháp:**
```bash
# Phương pháp 1: Cờ Writable System
emulator -avd SMC_Test_Device -writable-system
# Mount /system như read-write từ boot

# Phương pháp 2: Remount
adb root
adb remount
# Remount /system như read-write tại runtime
```

**Không có Nó:**
```bash
adb push cert.pem /system/etc/security/cacerts/
# Lỗi: Read-only file system
```

---

### Tại sao Quyền Root (`adb root`)?
**Câu trả lời Ngắn gọn:** Để có quyền superuser để sửa đổi file hệ thống.

**Lý do Sâu:**

**Quyền Linux:**
```
$ ls -la /system/etc/security/cacerts/
drwxr-xr-x root root   - cacerts
-rw-r--r-- root root 1234 12345678.0
```
- Chủ sở hữu: root
- Chỉ root mới có thể ghi vào thư mục này

**Những gì `adb root` Làm:**
```
ADB Bình thường:
$ adb shell
shell@android:/ $ whoami
shell
shell@android:/ $ ls /system/etc/security/cacerts/
Permission denied

Với adb root:
$ adb root
$ adb shell
root@android:/ # whoami
root
root@android:/ # ls /system/etc/security/cacerts/
[danh sách chứng chỉ]
```

**Không có Nó:**
- Không thể ghi vào `/system`
- Không thể `chmod` file hệ thống
- Không thể cài đặt chứng chỉ

---

### Tại sao Chuyển đổi Định dạng Chứng chỉ (DER sang PEM)?
**Câu trả lời Ngắn gọn:** Chứng chỉ hệ thống Android phải ở định dạng PEM với tên cụ thể.

**Lý do Sâu:**

**Định dạng Chứng chỉ:**
```
DER (Distinguished Encoding Rules)
- Định dạng nhị phân
- Nhỏ gọn
- Burp xuất định dạng này theo mặc định
- File: burp-cert.der

PEM (Privacy Enhanced Mail)
- DER được mã hóa Base64
- Có thể đọc được (một phần)
- Android mong đợi định dạng này
- File: 9a5ba575.0
```

**Chuyển đổi:**
```bash
# Burp cung cấp cho bạn: burp-cert.der
openssl x509 -inform DER -in burp-cert.der -out burp-cert.pem

# Android cần: [hash].0
HASH=$(openssl x509 -subject_hash_old -in burp-cert.pem | head -1)
cp burp-cert.pem ${HASH}.0
```

**Tại sao Hash?**
- Android tra cứu certs theo subject hash để hiệu quả
- Định dạng phải là: `[8-char-hex-hash].0`
- Ví dụ: `9a5ba575.0`

**Không có Nó:**
- Định dạng sai: Android không thể đọc chứng chỉ
- Tên sai: Android không thể tìm thấy chứng chỉ
- App sẽ không tin tưởng Burp

---

### Tại sao Build từ Mã nguồn (Không chỉ Tải APK)?
**Câu trả lời Ngắn gọn:** Để phân tích code và hiểu triển khai.

**Lý do Sâu:**

**Những gì Bạn Nhận được từ Mã nguồn:**
1. **Hiểu Code:**
   ```java
   // Bạn có thể thấy chính xác cách mã hóa hoạt động
   SecretKey key = generateKey();
   Cipher cipher = Cipher.getInstance("AES/GCM/NoPadding");
   cipher.init(Cipher.ENCRYPT_MODE, key);
   byte[] encrypted = cipher.doFinal(plaintext);
   ```

2. **Ánh xạ API:**
   ```java
   // Dòng 45 trong KeyExchangeService.java
   @POST("/api/keyexchange/init")
   Call<KeyExchangeResponse> initiateKeyExchange(
       @Body KeyExchangeRequest request
   );
   ```
   Bây giờ bạn biết request Burp này đến từ dòng 45!

3. **Khám phá Lỗ hổng:**
   ```java
   // Ồ, khóa được hardcode!
   private static final String SECRET_KEY = "hardcoded_secret_123";
   ```

4. **Xây dựng Request:**
   ```java
   // Request được xây dựng như thế nào?
   KeyExchangeRequest request = new KeyExchangeRequest();
   request.setUserId(userId);
   request.setPublicKey(Base64.encode(publicKey));
   request.setTimestamp(System.currentTimeMillis());
   ```

**Chỉ APK Đã Build Sẵn:**
- Bạn thấy lưu lượng mạng trong Burp
- Nhưng không biết nó đến từ đâu trong code
- Không thể hiểu triển khai crypto
- Khó tìm lỗ hổng hơn

---

## Mô hình Tư duy

### Mô hình Tư duy 1: Ví dụ Bưu điện Mở rộng

```
Ứng dụng Android = Người viết thư
  - Soạn tin nhắn
  - Bỏ vào phong bì (mã hóa)
  - Viết địa chỉ (API endpoint)
  - Thêm chữ ký (xác thực)

Burp Suite = Thanh tra bưu điện
  - Mở mọi phong bì
  - Đọc nội dung
  - Ghi log thông tin
  - Niêm phong lại phong bì
  - Gửi đến đích

Server = Người nhận
  - Nhận phong bì
  - Xác minh người gửi
  - Đọc tin nhắn
  - Viết phản hồi

Công việc của Bạn = Ghi chép hệ thống bưu điện
  - Có gì trong mỗi lá thư?
  - Phong bì được niêm phong như thế nào?
  - Địa chỉ nào được sử dụng?
  - Đâu có thể bảo mật yếu?
```

---

### Mô hình Tư duy 2: Dây chuyền Lắp ráp

```
Luồng Request (Trái sang Phải):
[App] → [Emulator] → [Burp] → [Internet] → [Server]
  ↑         ↑          ↑
  Tạo    Định tuyến  Kiểm tra

Luồng Response (Phải sang Trái):
[App] ← [Emulator] ← [Burp] ← [Internet] ← [Server]
  ↑         ↑          ↑
 Xử lý   Định tuyến  Kiểm tra

Bạn = Thanh tra chất lượng tại trạm Burp
- Xem mọi mục đi qua
- Ghi chép thông số kỹ thuật
- Tìm kiếm khuyết tật
```

---

### Mô hình Tư duy 3: Các Lớp

```
Lớp Ứng dụng:  [Logic App SMC]
                           ↓
Lớp Mạng:      [HTTP/HTTPS Requests]
                           ↓
Lớp Vận chuyển:    [Kết nối TCP]
                           ↓
Lớp Proxy:        [Chặn bắt Burp] ← Bạn quan sát ở đây
                           ↓
Lớp Vật lý:     [Network Interface]
                           ↓
                    [Internet]
                           ↓
                    [Server]
```

Bạn đang làm việc ở Lớp Proxy:
- Trên: Logic ứng dụng (nghiên cứu code)
- Tại: Network requests (chặn bắt với Burp)
- Dưới: Không quan tâm (được xử lý bởi OS)

---

## Những Hiểu lầm Thường gặp

### Hiểu lầm 1: "Burp hack mã hóa"
**Thực tế:** Burp không phá vỡ mã hóa. Nó lừa app tin tưởng nó.

```
App mã hóa → Burp giải mã (sử dụng tin cậy) → Burp mã hóa lại → Server

KHÔNG PHẢI:
App mã hóa → Burp phá vỡ mã hóa → Server
```

---

### Hiểu lầm 2: "Chúng ta cần điện thoại Android vật lý"
**Thực tế:** Emulator tốt hơn cho kiểm thử bảo mật vì:
- Kiểm soát hoàn toàn (quyền root)
- Hệ thống có thể ghi
- Dễ reset
- Không rủi ro cho thiết bị cá nhân
- Tốt hơn cho học tập

---

### Hiểu lầm 3: "Proxy làm chậm app"
**Thực tế:** Tác động tối thiểu vì:
- Burp chạy local (không có độ trễ mạng)
- Burp nhanh
- Độ trễ chính là từ việc ghi chép (bạn click qua)

---

### Hiểu lầm 4: "System certificate = kém an toàn hơn"
**Thực tế:** Đó là môi trường kiểm thử được kiểm soát:
- Chỉ emulator của bạn bị ảnh hưởng
- Chỉ cert của Burp được tin tưởng
- Cô lập khỏi thiết bị Android thật
- Cho mục đích giáo dục

Không bao giờ làm điều này trên điện thoại hàng ngày của bạn!

---

### Hiểu lầm 5: "Tôi có thể bỏ qua mã nguồn"
**Thực tế:** Mã nguồn là cần thiết vì:
- Task 3.1 yêu cầu ánh xạ APIs đến vị trí code
- Task 3.2 yêu cầu hiểu triển khai giao thức
- Task 3.3 yêu cầu tìm lỗ hổng trong code
- Không có code, bạn chỉ đang đoán

---

## Con đường Học tập

### Những gì Bạn đang Hướng tới

**Task 3.1 (Hiện tại):**
- **Kỹ năng:** Quan sát và ghi chép
- **Đầu ra:** Bản đồ tất cả giao tiếp API
- **Nền tảng cho:** Hiểu giao thức

**Task 3.2 (Tiếp theo):**
- **Kỹ năng:** Tái cấu trúc giao thức
- **Đầu ra:** Tái triển khai client
- **Nền tảng cho:** Tìm lỗ hổng

**Task 3.3 (Cuối cùng):**
- **Kỹ năng:** Khai thác
- **Đầu ra:** Proof-of-concept exploit hoạt động
- **Nền tảng cho:** Kiểm thử bảo mật thực tế

**Sự Tiến triển:**
```
Task 3.1: Điều gì đang xảy ra?
    ↓
Task 3.2: Nó hoạt động như thế nào?
    ↓
Task 3.3: Nó bị hỏng ở đâu?
```

---

## Tham khảo Nhanh: Tại sao Mỗi Thành phần

| Thành phần | Mục đích | Nó Làm gì | Tại sao Nó Cần thiết |
|-----------|---------|--------------|-------------------|
| **Mac M4** | Môi trường chủ | Chạy mọi thứ | Không gian làm việc của bạn |
| **Android Studio** | IDE phát triển | Build app, quản lý emulator | Phân tích mã nguồn |
| **ARM64 Emulator** | Môi trường kiểm thử | Chạy ứng dụng Android | Kiểm thử được kiểm soát |
| **Burp Suite** | MITM Proxy | Chặn bắt lưu lượng | Xem tất cả giao tiếp |
| **Burp Certificate** | Cơ chế tin cậy | Cho phép chặn bắt HTTPS | Giải mã lưu lượng |
| **System Cert Install** | Tin cậy cấp app | Làm app tin tưởng Burp | Yêu cầu cho Android 7+ |
| **Writable System** | Sửa đổi file | Cài đặt system cert | Sửa đổi phân vùng read-only |
| **Root Access** | Quyền | Ghi file hệ thống | Cần quyền admin |
| **Proxy Config** | Định tuyến lưu lượng | Định tuyến qua Burp | Hướng lưu lượng đến proxy |
| **Mã nguồn** | Hiểu biết | Xem triển khai | Ánh xạ lưu lượng đến code |
| **10.0.2.2** | Mạng | Emulator→Mac | Địa chỉ emulator đặc biệt |

---

## Suy nghĩ Cuối cùng

Hãy nghĩ về task này như xây dựng một bản đồ hoàn chỉnh của một hệ thống giao tiếp:

1. **Setup** = Xây dựng trạm quan sát của bạn
2. **Chặn bắt** = Ghi lại tất cả giao tiếp
3. **Ghi chép** = Tạo ghi chú chi tiết
4. **Phân tích** = Hiểu những gì bạn đã quan sát
5. **Ánh xạ** = Kết nối quan sát với mã nguồn

Mọi công cụ, mọi bước, mọi cấu hình đều phục vụ mục tiêu này.

Khi bạn hiểu "tại sao," "như thế nào" trở nên rõ ràng hơn nhiều.

Chúc may mắn với cuộc điều tra của bạn!

