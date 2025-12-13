# Phase 6: Source Code Mapping - Detailed Guide

## 🎯 **Mục tiêu**: Tìm code tương ứng với 3 API calls đã capture

## ✅ **Đã hoàn thành:**

- **Session Create API**: Found in `LoginActivity.smali` line 550

## 🔍 **Tiếp theo cần tìm:**

### **1. Session Exchange API**

**Search keywords (theo thứ tự ưu tiên):**

```
/session/exchange
session/exchange
ecdh_2
curveParameters
clientPublicKey
serverPublicKey
```

**Search settings:**

- **files to exclude**: `res/**, build/**, original/**`
- **Scope**: Chỉ trong smali directories

### **2. Message Send API**

**Search keywords (theo thứ tự ưu tiên):**

```
/message/send
message/send
encryptedMessage
messageSignature
encryptedResponse
what is your name
SecureBot
```

### **3. Crypto Implementation**

**Search keywords:**

```
ecdh_2
ECDSA-P256
Cipher
KeyGenerator
PublicKey
PrivateKey
```

## 📸 **Screenshots - CẦN LÀM:**

### **Tạo thư mục:**

```bash
mkdir -p 04-screenshots/code-mapping
```

### **Chụp screenshots cho mỗi API tìm được:**

1. **Search results** showing code location
2. **Actual code** với line numbers visible
3. **Save với tên:**
   - `01-session-create-code-location.png` ✅ (Done)
   - `02-session-exchange-code-location.png`
   - `03-message-send-code-location.png`

### **QUAN TRỌNG:**

- ❌ **KHÔNG cần paste ảnh vào đâu**
- ✅ **CHỈ cần save files** vào thư mục
- ✅ **Tên file phải đúng convention**

## 📝 **Ghi chép kết quả:**

**Mỗi khi tìm được API, ghi vào `05-analysis/Code-API-Mapping.md`:**

- File path
- Line number
- Code snippet
- Method context
- Purpose

## 🎯 **Action Items cho bạn:**

### **Bước 1**: Tìm Session Exchange

```
Search: /session/exchange
files to exclude: res/**, build/**, original/**
```

### **Bước 2**: Tìm Message Send

```
Search: /message/send
files to exclude: res/**, build/**, original/**
```

### **Bước 3**: Nếu không tìm thấy exact matches

- Thử keywords khác trong list
- Search trong LoginActivity.smali manually
- Có thể tất cả APIs đều trong LoginActivity

### **Bước 4**: Chụp screenshots

- Tạo folder: `04-screenshots/code-mapping/`
- Save screenshots với naming convention
- **KHÔNG paste vào đâu cả**

## 🤔 **Nếu không tìm thấy:**

**Có thể tất cả APIs đều trong LoginActivity.smali**

- Mở file `LoginActivity.smali` manually
- Scroll qua các methods
- Tìm các string constants khác
- Look for HTTP request building code

**Hoặc search broader:**

- `session` (filter results)
- `message` (filter results)
- `POST` (filter results)

## ✅ **Kết quả mong đợi:**

Sau Phase 6, bạn sẽ có:

- Code locations cho tất cả 3 APIs
- Screenshots của code
- Complete mapping table
- Ready cho Phase 7 (Documentation)

---

**Bắt đầu với search `/session/exchange` nhé!** 🚀
