# Code-to-API Mapping Analysis

## API Endpoints Found in Decompiled Code

### 1. Session Create API (Authentication)

**API Call**: `POST /session/create?userId=group-2`
**Code Location**:

- **File**: `smali_classes4/com/example/securechat/LoginActivity.smali`
- **Line**: 550
- **Code**: `const-string v7, "https://crypto-assignment.dangduongminhnhat2003.workers.dev/session/create?userId="`

**Analysis**:

- URL is hardcoded in LoginActivity
- Uses string concatenation to build full URL with userId parameter
- This confirms LoginActivity handles the authentication/key exchange process

### 2. Session Exchange API (Key Exchange)

**API Call**: `POST /session/exchange?userId=group-2`
**Code Location**:

- **Status**: ✅ **CRYPTO COMPONENTS FOUND**
- **Keywords Found**: `ecdh_2`, `curveParameters`, `clientPublicKey`, `serverPublicKey`
- **Analysis**: Key exchange logic distributed across multiple methods and classes
- **Primary File**: LoginActivity.smali (likely contains URL construction)
- **Crypto Operations**: Found in multiple smali files

**Screenshots Captured**:

- Session exchange search: `04-screenshots/code-mapping/02-session-exchange-search.png`
- ECDH algorithm: `04-screenshots/code-mapping/03-ecdh2-algorithm-search.png`
- Curve parameters: `04-screenshots/code-mapping/04-curve-parameters-search.png`
- Client public key: `04-screenshots/code-mapping/05-client-public-key-search.png`
- Server public key: `04-screenshots/code-mapping/06-server-public-key-search.png`

### 3. Message Send API (Messaging)

**API Call**: `POST /message/send?userId=group-2`
**Code Location**:

- **Status**: ✅ **MESSAGING COMPONENTS FOUND**
- **Keywords Found**: `encryptedMessage`, `messageSignature`, `encryptedResponse`
- **Keywords NOT Found**: `/message/send` (likely dynamic), `what is your name`, `SecureBot` (encrypted at runtime)
- **Analysis**: Messaging logic found but API endpoint built dynamically
- **Behavior**: Normal - plaintext messages encrypted before storage/transmission

**Screenshots Captured**:

- Message send search: `04-screenshots/code-mapping/07-message-send-search.png`
- Encrypted message: `04-screenshots/code-mapping/08-encrypted-message-found.png`
- Message signature: `04-screenshots/code-mapping/09-message-signature-found.png`
- Encrypted response: `04-screenshots/code-mapping/10-encrypted-response-found.png`
- SecureBot search (no results): `04-screenshots/code-mapping/11-securebot-search-no-results.png`

## Code Analysis Summary

### LoginActivity.smali Analysis

- **Primary Function**: Handles user authentication and key exchange
- **Server URL**: crypto-assignment.dangduongminhnhat2003.workers.dev
- **HTTP Client**: Uses OkHttp3 (evident from RequestBody usage)
- **URL Construction**: Dynamic URL building with userId parameter

### Code-to-API Mapping Table

| API Endpoint      | HTTP Method | Smali File          | Line    | Components Found                                          | Status              |
| ----------------- | ----------- | ------------------- | ------- | --------------------------------------------------------- | ------------------- |
| /session/create   | POST        | LoginActivity.smali | 550     | Hardcoded URL construction                                | ✅ FOUND            |
| /session/exchange | POST        | Multiple files      | Various | ecdh_2, curveParameters, clientPublicKey, serverPublicKey | ✅ COMPONENTS FOUND |
| /message/send     | POST        | Multiple files      | Various | encryptedMessage, messageSignature, encryptedResponse     | ✅ COMPONENTS FOUND |

## Detailed Analysis

### Session Create (Authentication)

- **URL Construction**: Hardcoded base URL + dynamic userId
- **Location**: LoginActivity.smali line 550
- **Pattern**: `const-string v7, "https://crypto-assignment.dangduongminhnhat2003.workers.dev/session/create?userId="`

### Session Exchange (Key Exchange)

- **Components**: ECDH_2 algorithm, curve parameters, public key operations
- **Distribution**: Logic spread across multiple smali files
- **Crypto Operations**: Elliptic curve cryptography implementation

### Message Send (Messaging)

- **Components**: Message encryption, digital signatures, response handling
- **Security**: End-to-end encryption, no plaintext storage
- **Pattern**: Runtime encryption/decryption of message content

## Screenshots Reference

### Code Mapping Screenshots

- Session create: `04-screenshots/code-mapping/01-session-create-code-found.png`
- Session exchange: `04-screenshots/code-mapping/02-session-exchange-search.png`
- ECDH algorithm: `04-screenshots/code-mapping/03-ecdh2-algorithm-search.png`
- Curve parameters: `04-screenshots/code-mapping/04-curve-parameters-search.png`
- Client public key: `04-screenshots/code-mapping/05-client-public-key-search.png`
- Server public key: `04-screenshots/code-mapping/06-server-public-key-search.png`
- Message send: `04-screenshots/code-mapping/07-message-send-search.png`
- Encrypted message: `04-screenshots/code-mapping/08-encrypted-message-found.png`
- Message signature: `04-screenshots/code-mapping/09-message-signature-found.png`
- Encrypted response: `04-screenshots/code-mapping/10-encrypted-response-found.png`
