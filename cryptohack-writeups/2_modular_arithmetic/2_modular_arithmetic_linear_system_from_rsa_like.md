# Recovering p, q from linear combinations inside RSA-like exponents

**File name:** `modular_arithmetic_linear_system_from_rsa_like.md`

## Idea
Đặt:
- A = 2p + 3q
- B = 5p + 7q

Đề cho:
- c1 ≡ A^{e1} (mod N)
- c2 ≡ B^{e2} (mod N)
- N = p·q

Nếu e1=e2=1 (hoặc bằng cách nào đó lấy được A,B từ c1,c2), ta có hệ: