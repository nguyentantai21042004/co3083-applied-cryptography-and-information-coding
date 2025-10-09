# Dữ liệu
mods = [5, 11, 17]
rem = [2, 3, 5]

# Tính N và các Ni = N/ni
from math import prod

N = prod(mods)
Ni = [N // m for m in mods]

# Nghịch đảo modular Ni^{-1} mod ni
# dùng pow(Ni, -1, ni) (Python 3.8+), hoặc extended_gcd nếu cần
inv = [pow(Ni[i], -1, mods[i]) for i in range(len(mods))]

# Công thức CRT: x ≡ sum(ai * Ni * inv_i) (mod N)
x = sum(rem[i] * Ni[i] * inv[i] for i in range(len(mods))) % N

print("N =", N)  # 935
print("x mod N =", x)  # 872
