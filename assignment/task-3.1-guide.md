# Task 3.1: End-to-End Guide - API Interception & Analysis using Burp Suite
## Mac M4 Edition with Containerized Android Environment

## Overview
This guide provides step-by-step instructions for completing Task 3.1 of the SMC Exploitation assignment on Mac M4. You will set up Burp Suite as a man-in-the-middle proxy to intercept and document all API calls between an Android client and the server using Android Studio's emulator.

**Points:** 0.5
**Goal:** Intercept and document all API calls from Key Exchange to Message Exchange phases.
**Environment:** Mac M4, Android Studio IDE, Docker (optional for advanced scenarios)

---

## Prerequisites

### System Requirements
- **Mac M4** (Apple Silicon)
- **macOS Sonoma** or later
- **Homebrew** installed
- At least **8GB RAM** and **20GB free disk space**

### Required Software

1. **Burp Suite Community Edition for macOS (ARM64)**
   - Download: https://portswigger.net/burp/releases/professional-community-2025-8-7?requestededition=community&requestedplatform=
   - Choose: **macOS (ARM64)** version for M4 chip

2. **Android Studio (Apple Silicon)**
   - Download: https://developer.android.com/studio
   - Choose: **Mac (ARM64)** version
   - Includes Android SDK and ARM64 emulator optimized for M4

3. **Java Development Kit (JDK)**
   ```bash
   brew install openjdk@17
   ```

4. **SMC Client Source Code & APK**
   - Repository: https://github.com/dangduongminhnhat/Client-Assignment-Advance-Cryptography-and-Coding-Theory
   - Clone to your workspace:
   ```bash
   cd ~/Workspaces/hcmut/co3083-applied-cryptography-and-information-coding
   git clone https://github.com/dangduongminhnhat/Client-Assignment-Advance-Cryptography-and-Coding-Theory.git smc-client
   ```

### Optional Tools
- **Docker Desktop for Mac (Apple Silicon)** - for containerized testing scenarios
- **Visual Studio Code** - for code analysis
- **apktool** - for APK analysis and modification
  ```bash
  brew install apktool
  ```

---

## Step 1: Install and Configure Burp Suite on Mac M4

### 1.1 Install Burp Suite
```bash
# Download the macOS ARM64 DMG file
# Open the downloaded DMG and drag Burp Suite to Applications

# Launch from Applications or via terminal
open -a "Burp Suite Community Edition"
```

### 1.2 Initial Burp Configuration
1. Launch Burp Suite
2. Choose **Temporary project** (for quick start)
3. Use **Burp defaults** for configuration
4. Click **Start Burp**

### 1.3 Configure Burp Proxy for localhost
1. Go to **Proxy** → **Settings** → **Proxy Listeners**
2. You should see a listener on `127.0.0.1:8080`
3. Since Android Emulator runs on the same machine, we'll use special addresses:
   - For Android Emulator, `10.0.2.2` points to host's `127.0.0.1`
   - Keep the default `127.0.0.1:8080` listener

### 1.4 Export Burp CA Certificate
```bash
# Create a directory for certificates
mkdir -p ~/Desktop/burp-setup

# In Burp Suite:
# 1. Go to Proxy → Settings → Proxy Listeners
# 2. Click "Import / export CA certificate"
# 3. Select "Certificate in DER format"
# 4. Save to ~/Desktop/burp-setup/burp-cert.der

# Convert DER to PEM format (needed for Android system certs)
openssl x509 -inform DER -in ~/Desktop/burp-setup/burp-cert.der \
  -out ~/Desktop/burp-setup/burp-cert.pem

# Get the certificate hash (needed for system cert installation)
openssl x509 -inform PEM -subject_hash_old -in ~/Desktop/burp-setup/burp-cert.pem | head -1
# This will output a hash like: 9a5ba575

# Rename cert with hash
HASH=$(openssl x509 -inform PEM -subject_hash_old -in ~/Desktop/burp-setup/burp-cert.pem | head -1)
cp ~/Desktop/burp-setup/burp-cert.pem ~/Desktop/burp-setup/${HASH}.0
```

---

