# Hướng Dẫn Bypass SSL Certificate Pinning cho Android App

## Tổng Quan

Document này mô tả chi tiết quá trình bypass SSL Certificate Pinning cho app SecureChat (SMC) để có thể intercept HTTPS traffic bằng Burp Suite.

## Môi Trường

- **OS**: macOS ARM64 (M4)
- **Android Studio**: ARM64 version
- **Emulator**: Android 13 (API 33) ARM64
- **Burp Suite**: Community Edition v2025.8.7 ARM64
- **Java**: OpenJDK 17.0.16
- **Tools**: apktool, apksigner, adb

## Vấn Đề Gặp Phải

App SecureChat có **multiple layers SSL security**:

1. **System Certificate Trust** - Không trust Burp CA certificate
2. **OkHttp CertificatePinner** - Hardcoded certificate pinning
3. **Custom SSL Validation** - App logic check SSL errors

## Giải Pháp Thực Hiện

### Bước 1: Cài Đặt Môi Trường

```bash
# Cài Android Studio ARM64
brew install --cask android-studio

# Tạo emulator với writable system
emulator -avd SMC_Test_Device -writable-system -http-proxy 127.0.0.1:8080 &

# Cài Burp CA certificate vào system
adb root
adb remount
adb push 01-setup/9a5ba575.0 /system/etc/security/cacerts/
adb shell chmod 644 /system/etc/security/cacerts/9a5ba575.0
adb reboot
```

### Bước 2: Xuất và Cài Đặt Burp Certificate

```bash
# Xuất certificate từ Burp Suite
# Proxy → Settings → Import/export CA certificate → DER format

# Convert DER to PEM
openssl x509 -inform DER -in burp-cert.der -out burp-cert.pem

# Tạo hash-named certificate
HASH=$(openssl x509 -inform PEM -subject_hash_old -in burp-cert.pem | head -1)
cp burp-cert.pem ${HASH}.0

# Cài vào user store (manual trong emulator Settings)
adb push burp-cert.der /sdcard/Download/burp-cert.cer
```

### Bước 3: Decompile và Patch APK

```bash
# Cài apktool
brew install apktool

# Decompile APK
apktool d 02-apk-files/secure-app.apk -o 03-decompiled/secure-app-decompiled -f
```

### Bước 4: Tạo Network Security Config

```xml
<!-- 03-decompiled/secure-app-decompiled/res/xml/network_security_config.xml -->
<?xml version="1.0" encoding="utf-8"?>
<network-security-config>
    <base-config cleartextTrafficPermitted="true">
        <trust-anchors>
            <certificates src="system"/>
            <certificates src="user"/>
        </trust-anchors>
    </base-config>
    <debug-overrides>
        <trust-anchors>
            <certificates src="system"/>
            <certificates src="user"/>
        </trust-anchors>
    </debug-overrides>
</network-security-config>
```

### Bước 5: Patch AndroidManifest.xml

```xml
<!-- Thêm networkSecurityConfig vào application tag -->
<application
    android:networkSecurityConfig="@xml/network_security_config"
    android:theme="@style/Theme.AppCompat.Light.DarkActionBar">
```

### Bước 6: Patch OkHttp CertificatePinner

**File**: `03-decompiled/secure-app-decompiled/smali/okhttp3/CertificatePinner.smali`

**Patch 1**: Method `check(String, List)`

```smali
.method public final check(Ljava/lang/String;Ljava/util/List;)V
    # SSL Pinning Bypass - return immediately
    return-void
.end method
```

**Patch 2**: Method `check(String, Certificate[])`

```smali
.method public final varargs check(Ljava/lang/String;[Ljava/security/cert/Certificate;)V
    # SSL Pinning Bypass - return immediately
    return-void
.end method
```

**Patch 3**: Method `check$okhttp` - Không throw exception

```smali
# Thay thế:
# new-instance v3, Ljavax/net/ssl/SSLPeerUnverifiedException;
# invoke-direct {v3, v2}, Ljavax/net/ssl/SSLPeerUnverifiedException;-><init>(Ljava/lang/String;)V
# throw v3

# Bằng:
# SSL Bypass - do not throw exception
# SSL Bypass - skip exception init
return-void
```

### Bước 7: Patch Custom SSL Validation

**File**: `03-decompiled/secure-app-decompiled/smali_classes4/com/example/securechat/LoginActivity.smali`

**Method**: `handleNetworkError`

```smali
.method private handleNetworkError(Ljava/io/IOException;)V
    .locals 2
    .param p1, "e"    # Ljava/io/IOException;

    .line 710
    const-string v0, "LoginActivity"
    const-string v1, "Network error"
    invoke-static {v0, v1, p1}, Landroid/util/Log;->e(Ljava/lang/String;Ljava/lang/String;Ljava/lang/Throwable;)I

    .line 713
    # SSL Pinning Bypass - skip all SSL checks
    return-void
.end method
```

### Bước 8: Rebuild và Sign APK

```bash
# Rebuild APK
apktool b 03-decompiled/secure-app-decompiled -o 02-apk-files/secure-app-patched.apk

# Tạo debug keystore
keytool -genkey -v -keystore 02-apk-files/debug.keystore -storepass android \
    -alias androiddebugkey -keypass android -keyalg RSA -keysize 2048 \
    -validity 10000 -dname "CN=Debug, OU=Debug, O=Debug, L=Debug, ST=Debug, C=US"

# Sign APK
$ANDROID_HOME/build-tools/*/apksigner sign --ks 02-apk-files/debug.keystore \
    --ks-pass pass:android --key-pass pass:android 02-apk-files/secure-app-patched.apk

# Cài đặt
adb uninstall com.example.securechat
adb install 02-apk-files/secure-app-patched.apk
```

## Kết Quả

- ✅ **SSL Certificate Pinning bypassed hoàn toàn**
- ✅ **App login thành công**
- ✅ **Burp Suite capture được HTTPS traffic**
- ✅ **Có thể intercept API calls đến server**

## Lỗi Thường Gặp và Giải Pháp

### 1. "Trust anchor for certification path not found"

**Nguyên nhân**: Certificate chưa được trust
**Giải pháp**: Cài Burp certificate vào user store và thêm network_security_config.xml

### 2. "SSL Certificate pinning failed"

**Nguyên nhân**: OkHttp CertificatePinner vẫn hoạt động
**Giải pháp**: Patch tất cả methods trong CertificatePinner.smali

### 3. "Certificate pinning failure!"

**Nguyên nhân**: Custom SSL validation trong app logic
**Giải pháp**: Patch handleNetworkError method trong LoginActivity

### 4. App crash sau patch

**Nguyên nhân**: Patch không đúng syntax smali
**Giải pháp**: Kiểm tra lại syntax và rebuild

## Tools và Commands Hữu Ích

```bash
# Kiểm tra certificate đã cài
adb shell ls -la /system/etc/security/cacerts/ | grep 9a5ba575

# Xem logcat để debug
adb logcat -d | grep -i "securechat\|ssl\|certificate"

# Kiểm tra app processes
adb shell ps -A | grep securechat

# Kill emulator
pkill -f emulator
```

## Tổng Kết

Việc bypass SSL Certificate Pinning yêu cầu patch **multiple layers**:

1. **System-level**: Network security config + certificate installation
2. **Library-level**: OkHttp CertificatePinner methods
3. **Application-level**: Custom SSL validation logic

Chỉ khi patch tất cả các layers này, app mới có thể hoạt động với Burp Suite proxy.
