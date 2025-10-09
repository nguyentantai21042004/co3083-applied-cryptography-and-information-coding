p = 17
print("3^17 mod 17 =", pow(3, 17, p))
print("5^17 mod 17 =", pow(5, 17, p))
print("7^16 mod 17 =", pow(7, 16, p))

p2 = 65537
a = 273246787654
print("a^(p2-1) mod p2 =", pow(a, p2 - 1, p2))