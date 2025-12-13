# SMC API Capture Summary

## Overview

This document summarizes all captured API calls from the SecureChat (SMC) application during the security analysis.

## API Endpoints Captured

### 1. Authentication & Key Exchange Phase

#### 1.1 Session Create

- **File**: `01-authentication/01-session-create-request.json` & `01-session-create-response.json`
- **Endpoint**: `POST /session/create?userId=group-2`
- **Purpose**: Initialize ECDH key exchange with curve parameters
- **Key Features**:
  - Client sends ECDH_2 curve parameters
  - Server responds with server public key + session token
  - Digital signatures for authentication

#### 1.2 Session Exchange

- **File**: `02-key-exchange/02-session-exchange-request.json` & `02-session-exchange-response.json`
- **Endpoint**: `POST /session/exchange?userId=group-2`
- **Purpose**: Complete ECDH key exchange
- **Key Features**:
  - Client sends client public key + signatures
  - Server verifies signatures and completes key exchange
  - Shared secret established for encryption

### 2. Messaging Phase

#### 2.1 Message Send

- **File**: `03-messaging/03-message-send-request.json` & `03-message-send-response.json`
- **Endpoint**: `POST /message/send?userId=group-2`
- **Purpose**: Send encrypted message to SecureBot
- **Key Features**:
  - End-to-end encryption using ECDH shared secret
  - Message authentication with ECDSA signatures
  - Bot responds with encrypted reply

## Conversation Flow

1. **User Message**: "what is your name ?"
2. **Bot Response**: "I'm SecureBot 🤖 — your friendly neighborhood crypto guardian!"

## Security Analysis

- **Encryption**: ECDH_2 for key exchange, symmetric encryption for messages
- **Authentication**: ECDSA-P256 signatures throughout
- **Session Management**: JWT tokens with encrypted session data
- **Security Level**: High - Strong cryptographic implementation

## File Structure

```
04-screenshots/
├── api-data/                          # Structured JSON data
│   ├── 01-authentication/
│   │   ├── 01-session-create-request.json
│   │   └── 01-session-create-response.json
│   ├── 02-key-exchange/
│   │   ├── 02-session-exchange-request.json
│   │   └── 02-session-exchange-response.json
│   ├── 03-messaging/
│   │   ├── 03-message-send-request.json
│   │   └── 03-message-send-response.json
│   └── API-Summary.md (this file)
└── burp-screenshots/                  # Burp Suite screenshots
    ├── 01-authentication/
    │   └── 01-session-create-burp-capture.png
    ├── 02-key-exchange/
    │   └── 02-session-exchange-burp-capture.png
    └── 03-messaging/
        └── 03-message-send-burp-capture.png
```

## Data Format

All JSON files follow standardized structure:

- **Request files**: endpoint, host, headers, requestBody, metadata
- **Response files**: status, headers, responseBody, metadata
- **Clean JSON**: Properly formatted, no HTTP headers mixed in
- **Metadata**: Additional context like plaintext messages, timestamps
