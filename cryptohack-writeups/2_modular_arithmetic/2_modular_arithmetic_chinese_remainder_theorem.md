# Chinese Remainder Theorem (CRT)

**File name:** `modular_arithmetic_chinese_remainder_theorem.md`

## Description
Giải hệ đồng dư:
- x ≡ 2 (mod 5)
- x ≡ 3 (mod 11)
- x ≡ 5 (mod 17)

Vì 5, 11, 17 đôi một nguyên tố cùng nhau, tồn tại nghiệm duy nhất mod N=5·11·17=935.

## Solution
Công thức CRT:
- N = 935
- N1 = N/5 = 187, tìm e1 = N1^{-1} (mod 5). Vì 187 ≡ 2 (mod 5), e1 = 3 (2·3≡1).
- N2 = N/11 = 85,  85 ≡ 8 (mod 11) ⇒ e2 = 7 (8·7≡1).
- N3 = N/17 = 55,  55 ≡ 4 (mod 17) ⇒ e3 = 13 (4·13≡1).

Sau đó:
x ≡ a1*N1*e1 + a2*N2*e2 + a3*N3*e3 (mod N)
  ≡ 2·187·3 + 3·85·7 + 5·55·13
  ≡ 1122 + 1785 + 3575
  ≡ 6482 ≡ 872 (mod 935)

## Verification
- 872 mod 5  = 2
- 872 mod 11 = 3
- 872 mod 17 = 5

## Answer
**a = 872**