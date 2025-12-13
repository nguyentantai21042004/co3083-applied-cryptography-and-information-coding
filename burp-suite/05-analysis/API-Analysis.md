# SMC API Analysis Report

## Thông Tin Chung

- **App**: SecureChat (SMC)
- **Package**: com.example.securechat
- **Server**: smc-server-assignment-1000.onrender.com
- **Ngày phân tích**: 13/12/2025
- **Tools**: Burp Suite Community Edition, Android Emulator

## 1. Authentication API

### Request

- **Endpoint**:
- **Method**:
- **Headers**:

  ```

  ```

- **Body**:

  ```json

  ```

### Response

- **Status Code**:
- **Headers**:

  ```

  ```

- **Body**:

  ```json

  ```

### Field Analysis

| Field | Type | Purpose | Notes |
| ----- | ---- | ------- | ----- |
|       |      |         |       |

---

## 2. Key Exchange API

### Request

- **Endpoint**:
- **Method**:
- **Headers**:

  ```

  ```

- **Body**:

  ```json

  ```

### Response

- **Status Code**:
- **Headers**:

  ```

  ```

- **Body**:

  ```json

  ```

### Field Analysis

| Field | Type | Purpose | Notes |
| ----- | ---- | ------- | ----- |
|       |      |         |       |

---

## 3. Messaging API

### Request

- **Endpoint**:
- **Method**:
- **Headers**:

  ```

  ```

- **Body**:

  ```json

  ```

### Response

- **Status Code**:
- **Headers**:

  ```

  ```

- **Body**:

  ```json

  ```

### Field Analysis

| Field | Type | Purpose | Notes |
| ----- | ---- | ------- | ----- |
|       |      |         |       |

---

## 4. Security Analysis

### Encryption Patterns

- **Key Exchange**:
- **Message Encryption**:
- **Signature Verification**:

### Observations

-
-
- ***

## 5. Code Mapping

### Authentication

- **File**:
- **Method**:
- **Line**:

### Key Exchange

- **File**:
- **Method**:
- **Line**:

### Messaging

- **File**:
- **Method**:
- **Line**:

---

## Screenshots

1. Authentication Request: `04-screenshots/burp-screenshots/01-authentication/01-login-request.png`
2. Authentication Response: `04-screenshots/burp-screenshots/01-authentication/02-login-response.png`
3. Key Exchange Request: `04-screenshots/burp-screenshots/02-key-exchange/01-init-request.png`
4. Key Exchange Response: `04-screenshots/burp-screenshots/02-key-exchange/02-init-response.png`
5. Message Request: `04-screenshots/burp-screenshots/03-messaging/01-send-message-request.png`
6. Message Response: `04-screenshots/burp-screenshots/03-messaging/02-send-message-response.png`
