# Quadratic Residues over F_p

**File name:** `modular_arithmetic_quadratic_residues.md`

## 1) Tóm tắt & lý thuyết
Trong trường hữu hạn \(\mathbb{F}_p\) (p nguyên tố), gọi \(x\) là **quadratic residue (QR)** nếu tồn tại \(a\) sao cho \(a^2 \equiv x \pmod p\); nếu không, \(x\) là **non-residue (QNR)**. Với mỗi QR, luôn có **hai nghiệm** \(a\) và \(-a \equiv p-a\).

## 2) Bài toán
- \(p = 29\)
- `ints = [14, 6, 11]`
- Tìm phần tử là **QR**, tính căn bậc hai của nó, và nộp **nghiệm nhỏ hơn** làm flag.

## 3) Cách giải
Vì \(p\) nhỏ, brute-force kiểm tra \((a^2 \bmod p)\) cho \(a \in \{0,\dots,p-1\}\).  
(Trong tổng quát, có thể dùng **Tonelli–Shanks** để lấy căn bậc hai modulo p nguyên tố.)

## 4) Code
```python
p = 29
ints = [14, 6, 11]

def square_roots_mod_p(x, p):
    roots = []
    for a in range(p):
        if (a * a) % p == x % p:
            roots.append(a)
    return sorted(set(roots))

qr_candidates = {x: square_roots_mod_p(x, p) for x in ints}
print(qr_candidates)