# Login API Analysis - Captured Data

## 1. Session Create API

### Request

- **Endpoint**: `POST /session/create?userId=group-2`
- **Host**: crypto-assignment.dangduongminhnhat2003.workers.dev
- **Headers**:
  - X-User-Id: group-2
  - Content-Type: application/json; charset=utf-8
  - User-Agent: okhttp/4.11.0

### Request Body (Formatted)

```json
{
  "algorithm": "ecdh_2",
  "curveParameters": {
    "p": "115792089210356248762697446949407573530086143415290314195533631308867097853951",
    "a": "-3",
    "b": "41058363725152142129326129780047268409114441015993725554835256314039467401291",
    "Gx": "48439561293906451759052585252797914202762949526041747995844080717082404635286",
    "Gy": "36134250956749795798585127919587881956611106672985015071877198253568414405109",
    "order": "115792089210356248762697446949407573529996955224135760342422259061068512044369"
  }
}
```

### Response

- **Status**: 200 OK
- **Headers**: Content-Type: application/json

### Response Body (Key Fields)

```json
{
  "success": true,
  "sessionToken": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
  "algorithm": "ecdh_2",
  "serverPublicKey": {
    "x": "108403884051254254355072719243635691885388267527392976659047680224103236631750",
    "y": "59428322367280812028082171623882445369407632434445180685123412416293451614781"
  },
  "signatureSupported": true,
  "serverSignaturePublicKey": {
    "x": "57148276168508521052242506279786419515268275974543392460161868634401787378820",
    "y": "115179942221755681754516411562467214652606277563851287151627283510846281485120"
  },
  "sessionSignature": {
    "r": "66889653065872274982018439208838230915718264377756460729586208415694313300926",
    "s": "59414307936893008229194657999453494367712491202740598871304207419041281488252",
    "messageHash": "54593776055354841420994645875048485931500939894373122888259713808776035333227",
    "algorithm": "ECDSA-P256"
  },
  "signatureAlgorithm": "ECDSA-P256"
}
```

---

## 2. Session Exchange API

### Request

- **Endpoint**: `POST /session/exchange?userId=group-2`
- **Host**: crypto-assignment.dangduongminhnhat2003.workers.dev
- **Headers**: Same as above

### Request Body (Key Fields)

```json
{
  "sessionToken": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
  "clientPublicKey": {
    "x": "4357310967645071789523757570136769223221101142442506170148130612898569960008",
    "y": "83772561147671305448585394191265703098056680965763100082235839861190153167518"
  },
  "clientPublicKeySignature": {
    "r": "91910994148506534561372800830543095620108129922263106006580266327061497142675",
    "s": "85650801310916979399664878953525721473344896066012875794052023294088604802929",
    "messageHash": "69729588429778916534444923603439409969931311880766751961335726889892654108522",
    "algorithm": "ECDSA-P256"
  },
  "clientSignaturePublicKey": {
    "x": "14404422292550558242297339553322053173706357772363553432259939928339233726381",
    "y": "9599261096838343071363020776933197501659012130960919404070372272763443576925"
  }
}
```

### Response

- **Status**: 200 OK

### Response Body

```json
{
  "success": true,
  "message": "Key exchange completed",
  "algorithm": "ecdh_2",
  "sessionToken": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
  "clientSignatureVerified": true
}
```

---

## Analysis Summary

### Protocol Flow

1. **Session Create**: Client sends ECDH curve parameters → Server responds with server public key + session token
2. **Session Exchange**: Client sends client public key + signatures → Server verifies and completes key exchange

### Cryptographic Details

- **Algorithm**: ECDH_2 (Elliptic Curve Diffie-Hellman)
- **Curve**: P-256 (based on parameters)
- **Signature**: ECDSA-P256 for authentication
- **Session Management**: JWT tokens for session tracking

### Security Features

- ✅ Strong cryptography (ECDH + ECDSA)
- ✅ Digital signatures for authentication
- ✅ Session tokens for state management
- ✅ Proper key exchange protocol
