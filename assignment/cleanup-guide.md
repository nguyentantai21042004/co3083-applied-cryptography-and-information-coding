# Complete Cleanup Guide - After Assignment Completion

## Overview
This guide helps you completely remove all tools, files, and configurations installed for Task 3.1, leaving only Java (as requested).

**What Will Be Removed:**
- Android Studio and all Android SDKs
- Android Emulators (AVDs)
- Burp Suite
- SMC Client source code and APKs
- All certificates and configuration files
- Homebrew packages (except Java)
- Cache and temporary files

**What Will Be Kept:**
- Java JDK 17 (as requested)
- Your assignment documentation and reports
- Screenshots and deliverables

---

## Table of Contents
1. [Quick Cleanup (Recommended)](#quick-cleanup-recommended)
2. [Detailed Step-by-Step Cleanup](#detailed-step-by-step-cleanup)
3. [Verify Cleanup](#verify-cleanup)
4. [Reclaim Disk Space](#reclaim-disk-space)
5. [Backup Important Files First](#backup-important-files-first)

---

## Backup Important Files First

### Before You Start Cleaning
**IMPORTANT:** Save your work before deleting anything!

```bash
# Create a backup directory
mkdir -p ~/Desktop/smc-assignment-backup

# Copy your documentation
cp ~/Workspaces/hcmut/co3083-applied-cryptography-and-information-coding/assignment/*.md \
   ~/Desktop/smc-assignment-backup/

# Copy your screenshots (if any)
cp -r ~/Desktop/burp-screenshots ~/Desktop/smc-assignment-backup/ 2>/dev/null || true

# Copy Burp saved sessions (if any)
cp -r ~/Desktop/burp-setup/*.burp ~/Desktop/smc-assignment-backup/ 2>/dev/null || true

# Copy your final report
cp -r ~/Documents/Task-3.1-Report* ~/Desktop/smc-assignment-backup/ 2>/dev/null || true

echo "Backup completed at ~/Desktop/smc-assignment-backup"
```

---

## Quick Cleanup (Recommended)

### One-Command Cleanup Script

Create and run this automated cleanup script:

```bash
# Create the cleanup script
cat > ~/Desktop/cleanup-smc-assignment.sh << 'EOF'
#!/bin/bash

echo "======================================"
echo "SMC Assignment Cleanup Script"
echo "======================================"
echo ""
echo "This will remove:"
echo "- Android Studio"
echo "- Android SDK and Emulators"
echo "- Burp Suite"
echo "- SMC Client code"
echo "- All related files and configs"
echo ""
echo "Java will be KEPT as requested."
echo ""
read -p "Continue? (y/N): " -n 1 -r
echo
if [[ ! $REPLY =~ ^[Yy]$ ]]; then
    echo "Cleanup cancelled."
    exit 1
fi

echo ""
echo "Starting cleanup..."
echo ""

# 1. Remove Android Studio
echo "[1/10] Removing Android Studio..."
rm -rf /Applications/Android\ Studio.app
brew uninstall --cask android-studio 2>/dev/null || true

# 2. Remove Android SDK
echo "[2/10] Removing Android SDK..."
rm -rf ~/Library/Android

# 3. Remove Android Emulator data
echo "[3/10] Removing Android Emulator data..."
rm -rf ~/.android

# 4. Remove Burp Suite
echo "[4/10] Removing Burp Suite..."
rm -rf /Applications/Burp\ Suite\ Community\ Edition.app
rm -rf ~/Library/Application\ Support/BurpSuite

# 5. Remove SMC Client source code
echo "[5/10] Removing SMC Client..."
rm -rf ~/Workspaces/hcmut/co3083-applied-cryptography-and-information-coding/smc-client

# 6. Remove Burp setup files
echo "[6/10] Removing Burp certificates and setup files..."
rm -rf ~/Desktop/burp-setup
rm -rf ~/Desktop/burp-screenshots

# 7. Remove Gradle cache
echo "[7/10] Removing Gradle cache..."
rm -rf ~/.gradle

# 8. Remove Homebrew packages (except Java)
echo "[8/10] Removing Homebrew packages..."
brew uninstall apktool 2>/dev/null || true
brew uninstall ripgrep 2>/dev/null || true

# 9. Remove pip packages (Frida, Objection)
echo "[9/10] Removing Python packages..."
pip3 uninstall -y frida-tools objection 2>/dev/null || true

# 10. Clean up environment variables
echo "[10/10] Cleaning environment variables..."
# Remove Android environment variables from shell configs
sed -i.backup '/ANDROID_HOME/d' ~/.zshrc 2>/dev/null || true
sed -i.backup '/ANDROID_SDK/d' ~/.zshrc 2>/dev/null || true
sed -i.backup '/Android\/sdk/d' ~/.zshrc 2>/dev/null || true
sed -i.backup '/platform-tools/d' ~/.zshrc 2>/dev/null || true

# Also clean .bash_profile if exists
sed -i.backup '/ANDROID_HOME/d' ~/.bash_profile 2>/dev/null || true
sed -i.backup '/ANDROID_SDK/d' ~/.bash_profile 2>/dev/null || true
sed -i.backup '/Android\/sdk/d' ~/.bash_profile 2>/dev/null || true
sed -i.backup '/platform-tools/d' ~/.bash_profile 2>/dev/null || true

echo ""
echo "======================================"
echo "Cleanup Complete!"
echo "======================================"
echo ""
echo "Removed:"
echo "  ✓ Android Studio"
echo "  ✓ Android SDK (~10-20 GB)"
echo "  ✓ Android Emulators"
echo "  ✓ Burp Suite"
echo "  ✓ SMC Client code"
echo "  ✓ Related configurations"
echo ""
echo "Kept:"
echo "  ✓ Java JDK 17"
echo "  ✓ Assignment documentation"
echo "  ✓ Backup at ~/Desktop/smc-assignment-backup"
echo ""
echo "To reclaim more space, run:"
echo "  brew cleanup"
echo "  rm -rf ~/.Trash/*"
echo ""
echo "Restart your terminal for environment changes to take effect."
EOF

# Make it executable
chmod +x ~/Desktop/cleanup-smc-assignment.sh

# Run the cleanup script
~/Desktop/cleanup-smc-assignment.sh
```

---

## Detailed Step-by-Step Cleanup

If you prefer to clean up manually or want to understand each step:

### Step 1: Remove Android Studio

```bash
# Remove the application
rm -rf /Applications/Android\ Studio.app

# If installed via Homebrew
brew uninstall --cask android-studio

# Verify removal
ls /Applications/ | grep -i android
# Should return nothing
```

**What This Removes:**
- Android Studio IDE (~1 GB)
- Built-in SDK manager
- IDE plugins and settings

**Disk Space Freed:** ~1 GB

---

### Step 2: Remove Android SDK

```bash
# Remove entire Android SDK directory
rm -rf ~/Library/Android

# This includes:
# - SDK Platform tools
# - Build tools
# - Platform APIs (API 29, 30, 31, 33, etc.)
# - System images for emulators
# - NDK (if installed)
```

**What This Removes:**
- All Android SDK platforms (~5-15 GB)
- Build tools
- Platform tools (adb, fastboot)
- Android emulator binaries
- System images

**Disk Space Freed:** ~10-20 GB

---

### Step 3: Remove Android Virtual Devices (AVDs)

```bash
# Remove all emulator data
rm -rf ~/.android

# This includes:
# - AVD configurations
# - Emulator cache
# - Debug certificates
# - adb keys
```

**What This Removes:**
- All created AVDs (SMC_Test_Device, etc.)
- Emulator snapshots
- Virtual SD card images
- Debug certificates

**Disk Space Freed:** ~5-10 GB (depending on how many AVDs you created)

---

### Step 4: Remove Burp Suite

```bash
# Remove Burp Suite application
rm -rf /Applications/Burp\ Suite\ Community\ Edition.app

# Remove Burp Suite data
rm -rf ~/Library/Application\ Support/BurpSuite

# Remove Burp Suite preferences
rm -rf ~/Library/Preferences/com.install4j.* 2>/dev/null

# Remove saved projects (if any)
rm -rf ~/Documents/Burp* 2>/dev/null
```

**What This Removes:**
- Burp Suite application (~200 MB)
- Saved projects and configurations
- Proxy history
- Extensions and plugins

**Disk Space Freed:** ~200-500 MB

---

### Step 5: Remove Burp Certificates and Setup Files

```bash
# Remove burp setup directory
rm -rf ~/Desktop/burp-setup

# This includes:
# - burp-cert.der
# - burp-cert.pem
# - [hash].0 certificate files
# - startup scripts
```

**What This Removes:**
- Exported Burp CA certificates
- Certificate conversion files
- Any setup scripts you created

**Disk Space Freed:** ~10 KB

---

### Step 6: Remove SMC Client Source Code

```bash
# Remove cloned repository
rm -rf ~/Workspaces/hcmut/co3083-applied-cryptography-and-information-coding/smc-client

# Remove downloaded APKs (if any)
find ~/Downloads -name "*.apk" -type f -delete
```

**What This Removes:**
- SMC client source code
- Built APKs
- Gradle build cache
- Git history

**Disk Space Freed:** ~100-500 MB

---

### Step 7: Remove Gradle Cache

```bash
# Remove Gradle global cache
rm -rf ~/.gradle

# This includes:
# - Downloaded dependencies
# - Build cache
# - Wrapper distributions
```

**What This Removes:**
- Gradle build cache
- Downloaded Android libraries
- Gradle wrapper files

**Disk Space Freed:** ~1-5 GB

---

### Step 8: Remove Additional Tools

```bash
# Remove apktool (if installed)
brew uninstall apktool

# Remove ripgrep (if you don't use it otherwise)
brew uninstall ripgrep

# Remove Python packages for Android testing
pip3 uninstall -y frida-tools
pip3 uninstall -y objection

# Remove Node.js packages (if you installed any for testing)
npm uninstall -g appium 2>/dev/null || true
```

**What This Removes:**
- APK analysis tools
- SSL pinning bypass tools
- Mobile automation tools

**Disk Space Freed:** ~100-500 MB

---

### Step 9: Clean Environment Variables

```bash
# Check current environment variables
echo "Current Android-related variables:"
env | grep -i android

# Remove from .zshrc (Mac default shell)
nano ~/.zshrc
# Delete these lines (if present):
# export ANDROID_HOME=~/Library/Android/sdk
# export PATH=$PATH:$ANDROID_HOME/emulator
# export PATH=$PATH:$ANDROID_HOME/platform-tools

# Or use sed to remove automatically
sed -i.backup '/ANDROID_HOME/d' ~/.zshrc
sed -i.backup '/ANDROID_SDK/d' ~/.zshrc
sed -i.backup '/Android\/sdk/d' ~/.zshrc
sed -i.backup '/platform-tools/d' ~/.zshrc
sed -i.backup '/emulator/d' ~/.zshrc

# If you use bash instead
sed -i.backup '/ANDROID_HOME/d' ~/.bash_profile
sed -i.backup '/ANDROID_SDK/d' ~/.bash_profile

# Reload shell configuration
source ~/.zshrc
```

**What This Removes:**
- ANDROID_HOME variable
- Android SDK paths from PATH
- Emulator paths

---

### Step 10: Remove Screenshot and Working Directories

```bash
# Remove screenshot directory (if created)
rm -rf ~/Desktop/burp-screenshots

# Remove any working directories
rm -rf ~/Desktop/smc-testing

# Clean Downloads folder of APKs
find ~/Downloads -name "*.apk" -delete
find ~/Downloads -name "*burp*" -type f -delete
```

**What This Removes:**
- Screenshots taken during testing
- Temporary working directories
- Downloaded APK files

**Disk Space Freed:** ~100 MB - 1 GB

---

## Verify Cleanup

### Check What's Been Removed

```bash
# Create verification script
cat > ~/Desktop/verify-cleanup.sh << 'EOF'
#!/bin/bash

echo "Verification Report"
echo "==================="
echo ""

# Check Android Studio
if [ -d "/Applications/Android Studio.app" ]; then
    echo "❌ Android Studio: Still installed"
else
    echo "✅ Android Studio: Removed"
fi

# Check Android SDK
if [ -d ~/Library/Android ]; then
    echo "❌ Android SDK: Still present"
    du -sh ~/Library/Android
else
    echo "✅ Android SDK: Removed"
fi

# Check AVDs
if [ -d ~/.android ]; then
    echo "❌ Android AVDs: Still present"
    du -sh ~/.android
else
    echo "✅ Android AVDs: Removed"
fi

# Check Burp Suite
if [ -d "/Applications/Burp Suite Community Edition.app" ]; then
    echo "❌ Burp Suite: Still installed"
else
    echo "✅ Burp Suite: Removed"
fi

# Check SMC Client
if [ -d ~/Workspaces/hcmut/co3083-applied-cryptography-and-information-coding/smc-client ]; then
    echo "❌ SMC Client: Still present"
else
    echo "✅ SMC Client: Removed"
fi

# Check Gradle
if [ -d ~/.gradle ]; then
    echo "❌ Gradle cache: Still present"
    du -sh ~/.gradle
else
    echo "✅ Gradle cache: Removed"
fi

# Check Java (should still be installed)
if command -v java &> /dev/null; then
    echo "✅ Java: Still installed (as requested)"
    java -version 2>&1 | head -1
else
    echo "❌ Java: Removed (this might be a problem)"
fi

# Check environment variables
echo ""
echo "Environment Variables:"
if env | grep -i android > /dev/null; then
    echo "❌ Android variables still present:"
    env | grep -i android
else
    echo "✅ Android variables: Removed"
fi

echo ""
echo "==================="
EOF

chmod +x ~/Desktop/verify-cleanup.sh
~/Desktop/verify-cleanup.sh
```

---

## Reclaim Disk Space

### Additional Cleanup Steps

```bash
# 1. Clean Homebrew cache
brew cleanup -s
brew autoremove

# 2. Empty Trash
rm -rf ~/.Trash/*

# 3. Clear system caches (be careful!)
# These will regenerate automatically
sudo rm -rf /Library/Caches/*
rm -rf ~/Library/Caches/*

# 4. Clean pip cache
pip3 cache purge

# 5. Clear system logs
sudo rm -rf /var/log/*

# 6. Remove old shell backups
rm -f ~/.zshrc.backup*
rm -f ~/.bash_profile.backup*
```

### Check Disk Space Freed

```bash
# Before cleanup (if you noted it)
# After cleanup - check available space
df -h ~

# Detailed disk usage
du -sh ~/Library/Android 2>/dev/null || echo "Android SDK: removed"
du -sh ~/.android 2>/dev/null || echo "AVDs: removed"
du -sh ~/.gradle 2>/dev/null || echo "Gradle: removed"
```

**Expected Disk Space Freed:** 15-35 GB

---

## What to Keep (Java Only)

### Verify Java is Still Installed

```bash
# Check Java installation
java -version

# Should show something like:
# openjdk version "17.0.x" 2024-xx-xx
# OpenJDK Runtime Environment (build ...)
# OpenJDK 64-Bit Server VM (build ...)

# Check Java location
which java
# Should show: /opt/homebrew/bin/java or similar

# Check JAVA_HOME (if set)
echo $JAVA_HOME
# Should show path to JDK 17
```

### Keep Java Configuration

Your `~/.zshrc` should still have (if needed):
```bash
export JAVA_HOME=$(/usr/libexec/java_home -v 17)
```

Keep this line if you use Java for other projects.

---

## Final Checklist

### After Cleanup, You Should Have:

**Removed:**
- [x] Android Studio
- [x] Android SDK (~10-20 GB)
- [x] Android Emulators (~5-10 GB)
- [x] Burp Suite
- [x] SMC Client source code
- [x] Gradle cache (~1-5 GB)
- [x] Burp certificates
- [x] Android environment variables
- [x] Additional tools (apktool, frida, etc.)

**Kept:**
- [x] Java JDK 17
- [x] Your assignment documentation (in backup)
- [x] Screenshots and deliverables (in backup)
- [x] Your final report

**Backup Location:**
- [x] `~/Desktop/smc-assignment-backup/`

---

## Restore If Needed

### If You Need to Redo the Assignment

All your important files are backed up at:
```
~/Desktop/smc-assignment-backup/
├── task-3.1-guide.md
├── task-3.1-concepts.md
├── cleanup-guide.md
├── burp-screenshots/
│   ├── 01-authentication/
│   ├── 02-key-exchange/
│   └── 03-messaging/
└── your-report.pdf
```

To reinstall:
1. Follow the original setup guide
2. Reference your screenshots and notes
3. Java is already installed

---

## Troubleshooting Cleanup

### Issue 1: "Permission denied" when deleting
```bash
# Use sudo for system files
sudo rm -rf /path/to/file

# Or change ownership first
sudo chown -R $(whoami) /path/to/file
rm -rf /path/to/file
```

### Issue 2: "Directory not found"
```bash
# Already deleted - this is fine
# The cleanup script handles this with `|| true`
```

### Issue 3: Java was accidentally deleted
```bash
# Reinstall Java
brew install openjdk@17

# Set JAVA_HOME
echo 'export JAVA_HOME=$(/usr/libexec/java_home -v 17)' >> ~/.zshrc
source ~/.zshrc

# Verify
java -version
```

### Issue 4: Still seeing Android files
```bash
# Find remaining Android files
find ~ -name "*android*" -type d 2>/dev/null

# Find remaining AVD files
find ~ -name "*.avd" -type d 2>/dev/null

# Remove manually
rm -rf [found-directory]
```

---

## Complete Reset (Nuclear Option)

### If You Want to Remove EVERYTHING (Including Java)

```bash
# DANGER: This removes Java too!

# Remove all Homebrew packages
brew list | xargs brew uninstall --force

# Remove Homebrew itself
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/uninstall.sh)"

# Clean user directories
rm -rf ~/Library/Android
rm -rf ~/.android
rm -rf ~/.gradle
rm -rf ~/Library/Application\ Support/BurpSuite

# Remove applications
rm -rf /Applications/Android\ Studio.app
rm -rf /Applications/Burp\ Suite\ Community\ Edition.app

echo "Everything removed. You'll need to reinstall Java if needed."
```

---

## Summary

### Quick Commands Reference

```bash
# Full cleanup (keeping Java)
~/Desktop/cleanup-smc-assignment.sh

# Verify cleanup
~/Desktop/verify-cleanup.sh

# Check disk space freed
df -h ~

# List what's left
du -sh ~/Library/Android ~/.android ~/.gradle 2>/dev/null

# Reinstall Java (if accidentally deleted)
brew install openjdk@17
```

### Expected Results

| Item | Before | After | Space Freed |
|------|--------|-------|-------------|
| Android Studio | 1 GB | 0 | 1 GB |
| Android SDK | 10-20 GB | 0 | 10-20 GB |
| AVDs | 5-10 GB | 0 | 5-10 GB |
| Gradle Cache | 1-5 GB | 0 | 1-5 GB |
| Burp Suite | 500 MB | 0 | 500 MB |
| SMC Client | 200 MB | 0 | 200 MB |
| **Total** | **~20-40 GB** | **0** | **~20-40 GB** |
| Java | 300 MB | **300 MB** | **Kept** |

---

## Post-Cleanup

### After Running Cleanup

1. **Restart Terminal**
   ```bash
   # Open new terminal window
   # Or reload config
   source ~/.zshrc
   ```

2. **Verify Java Still Works**
   ```bash
   java -version
   javac -version
   ```

3. **Check Backup**
   ```bash
   ls ~/Desktop/smc-assignment-backup/
   ```

4. **Remove Cleanup Scripts (Optional)**
   ```bash
   rm ~/Desktop/cleanup-smc-assignment.sh
   rm ~/Desktop/verify-cleanup.sh
   ```

5. **Submit Assignment**
   - Upload your final report
   - Submit screenshots
   - Keep backup until grades are posted

6. **Final Cleanup (After Grades)**
   ```bash
   # Delete backup after you get your grade
   rm -rf ~/Desktop/smc-assignment-backup/
   ```

---

**You're done! Your Mac is clean, with only Java remaining.**

**Disk space freed: ~20-40 GB**

**Time to cleanup: ~5 minutes**
