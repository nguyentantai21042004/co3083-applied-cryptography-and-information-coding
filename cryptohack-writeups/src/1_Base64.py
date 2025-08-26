import base64

# Given hex string
hex_str = '72bca9b68fc16ac7beeb8f849dca1d8a783e8acf9679bf9269f7bf'

# Decode the hex string to bytes
byte_data = bytes.fromhex(hex_str)

# Encode the bytes to Base64
base64_encoded = base64.b64encode(byte_data).decode('utf-8')

print(base64_encoded)