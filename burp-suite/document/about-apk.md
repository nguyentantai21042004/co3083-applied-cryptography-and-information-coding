# About assignment.apk - What Is It and How to Use It

## What is `assignment.apk`?

### Quick Answer

`assignment.apk` (note the typo: "assigment") is the **pre-built Android application package** for the SMC (Secure Messaging Component) client that you need to test for Task 3.1.

### Location

```
/Users/tantai/Workspaces/hcmut/co3083-applied-cryptography-and-information-coding/burp-suite/assigment.apk
```

File size: ~7.3 MB

---

## What is an APK File?

### Definition

**APK** stands for **Android Package Kit** - it's the file format used to distribute and install applications on Android devices.

Think of it like:

- `.dmg` or `.app` on Mac
- `.exe` on Windows
- `.deb` on Linux

### What's Inside an APK?

An APK contains:

```
assignment.apk
├── AndroidManifest.xml     # App configuration and permissions
├── classes.dex             # Compiled Java/Kotlin code
├── resources.arsc          # Compiled resources
├── res/                    # Images, layouts, strings
│   ├── drawable/
│   ├── layout/
│   └── values/
├── lib/                    # Native libraries (ARM, x86)
│   └── arm64-v8a/         # ARM64 libraries (for M4 emulator)
├── assets/                 # Additional files
└── META-INF/              # Signing information
    ├── CERT.RSA
    ├── CERT.SF
    └── MANIFEST.MF
```

---

## Two Ways to Get the SMC App

You have **two options** to get the SMC application:

### Option 1: Use the Pre-built APK (Faster) ⭐ Recommended for Quick Start

**File:** `assignment.apk` (the file you have)

**Pros:**

- ✅ Ready to use immediately
- ✅ No build process needed
- ✅ No Gradle/Android Studio setup required initially
- ✅ Quick testing

**Cons:**

- ❌ Can't see source code directly
- ❌ Harder to map API calls to code locations
- ❌ Can't modify the app easily
- ❌ Need to decompile to understand implementation

**Use Case:**

- Quick initial testing
- Just want to intercept traffic
- Time-constrained

---

### Option 2: Clone and Build from Source (Better for Assignment) ⭐ Recommended for Complete Task

**Source:** GitHub repository

**Pros:**

- ✅ Full access to source code
- ✅ Can map API calls to exact code locations (required for Task 3.1)
- ✅ Understand crypto implementation (needed for Tasks 3.2 & 3.3)
- ✅ Can modify if needed (disable cert pinning, debug)
- ✅ Learn how the app works

**Cons:**

- ❌ Requires Android Studio setup
- ❌ Build time (~5-10 minutes first time)
- ❌ Larger download (~500 MB with dependencies)

**Use Case:**

- Complete assignment properly
- Need to document code locations
- Want to understand the implementation
- Required for full marks

---

## How to Use `assignment.apk`

### Method 1: Install Directly on Emulator (Quick Test)

```bash
# 1. Start your emulator (from Android Studio or command line)
emulator -avd SMC_Test_Device -writable-system &

# 2. Wait for emulator to boot
adb wait-for-device

# 3. Install the APK
adb install -r /Users/tantai/Workspaces/hcmut/co3083-applied-cryptography-and-information-coding/burp-suite/assigment.apk

# 4. Verify installation
adb shell pm list packages | grep -i smc
# Should show the package name (e.g., com.example.smc)

# 5. Launch the app
# Open from emulator's app drawer or:
adb shell monkey -p com.example.smc -c android.intent.category.LAUNCHER 1
```

### Method 2: Use with Android Studio

```bash
# 1. Open Android Studio
# 2. Tools → Device Manager
# 3. Start your emulator
# 4. Simply drag and drop the APK file onto the emulator window
# 5. The app will be installed automatically
```

---

## Recommended Workflow for Task 3.1

### Best Approach: Use Both!

```
Phase 1: Quick Start with APK (Day 1)
├── Install assignment.apk on emulator
├── Set up Burp Suite interception
├── Capture initial API traffic
├── Get familiar with the app flow
└── Take preliminary screenshots

Phase 2: Deep Analysis with Source Code (Day 2-3)
├── Clone the GitHub repository
├── Build from source in Android Studio
├── Map intercepted APIs to source code
├── Understand crypto implementation
├── Document code locations (required!)
└── Complete full analysis
```

**Why this approach?**

1. APK lets you start testing immediately
2. Source code gives you the details needed for documentation
3. You need both to complete Task 3.1 properly

---

## The Problem: APK Alone is Not Enough for Task 3.1

### What Task 3.1 Requires:

From the assignment document:

> **Deliverables:** Documentation containing: Burp screenshots, a table listing each API endpoint, request/response fields, and **mapping to code locations**.

### What You Can Do with APK Only:

- ✅ Intercept API calls
- ✅ Take Burp screenshots
- ✅ Document request/response fields
- ❌ **Can't easily map to code locations** (major requirement!)

### What You Can Do with Source Code:

- ✅ Everything above, plus:
- ✅ Find exact Java/Kotlin files
- ✅ Identify methods that make API calls
- ✅ Understand request construction
- ✅ See crypto implementation
- ✅ Map to line numbers

**Example of Required Mapping:**

```
API: POST /api/keyexchange/init

With APK only:
  - You can intercept the request
  - You see the data
  - But you DON'T know where in code this comes from ❌

With Source Code:
  - File: app/src/main/java/com/example/smc/network/KeyExchangeService.java
  - Method: initiateKeyExchange()
  - Lines: 45-67 ✅
```

---

## How to Get the Source Code

### Clone from GitHub