## Step 2: Set Up Android Studio and Emulator

### 2.1 Install Android Studio
```bash
# Download from https://developer.android.com/studio
# Install Android Studio (ARM64 version for M4)

# Or via Homebrew:
brew install --cask android-studio
```

### 2.2 Configure Android Studio
1. Launch Android Studio
2. Complete the setup wizard:
   - Install Android SDK
   - Install Android SDK Platform
   - Install Android Virtual Device (AVD)

3. Install required SDK components:
   - Open **Settings/Preferences** → **Appearance & Behavior** → **System Settings** → **Android SDK**
   - Check and install:
     - Android 13.0 (API 33) or higher
     - Android SDK Build-Tools
     - Android SDK Platform-Tools
     - Android SDK Command-line Tools

### 2.3 Create an ARM64 Android Emulator

1. Open **Device Manager** (in Android Studio toolbar)
2. Click **Create Device**
3. Choose a device definition (e.g., **Pixel 7**)
4. Select a system image:
   - Choose **arm64-v8a** architecture (optimized for M4)
   - Recommended: **Android 13.0 (API 33)** or **Android 12.0 (API 31)**
   - Download if not already installed
5. Name your AVD: `SMC_Test_Device`
6. Show **Advanced Settings**:
   - Set **RAM:** 4096 MB (or higher)
   - Enable **Cold boot**
   - Note the emulator path for later use

### 2.4 Configure Emulator Network Settings

**Method 1: Launch with Proxy (Recommended)**
```bash
# Set up environment variables
export ANDROID_HOME=~/Library/Android/sdk
export PATH=$PATH:$ANDROID_HOME/emulator:$ANDROID_HOME/platform-tools

# Launch emulator with HTTP proxy
emulator -avd SMC_Test_Device \
  -http-proxy 127.0.0.1:8080 \
  -writable-system
```

**Method 2: Set Proxy via Android Settings**
1. Launch emulator normally from Android Studio
2. In the emulator, go to **Settings** → **Network & Internet** → **Internet**
3. Long-press **AndroidWifi**
4. Select **Modify network**
5. Expand **Advanced options**
6. Set **Proxy** to **Manual**:
   - **Proxy hostname:** `10.0.2.2` (special address for host)
   - **Proxy port:** `8080`
7. Save

### 2.5 Install Burp Certificate as System Certificate

Since Android 7.0+, user-installed certificates are not trusted by apps. We need to install Burp's certificate as a system certificate.

```bash
# Start the emulator with writable system partition
emulator -avd SMC_Test_Device -writable-system &

# Wait for emulator to fully boot
adb wait-for-device

# Remount system partition as writable
adb root
adb remount

# Push the certificate to system certificates directory
# Use the hash-named file created earlier
adb push ~/Desktop/burp-setup/${HASH}.0 /system/etc/security/cacerts/

# Set correct permissions
adb shell chmod 644 /system/etc/security/cacerts/${HASH}.0

# Reboot the emulator
adb reboot

# Verify certificate installation after reboot
adb shell ls -la /system/etc/security/cacerts/ | grep ${HASH}
```

### 2.6 Verify Proxy Connection
```bash
# In emulator, open Chrome browser
# Navigate to: http://burp

# You should see the Burp Suite welcome page
# Check Burp Suite → Proxy → HTTP history for the request
```

---

## Step 3: Open SMC Client Project in Android Studio

### 3.1 Import the Project
1. In Android Studio, select **File** → **Open**
2. Navigate to the cloned repository:
   ```
   ~/Workspaces/hcmut/co3083-applied-cryptography-and-information-coding/smc-client
   ```
3. Click **Open**
4. Wait for Gradle sync to complete

### 3.2 Build the Project
```bash
# Via Android Studio: Build → Make Project
# Or via terminal:
cd ~/Workspaces/hcmut/co3083-applied-cryptography-and-information-coding/smc-client
./gradlew assembleDebug
```

### 3.3 Install APK on Emulator

**Method 1: Direct Install from Android Studio**
1. Select your emulator from the device dropdown
2. Click the **Run** button (green play icon)
3. The app will be built and installed automatically

