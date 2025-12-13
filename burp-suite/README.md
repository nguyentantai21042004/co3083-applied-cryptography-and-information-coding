# SMC Exploitation Task 3.1 - Workspace

## Cấu Trúc Workspace

```
burp-suite/
├── 01-setup/                    # Certificates và setup files
│   ├── 9a5ba575.0              # Burp CA certificate (hash-named)
│   ├── burp-cert.der           # Burp certificate (DER format)
│   └── burp-cert.pem           # Burp certificate (PEM format)
├── 02-apk-files/               # APK files và keystores
│   ├── debug.keystore          # Debug keystore for signing
│   ├── secure-app.apk          # Original APK
│   ├── secure-app-patched.apk  # Patched APK (SSL pinning bypassed)
│   └── secure-app-patched.apk.idsig
├── 03-decompiled/              # Decompiled source code
│   └── secure-app-decompiled/  # APK decompiled với apktool
├── 04-screenshots/             # Burp Suite screenshots
│   └── burp-screenshots/       # API interception screenshots
│       ├── 01-authentication/
│       ├── 02-key-exchange/
│       └── 03-messaging/
├── 05-analysis/                # API analysis và reports
│   └── API-Analysis.md         # Chi tiết phân tích API calls
├── 06-documentation/           # Guides và documentation
│   ├── Phase-5-API-Interception-Guide.md
│   ├── SSL-Pinning-Bypass-Documentation.md
│   └── SSL-Pinning-Bypass-Guide.md
├── document/                   # Requirements từ assignment
│   ├── about-apk.md
│   ├── cleanup.md
│   ├── concepts.md
│   ├── description.md
│   ├── guide-updates-summary.md
│   ├── guide.md
│   └── UPDATE.md
├── .kiro/                      # Kiro IDE specs
│   └── specs/smc-exploitation-task-3.1/
└── README.md                   # File này
```

## Trạng Thái Hiện Tại

### ✅ Đã Hoàn Thành

- **Phase 0**: Workspace restructure & cleanup
- **Phase 1-4**: Environment setup, certificate installation, SSL pinning bypass
- **SSL Pinning Bypass**: App có thể login và Burp Suite capture traffic

### 🎯 Tiếp Theo

- **Phase 5**: API Interception (Tasks 14-18)
- **Phase 6**: Source Code Mapping (Tasks 19-20)
- **Phase 7**: Documentation (Tasks 21-22)

## Quick Commands

### Khởi động Emulator với Proxy

```bash
pkill -f emulator
emulator -avd SMC_Test_Device -writable-system -http-proxy 127.0.0.1:8080 &
```

### Cài đặt Patched APK

```bash
adb uninstall com.example.securechat
adb install 02-apk-files/secure-app-patched.apk
```

### Kiểm tra Certificate

```bash
adb shell ls -la /system/etc/security/cacerts/ | grep 9a5ba575
```

## Files Đã Xóa (Cleanup)

- `Burp_Suite_Professional_-_licensed_to_trial_user.txt` (license text)
- `CMC_Test.burp` và `CMC_Test.burp.backup` (temp Burp files)
- `assigment.apk` (typo filename, duplicate)
- `smc-client/` (empty repository)

## Ghi Chú

- Tất cả paths trong documentation đã được cập nhật
- Workspace được tổ chức theo phases của assignment
- Ready để tiếp tục Phase 5 - API Interception