```bash
# Navigate to your workspace
cd /Users/tantai/Workspaces/hcmut/co3083-applied-cryptography-and-information-coding

# Clone the repository
git clone https://github.com/dangduongminhnhat/Client-Assignment-Advance-Cryptography-and-Coding-Theory.git smc-client

# Check what you got
cd smc-client
ls -la

# Expected structure:
# smc-client/
# ├── app/
# │   └── src/
# │       └── main/
# │           ├── java/          # Source code here!
# │           └── res/
# ├── gradle/
# ├── build.gradle
# └── settings.gradle
```

---

## Analyzing the APK (Advanced - Optional)

If you're curious about what's inside the APK, you can decompile it:

### Using apktool (Disassemble)

```bash
# Install apktool
brew install apktool

# Decompile the APK
cd /Users/tantai/Workspaces/hcmut/co3083-applied-cryptography-and-information-coding/burp-suite
apktool d assigment.apk -o smc-decompiled

# Explore the decompiled code
cd smc-decompiled
ls -la

# You'll see:
# - AndroidManifest.xml (readable now)
# - smali/ (disassembled bytecode)
# - res/ (resources)
```

### Using jadx (Decompile to Java)

```bash
# Install jadx (Java decompiler)
brew install jadx

# Decompile APK to Java
jadx assigment.apk -d smc-java

# Open in file browser
open smc-java

# Navigate to sources to see Java code
# Note: This is reconstructed from bytecode, not original source
```

**Note:** Decompiled code is harder to read than original source. It's better to use the GitHub repository.

---

## Quick Comparison

| Aspect                       | Pre-built APK | Source Code from GitHub |
| ---------------------------- | ------------- | ----------------------- |
| **Installation Time**        | Immediate     | 10-15 minutes           |
| **Size**                     | 7.3 MB        | ~500 MB (with deps)     |
| **Can Run App?**             | ✅ Yes        | ✅ Yes (after build)    |
| **Can Intercept Traffic?**   | ✅ Yes        | ✅ Yes                  |
| **Can Map to Code?**         | ❌ Hard       | ✅ Easy                 |
| **Can Modify App?**          | ❌ No         | ✅ Yes                  |
| **Sufficient for Task 3.1?** | ❌ **No**     | ✅ **Yes**              |
| **Sufficient for Task 3.2?** | ❌ **No**     | ✅ **Yes**              |
| **Sufficient for Task 3.3?** | ❌ **No**     | ✅ **Yes**              |

---

## My Recommendation

### Step-by-Step Plan

**Day 1 - Quick Start (2-3 hours)**

```bash
# Use the APK for initial exploration
1. Install assignment.apk on emulator
2. Set up Burp Suite
3. Install Burp certificate
4. Configure proxy
5. Test basic interception
6. Get familiar with app features
```

**Day 2 - Setup Source Code (2-3 hours)**

```bash
# Get the proper source code
1. Clone GitHub repository
2. Open in Android Studio
3. Build the project
4. Install on emulator
5. Verify it works the same as APK
```

**Day 3-4 - Complete Analysis (4-6 hours)**

```bash
# Do the actual assignment
1. Intercept all API calls (use either APK or built app)
2. Take Burp screenshots
3. Document request/response fields
4. Map each API to source code (need source!)
5. Create final documentation
```

---

## Common Questions

### Q1: Can I complete the assignment with just the APK?

**A:** No. You need source code to map API calls to code locations, which is a required deliverable.

### Q2: Do I need to build from source if I have the APK?

**A:** Yes, for a complete assignment. You need source code access for documentation.

### Q3: Is the APK the same as building from source?

**A:** It should be functionally identical, but you won't have access to:

- Original source code
- Comments in code
- Clear file/method names
- Easy code navigation

### Q4: Can I use the APK for testing and source for analysis?

**A:** Yes! This is actually a good approach:

- Install APK quickly → Test and intercept
- Use source code → Analyze and map to code locations

### Q5: Which should I use first?

**A:** Start with APK for quick testing, then set up source code for proper analysis.

---

## File Information

### About Your APK

```bash
# Check APK details
aapt dump badging /path/to/assigment.apk

# Check package name
aapt dump badging assigment.apk | grep package

# Check permissions
aapt dump permissions assigment.apk

# Check app version
aapt dump badging assigment.apk | grep version
```

Note: `aapt` comes with Android SDK

---

## Summary

### What `assignment.apk` Is:

- ✅ The pre-built SMC client application
- ✅ Ready to install and test immediately
- ✅ Useful for quick exploration
- ✅ Good for initial traffic interception

### What `assignment.apk` Is NOT:

- ❌ A replacement for source code
- ❌ Sufficient alone for completing the assignment
- ❌ Easy to analyze without decompiling
- ❌ Modifiable without advanced tools

### What You Should Do:

1. ✅ Use `assignment.apk` for **quick initial testing**
2. ✅ Clone source code from GitHub for **proper analysis**
3. ✅ Use both together for **efficient workflow**
4. ✅ Complete assignment with **source code access**

---

## Next Steps

```bash
# Quick start with APK (today)
adb install -r /Users/tantai/Workspaces/hcmut/co3083-applied-cryptography-and-information-coding/burp-suite/assigment.apk

# Setup source code (also today or tomorrow)
cd /Users/tantai/Workspaces/hcmut/co3083-applied-cryptography-and-information-coding
git clone https://github.com/dangduongminhnhat/Client-Assignment-Advance-Cryptography-and-Coding-Theory.git smc-client
cd smc-client
```

Then follow the guide at:

- Technical guide: `assignment/task-3.1-guide.md`
- Conceptual guide: `assignment/task-3.1-concepts.md`

Good luck! 🚀