**Method 2: Manual Install via ADB**
```bash
# Find the generated APK
find . -name "*.apk" -type f

# Install on emulator
adb install -r app/build/outputs/apk/debug/app-debug.apk

# Verify installation
adb shell pm list packages | grep smc
```

### 3.4 Disable Certificate Pinning (if needed)

If the app uses certificate pinning, you'll need to bypass it:

**Option 1: Modify network_security_config.xml**
1. Open the project in Android Studio
2. Navigate to `app/src/main/res/xml/network_security_config.xml`
3. Modify to trust user certificates:
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
4. Rebuild and reinstall

**Option 2: Use Frida for Runtime Bypass**
```bash
# Install Frida tools
pip3 install frida-tools

# Download frida-server for Android ARM64
# https://github.com/frida/frida/releases

# Push to emulator
adb push frida-server-*-android-arm64 /data/local/tmp/frida-server
adb shell chmod 755 /data/local/tmp/frida-server
adb shell /data/local/tmp/frida-server &

# Use Frida script to bypass SSL pinning
frida -U -f com.example.smc -l ssl-pinning-bypass.js
```

### 3.5 Prepare for Testing
1. Note your assigned User ID from the Google Sheet
2. Configure server endpoint in the app settings
3. Have your analysis tools ready (text editor, screenshot tool)

---

## Step 4: Intercept API Traffic

### 4.1 Start Burp Interception
1. In Burp Suite, go to **Proxy** → **Intercept**
2. Ensure **Intercept is on** (button should show this)
3. Clear any previous history: **Proxy** → **HTTP history** → Right-click → **Clear history**

### 4.2 Launch the SMC Client
1. Open the SMC app on Android
2. Start with the initial setup/login process

### 4.3 Capture Phase 1: Initial Key Exchange / Handshake
1. Begin the key exchange process in the app
2. For each request that appears in Burp:
   - **Take a screenshot** showing:
     - Request tab (URL, headers, body)
     - Response tab (status, headers, body)
   - **Document the following:**
     - API endpoint URL
     - HTTP method (GET, POST, etc.)
     - Request headers
     - Request body (if any)
     - Response status code
     - Response headers
     - Response body
   - Click **Forward** to send the request
3. Save each intercepted request/response to Burp's history

### 4.4 Capture Phase 2: Session Establishment
1. Continue through the session establishment phase
2. Repeat the documentation process for each API call
3. Take screenshots and notes

### 4.5 Capture Phase 3: Encrypted Messaging
1. Send at least 2-3 test messages through the app
2. Intercept and document each message exchange
3. Note any differences in encrypted vs. plaintext patterns

### 4.6 Save Burp Session
1. **Proxy** → **HTTP history**
2. Select all relevant requests
3. Right-click → **Save items**
4. Save as a file for reference

---

## Step 5: Analyze and Document Each API Call

For each intercepted API call, create a detailed entry with:

### 5.1 API Call Information
Create a table with these columns:

| # | Endpoint | Method | Phase | Purpose |
|---|----------|--------|-------|---------|
| 1 | /api/auth/login | POST | Authentication | User login |
| 2 | /api/keyexchange/init | POST | Key Exchange | Initialize key exchange |
| ... | ... | ... | ... | ... |

### 5.2 Request/Response Fields Documentation

For each API call, document:

**Request Fields:**
```
Endpoint: /api/keyexchange/init
Method: POST
Headers:
  - Content-Type: application/json
  - Authorization: Bearer <token>

Body Parameters:
  - userId: string - The user identifier
  - publicKey: string - Base64-encoded client public key
  - timestamp: long - Unix timestamp of request
  - nonce: string - Random nonce for replay protection
```

**Response Fields:**
```
Status: 200 OK
Headers:
  - Content-Type: application/json

Body:
  - serverPublicKey: string - Base64-encoded server public key
  - sessionId: string - Unique session identifier
  - signature: string - Server signature over the response
  - timestamp: long - Server timestamp
```

### 5.3 Map to Source Code

For each API call, find the corresponding code:

