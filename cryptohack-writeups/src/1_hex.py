str = '63727970746f7b596f755f77696c6c5f62655f776f726b696e675f776974685f6865785f737472696e67735f615f6c6f747d'

decrypted_flag = bytes.fromhex(str).decode('utf-8')
print(decrypted_flag)

def encrypt_flag(str):
    return str.encode('utf-8').hex()

print(encrypt_flag(decrypted_flag))

# flag: 63727970746f7b596f755f77696c6c5f62655f776f726b696e675f776974685f6865785f737472696e67735f615f6c6f747d