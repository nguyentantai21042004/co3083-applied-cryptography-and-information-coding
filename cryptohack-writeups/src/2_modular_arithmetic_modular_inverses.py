# Cách 1: dùng pow() với Fermat's Little Theorem
p = 13
a = 3
inverse = pow(a, p-2, p)
print("Inverse of 3 mod 13 =", inverse)

# Cách 2: kiểm chứng thủ công
print((a * inverse) % p)