**Example:**
```
API: POST /api/keyexchange/init

Client Code:
  - File: app/src/main/java/com/example/smc/network/KeyExchangeService.java
  - Method: initiateKeyExchange()
  - Lines: 45-67

Server Code (if available):
  - File: server/src/handlers/keyexchange.js
  - Function: handleKeyExchangeInit()
  - Lines: 23-45
```

---

## Step 6: Create Deliverables

### 6.1 Screenshot Organization
Organize screenshots by phase:
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

### 6.2 Create Documentation Report

Create a document with the following structure:

```markdown
# Task 3.1: API Interception & Analysis Report

## 1. Setup Summary
- Burp Suite version: ...
- Android device/emulator: ...
- Date of testing: ...
- User ID used: ...

## 2. Intercepted API Calls Summary

### 2.1 Authentication Phase
#### API 1: User Login
- **Screenshot:** [screenshots/01-authentication/01-login-request.png]
- **Endpoint:** POST /api/auth/login
- **Request Fields:**
  - username: string - User identifier
  - password: string - User password (hashed)
  - deviceId: string - Device identifier
- **Response Fields:**
  - token: string - JWT authentication token
  - userId: string - User ID
  - expiresIn: number - Token expiration time
- **Code Location:**
  - Client: AuthService.java:23-45
  - Server: auth.controller.js:67-89

### 2.2 Key Exchange Phase
#### API 2: Initialize Key Exchange
[Similar detailed documentation]

### 2.3 Messaging Phase
#### API 3: Send Encrypted Message
[Similar detailed documentation]

## 3. API Call Mapping Table

| # | Endpoint | Method | Request Fields | Response Fields | Code Location |
|---|----------|--------|----------------|-----------------|---------------|
| 1 | /api/auth/login | POST | username, password | token, userId | AuthService.java:23 |
| 2 | /api/keyexchange/init | POST | userId, publicKey | serverPublicKey, sessionId | KeyExchangeService.java:45 |
| ... | ... | ... | ... | ... | ... |

## 4. Field Explanations

### 4.1 Authentication Fields
- **username:** ...
- **token:** ...

### 4.2 Key Exchange Fields
- **publicKey:** ...
- **serverPublicKey:** ...

### 4.3 Messaging Fields
- **encryptedMessage:** ...
- **signature:** ...

## 5. Source Code Mapping

[Detailed mapping of each API to specific files and line numbers]
```

---

## Step 7: Verification Checklist

Before submission, verify you have:

- [ ] Burp Suite screenshots for ALL API calls
- [ ] Clear, legible screenshots showing both request and response
- [ ] Documented every field in requests and responses
- [ ] Explained the purpose of each field
- [ ] Mapped each API call to source code locations
- [ ] Organized screenshots in a clear folder structure
- [ ] Created a comprehensive summary table
- [ ] Included both authentication and messaging phases
- [ ] Verified all code references point to correct files/lines
- [ ] Proofread documentation for clarity and accuracy

---

## Common Issues and Solutions (Mac M4 Specific)

### Issue 1: Emulator won't start or crashes
**Solution:**
```bash
# Check if virtualization is enabled
sysctl kern.hv_support
# Should return: kern.hv_support: 1

# Clear emulator cache
rm -rf ~/.android/avd/SMC_Test_Device.avd/cache/*

# Launch with more verbose logging
emulator -avd SMC_Test_Device -verbose -show-kernel

# If still failing, try creating a new AVD with different API level
```

### Issue 2: ADB not recognizing emulator
**Solution:**
```bash
# Kill and restart ADB server
adb kill-server
adb start-server

# List connected devices
adb devices

# If emulator shows as offline
adb reconnect

# Check PATH includes Android SDK
echo $ANDROID_HOME
export ANDROID_HOME=~/Library/Android/sdk
export PATH=$PATH:$ANDROID_HOME/platform-tools
```

