# Legendre Symbol & Square Roots (p ≡ 3 mod 4)

**File name:** `modular_arithmetic_legendre_symbol.md`

## 1) Tóm tắt lý thuyết
- Với p nguyên tố lớn, kiểm tra "x có là bình phương mod p không" dùng **ký hiệu Legendre**:
  (x/p) ≡ x^((p-1)/2) (mod p) ∈ {1, -1, 0}.
- Nếu (x/p) = 1 ⇒ x là **quadratic residue (QR)**; = -1 ⇒ **non-residue (QNR)**; = 0 ⇒ x ≡ 0 (mod p).
- Nếu p ≡ 3 (mod 4), căn bậc hai của QR x tính rất nhanh:
  a ≡ x^((p+1)/4) (mod p), nghiệm còn lại là p - a.

## 2) Bài toán
- Cho p (1024-bit, p ≡ 3 mod 4) và 10 số `ints`.
- Bước 1: dùng Legendre để tìm số duy nhất là QR.
- Bước 2: tính căn bậc hai của nó; nộp **nghiệm lớn hơn** làm flag.

## 3) Cách giải & Code
- Đánh dấu từng x bằng pow(x, (p-1)//2, p) để lấy Legendre.
- Lấy x là QR, rồi tính a = pow(x, (p+1)//4, p).
- Flag = max(a, p-a).

(Đính kèm code tham khảo ở phần trên.)

## 4) Kết quả
- Số là QR: **ints[5]**.
- Hai căn: a và p-a.
- **Flag (nghiệm lớn hơn):**
93291799125366706806545638475797430512104976066103610269938025709952247020061090804870186195285998727680200979853848718589126765742550855954805290253592144209552123062161458584575060939481368210688629862036958857604707468372384278049741369153506182660264876115428251983455344219194133033177700490981696141526