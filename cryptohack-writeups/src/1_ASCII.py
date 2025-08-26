
arr = [99, 114, 121, 112, 116, 111, 123, 65, 83, 67, 73, 73, 95, 112, 114, 49, 110, 116, 52, 98, 108, 51, 125]

decrypted_flag = "".join(chr(i) for i in arr)
print(decrypted_flag)

# flag: crypto{ASCII_pr1nt4bl3}

def encrypt_flag(str):
    return "".join(chr(ord(i) ^ 13) for i in str)

print(encrypt_flag(decrypted_flag))

# flag: crypto{ASCII_pr1nt4bl3}