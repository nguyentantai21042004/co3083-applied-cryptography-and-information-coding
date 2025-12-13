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

- **Endpoint**: POST /message/send?userId=group-2
- **Method**: POST
- **Headers**:

  ```
  X-User-Id: group-2
  Content-Type: application/json; charset=utf-8
  User-Agent: okhttp/4.11.0
  ```

- **Body**:

  ```json
  {
    "sessionToken": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
    "encryptedMessage": "3xHDVhZj5VpLQ4YWJK/3Tkqphg7N9oyC2qcOkovQd4k6tv7ISkvUrVnR4VaJHwM=",
    "messageSignature": {
      "r": "30016840686920661131186144815592580206549297350527278483086679515447399036715",
      "s": "25805279053609117703494590460645853309696778084063326097019163091287280930530",
      "messageHash": "71956769915691024860944709399764371723537091875395554301528540153151891683530",
      "algorithm": "ECDSA-P256"
    }
  }
  ```

### Response

- **Status Code**: 200 OK
- **Headers**:

  ```
  Content-Type: application/json
  Access-Control-Allow-Origin: *
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

## Data Files

### JSON Data (Structured)

1. **Session Create**: `04-screenshots/api-data/01-authentication/01-session-create-request.json` & `01-session-create-response.json`
2. **Session Exchange**: `04-screenshots/api-data/02-key-exchange/02-session-exchange-request.json` & `02-session-exchange-response.json`
3. **Message Send**: `04-screenshots/api-data/03-messaging/03-message-send-request.json` & `03-message-send-response.json`

### Screenshots (Burp Suite)

1. **Session Create**: `04-screenshots/burp-screenshots/01-authentication/01-session-create-burp-capture.png`
2. **Session Exchange**: `04-screenshots/burp-screenshots/02-key-exchange/02-session-exchange-burp-capture.png`
3. **Message Send**: `04-screenshots/burp-screenshots/03-messaging/03-message-send-burp-capture.png`

### Summary

- **API Summary**: `04-screenshots/api-data/API-Summary.md`
- **Complete Analysis**: This file (`05-analysis/API-Analysis.md`)
