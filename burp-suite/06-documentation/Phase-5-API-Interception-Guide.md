# Phase 5: API Interception Guide

## Tình Trạng Hiện Tại

✅ **HOÀN THÀNH**: SSL Certificate Pinning đã được bypass thành công
✅ **HOÀN THÀNH**: App SecureChat có thể login và kết nối với server
✅ **HOÀN THÀNH**: Burp Suite đang capture HTTPS traffic
✅ **HOÀN THÀNH**: Thư mục screenshots đã được tạo

## Bước Tiếp Theo: Chặn Bắt và Phân Tích API

### Task 14: Chặn Bắt Authentication API

#### 14.1 Chuẩn Bị Burp Suite

1. **Mở Burp Suite**
2. **Bật Intercept**: Proxy → Intercept → "Intercept is on"
3. **Xóa History cũ**: Proxy → HTTP history → Right-click → "Clear history"

#### 14.2 Thực Hiện Login và Capture

1. **Trong Android Emulator**:

   - Mở app SecureChat
   - Nhập User ID (theo phân nhóm từ Google Sheet)
   - Nhấn Login

2. **Trong Burp Suite**:

   - Khi request xuất hiện trong Intercept tab
   - **Chụp screenshot**: Request tab (URL, headers, body)
   - Lưu vào: `04-screenshots/burp-screenshots/01-authentication/01-login-request.png`
   - Click **Forward** để gửi request

3. **Capture Response**:
   - Khi response xuất hiện
   - **Chụp screenshot**: Response tab (status, headers, body)
   - Lưu vào: `04-screenshots/burp-screenshots/01-authentication/02-login-response.png`
   - Click **Forward**

#### 14.3 Ghi Chép API Fields

Tạo file `API-Analysis.md` và ghi lại:

**Login Request**:

- Endpoint: (ghi lại URL đầy đủ)
- Method: (GET/POST)
- Headers: (quan trọng: Content-Type, User-Agent)
- Body: (JSON fields và values)

**Login Response**:

- Status Code: (200, 401, etc.)
- Headers: (quan trọng: Set-Cookie, Content-Type)
- Body: (JSON response fields)

### Task 15: Chặn Bắt Key Exchange API

#### 15.1 Trigger Key Exchange

1. **Sau khi login thành công**:

   - Tìm chức năng trong app để bắt đầu key exchange
   - Có thể là: "Start Chat", "Generate Keys", hoặc tự động

2. **Capture Key Exchange Request**:

   - Chụp screenshot request
   - Lưu vào: `04-screenshots/burp-screenshots/02-key-exchange/01-init-request.png`

3. **Capture Key Exchange Response**:
   - Chụp screenshot response
   - Lưu vào: `04-screenshots/burp-screenshots/02-key-exchange/02-init-response.png`

#### 15.2 Phân Tích Key Exchange

Ghi lại trong `API-Analysis.md`:

**Key Exchange Request Fields**:

- `userId`: ID người dùng
- `publicKey`: Public key (base64 encoded)
- `timestamp`: Thời gian request
- `nonce`: Random number

**Key Exchange Response Fields**:

- `serverPublicKey`: Server's public key
- `sessionId`: Session identifier
- `signature`: Digital signature
- `timestamp`: Server timestamp

### Task 16: Chặn Bắt Messaging API

#### 16.1 Gửi Test Messages

1. **Trong app**:

   - Tìm chức năng gửi tin nhắn
   - Gửi 2-3 tin nhắn test ngắn

2. **Capture Send Message Request**:

   - Chụ screenshot request
   - Lưu vào: `04-screenshots/burp-screenshots/03-messaging/01-send-message-request.png`

3. **Capture Message Response**:
   - Chụp screenshot response
   - Lưu vào: `04-screenshots/burp-screenshots/03-messaging/02-send-message-response.png`

#### 16.2 Phân Tích Messaging

Ghi lại trong `API-Analysis.md`:

**Send Message Request Fields**:

- `recipientId`: ID người nhận
- `encryptedMessage`: Tin nhắn đã mã hóa
- `signature`: Chữ ký số
- `timestamp`: Thời gian gửi

**Message Response Fields**:

- `messageId`: ID tin nhắn
- `status`: Trạng thái (sent/delivered)
- `timestamp`: Thời gian server nhận

### Task 17: Lưu Burp Session

#### 17.1 Export HTTP History

1. **Trong Burp Suite**:
   - Proxy → HTTP history
   - Select all requests (Ctrl+A)
   - Right-click → "Save items"
   - Lưu vào: `01-setup/captured-traffic.xml`

### Lưu Ý Quan Trọng

1. **Screenshots phải rõ ràng**: Đảm bảo có thể đọc được URL, headers, và body
2. **Ghi chép đầy đủ**: Mỗi field phải có giải thích mục đích
3. **Phân tích mã hóa**: Chú ý patterns trong encrypted data
4. **Server endpoint**: Tất cả requests đều đến `smc-server-assignment-1000.onrender.com`

### Troubleshooting

**Nếu không thấy requests trong Burp**:

- Kiểm tra Intercept có bật không
- Kiểm tra emulator proxy settings
- Restart emulator với proxy flag

**Nếu app không hoạt động**:

- Kiểm tra logcat: `adb logcat -d | grep -i securechat`
- Reinstall patched APK nếu cần

### Kết Quả Mong Đợi

Sau khi hoàn thành Phase 5, bạn sẽ có:

- Screenshots của tất cả API calls (authentication, key exchange, messaging)
- File phân tích chi tiết các API fields
- Burp session file với toàn bộ traffic
- Hiểu rõ cách app giao tiếp với server

## Bước Tiếp Theo

Sau khi hoàn thành Phase 5, chúng ta sẽ chuyển sang:

- **Phase 6**: Source Code Mapping (ánh xạ API calls với decompiled code)
- **Phase 7**: Documentation (tạo báo cáo hoàn chỉnh)

Hãy bắt đầu với Task 14.1 và thông báo khi bạn đã capture được authentication API!
