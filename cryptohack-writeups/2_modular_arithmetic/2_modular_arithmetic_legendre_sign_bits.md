# Legendre-based sign encoding — Recovering the flag

**File name:** `modular_arithmetic_legendre_sign_bits.md`

## Idea
Mã hóa mỗi bit thành \(a^e \bmod p\) nếu bit=1, và \(-a^e \bmod p\) nếu bit=0.  
Nếu \(p \equiv 3 \pmod 4\) thì \((-1/p)=-1\). Nếu thêm \((a/p)=1\) thì \((a^e/p)=1\) với mọi \(e\).  
Do đó:
- bit `1` ⇒ Legendre(cipher) = \(1\)
- bit `0` ⇒ Legendre(cipher) = \(-1\)

Vì thế chỉ cần tính ký hiệu Legendre của từng phần tử ciphertext để khôi phục bitstream, sau đó nhóm 8 bit thành byte theo thứ tự MSB→LSB (đúng như `''.join(bin(i)[2:].zfill(8) for i in flag)` trong đề).

## Steps
1. Kiểm tra \(p \bmod 4 = 3\) ⇒ \((-1/p)=-1\).
2. Tính \((a/p)\) và thấy bằng 1 ⇒ \((a^e/p)=1\) với mọi \(e\).
3. Với từng ciphertext \(c\), tính \(c^{(p-1)/2} \bmod p\):
   - 1 → bit ‘1’
   - \(p-1\) → bit ‘0’
4. Gom 8 bit/byte, decode ASCII.

## Result
**Flag:** `crypto{p4tterns_1n_re5idu3s}`