### Issue 3: Certificate installation fails on emulator
**Solution:**
```bash
# Ensure emulator was launched with -writable-system
emulator -list-avds
emulator -avd SMC_Test_Device -writable-system -no-snapshot-load &

# Try manual SELinux permissive mode
adb root
adb shell setenforce 0
adb remount

# Re-push certificate
HASH=$(openssl x509 -inform PEM -subject_hash_old -in ~/Desktop/burp-setup/burp-cert.pem | head -1)
adb push ~/Desktop/burp-setup/${HASH}.0 /system/etc/security/cacerts/
adb shell chmod 644 /system/etc/security/cacerts/${HASH}.0
adb reboot
```

### Issue 4: Burp not intercepting traffic
**Solution:**
```bash
# Check proxy settings in emulator
adb shell settings get global http_proxy

# Manually set proxy
adb shell settings put global http_proxy 10.0.2.2:8080

# Verify Burp is listening
lsof -i :8080

# Check macOS firewall isn't blocking
# System Settings → Network → Firewall → Allow Burp Suite

# Test connectivity
adb shell curl -x 10.0.2.2:8080 http://example.com
```

### Issue 5: Gradle build fails in Android Studio
**Solution:**
```bash
# Clean and rebuild
./gradlew clean
./gradlew assembleDebug --stacktrace

# Check Java version
java -version
# Should be Java 17

# If JDK issues:
export JAVA_HOME=$(/usr/libexec/java_home -v 17)

# Clear Gradle cache
rm -rf ~/.gradle/caches/
```

### Issue 6: SSL pinning still blocking traffic
**Solution:**
```bash
# Use objection for automated bypass
pip3 install objection

# Start objection
objection -g com.example.smc explore

# Inside objection console:
android sslpinning disable

# Or use Frida script
frida -U -f com.example.smc --no-pause -l universal-ssl-pinning-bypass.js
```

### Issue 7: Can't find code location
**Solution:**
```bash
# Use ripgrep for fast searching
brew install ripgrep

# Search for API endpoints
cd ~/Workspaces/hcmut/co3083-applied-cryptography-and-information-coding/smc-client
rg "api/keyexchange" -A 5 -B 5

# Search for network classes
rg "OkHttp|Retrofit|HttpClient" --type java

# Search for JSON field names
rg "publicKey|serverPublicKey" --type java

# Use Android Studio's Find in Path (Cmd+Shift+F)
```

---

## Mac M4 Specific Tips

### Performance Optimization
```bash
# Give emulator more resources
emulator -avd SMC_Test_Device \
  -memory 4096 \
  -cores 4 \
  -gpu auto \
  -writable-system \
  -http-proxy 127.0.0.1:8080
```

### Screenshot Tools for Mac
```bash
# Built-in screenshot
# Cmd+Shift+4 for area selection
# Cmd+Shift+5 for advanced options

# Or use screencapture command
screencapture -i ~/Desktop/burp-screenshots/screenshot-$(date +%Y%m%d-%H%M%S).png
```

### Workflow Automation Script
```bash
# Create a startup script: ~/Desktop/burp-setup/start-testing.sh
#!/bin/bash

# Start Burp Suite
open -a "Burp Suite Community Edition"
sleep 5

# Set environment
export ANDROID_HOME=~/Library/Android/sdk
export PATH=$PATH:$ANDROID_HOME/emulator:$ANDROID_HOME/platform-tools

# Start emulator
emulator -avd SMC_Test_Device \
  -writable-system \
  -http-proxy 127.0.0.1:8080 \
  -memory 4096 &

# Wait for boot
adb wait-for-device
echo "Emulator ready!"

# Set proxy (backup)
adb shell settings put global http_proxy 10.0.2.2:8080

echo "Setup complete. Ready for testing."
```

Make it executable:
```bash
chmod +x ~/Desktop/burp-setup/start-testing.sh
```

---

## Docker Alternative (Advanced)

For a fully containerized approach:

### Using Docker with Android Emulator

```bash
# Pull Android emulator Docker image
docker pull budtmo/docker-android:emulator_12.0

# Run container with Burp proxy
docker run -d \
  --name android-emulator \
  -p 5555:5555 \
  -p 5554:5554 \
  -e EMULATOR_DEVICE="Samsung Galaxy S10" \
  -e WEB_VNC=true \
  -e PROXY_HOST=host.docker.internal \
  -e PROXY_PORT=8080 \
  budtmo/docker-android:emulator_12.0

# Connect to emulator
adb connect localhost:5555

# Access via VNC at http://localhost:6080
```

**Note:** Docker emulator on M4 may have performance limitations. Android Studio's native ARM64 emulator is recommended.

---

## Expected Deliverable Format

Submit a document containing:

1. **Cover Page:**
   - Task name: Task 3.1 - API Interception & Analysis
   - Your name/group
   - Date
   - Environment: Mac M4, Android Studio, Burp Suite

2. **Table of Contents**

3. **Introduction:**
   - Testing environment: Mac M4, ARM64 emulator
   - Tools used: Burp Suite version, Android Studio version
   - Setup summary: emulator config, proxy setup

4. **API Documentation:**
   - For each API call (organized by phase):
     - Screenshots (Burp request + response)
     - Field-by-field explanation
     - Code location mapping

5. **Summary Table:**
   - Complete list of all intercepted APIs

6. **Source Code Analysis:**
   - How requests are constructed in code
   - How responses are processed
   - Key exchange and crypto operations

7. **Appendix:**
   - Burp configuration details
   - Emulator specifications
   - Commands used
   - Challenges encountered and solutions

---

## Time Estimate (Mac M4)

- Install Android Studio and setup: 1 hour
- Install Burp Suite: 15 minutes
- Create and configure emulator: 30 minutes
- Install certificates and test proxy: 45 minutes
- Clone and build SMC client: 30 minutes
- Intercept and document APIs: 2-3 hours
- Map to source code: 2-3 hours
- Create final documentation: 2-3 hours

**Total: 9-12 hours**

---

## Useful Commands Reference

### ADB Commands
```bash
# List devices
adb devices

# Root access
adb root

# Remount system
adb remount

# Install APK
adb install -r app.apk

# Uninstall app
adb uninstall com.example.smc

# View logs
adb logcat | grep "TAG"

# Screenshot
adb exec-out screencap -p > screenshot.png

# List packages
adb shell pm list packages | grep smc
```

### Emulator Commands
```bash
# List AVDs
emulator -list-avds

# Start emulator
emulator -avd SMC_Test_Device

# With options
emulator -avd SMC_Test_Device -writable-system -http-proxy 127.0.0.1:8080

# Kill all emulators
adb emu kill
```

### Gradle Commands
```bash
# Clean build
./gradlew clean

# Build debug APK
./gradlew assembleDebug

# List tasks
./gradlew tasks

# Build with logs
./gradlew assembleDebug --info
```

---

## Resources

### Mac M4 Specific
- Android Studio for Mac ARM64: https://developer.android.com/studio
- Burp Suite for Mac ARM64: https://portswigger.net/burp/releases
- Homebrew: https://brew.sh

### General Resources
- Burp Suite Documentation: https://portswigger.net/burp/documentation
- Android SSL Pinning Bypass: https://github.com/ac-pm/Inspeckage
- Frida SSL Pinning Bypass: https://codeshare.frida.re/@pcipolloni/universal-android-ssl-pinning-bypass-with-frida/
- Android Emulator Networking: https://developer.android.com/studio/run/emulator-networking
- ADB Reference: https://developer.android.com/tools/adb

### Tools
- Objection: https://github.com/sensepost/objection
- Frida: https://frida.re
- APKTool: https://ibotpeaches.github.io/Apktool/
- ripgrep: https://github.com/BurntSushi/ripgrep

---

## Quick Start Checklist

- [ ] Install Homebrew
- [ ] Install Java 17 via Homebrew
- [ ] Download and install Android Studio (ARM64)
- [ ] Download and install Burp Suite (ARM64)
- [ ] Create Android emulator (arm64-v8a)
- [ ] Export Burp certificate
- [ ] Convert certificate to correct format
- [ ] Start emulator with writable system
- [ ] Install certificate as system cert
- [ ] Configure proxy settings
- [ ] Clone SMC client repository
- [ ] Build SMC client in Android Studio
- [ ] Install app on emulator
- [ ] Verify Burp intercepts traffic
- [ ] Begin API interception

---

Good luck with Task 3.1 on your Mac M4!
