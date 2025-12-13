# SSL Pinning Bypass Documentation
## SMC SecureChat App - Complete Setup Guide

### Môi trường thực hiện
- **Hệ điều hành**: macOS ARM64 (Apple Silicon)
- **Android Studio**: ARM64 version
- **Burp Suite**: Community Edition v2025.8.7 ARM64
- **Android Emulator**: API 36 (Android 14), ARM64-v8a
- **Java**: OpenJDK 17.0.16

---

## Phase 1: Environment Setup

### 1.1 Android Studio & SDK Setup
```bash
# Cài đặt Android Studio ARM64
brew install --cask android-studio

# Cấu hình biến môi trường
echo 'export ANDROID_HOME=~/Library/Android/sdk' >> ~/.zshrc
echo 'export PATH=$PATH:$ANDROID_HOME/emulator:$ANDROID_HOME/platform-tools' >> ~/.zshrc
source ~/.zshrc

# Verify installation
adb --version
emulator -list-avds
```

### 1.2 Android Emulator Creation
- **Device**: Pixel 7
- **System Image**: Google APIs ARM64-v8a, API 36 (Android 14)
- **Name**: SMC_Test_Device
-