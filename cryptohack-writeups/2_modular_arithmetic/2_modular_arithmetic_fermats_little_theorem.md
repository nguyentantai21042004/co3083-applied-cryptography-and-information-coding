# Fermat's Little Theorem — Write-up

**File name:** `modular_arithmetic_fermats_little_theorem.md`

## 1) Bối cảnh & nhắc nhanh lý thuyết

- Khi lấy mô-đun **nguyên tố** \(p\), tập \(\mathbb{F}_p=\{0,1,\dots,p-1\}\) tạo thành **trường**:
  - **Nghịch đảo cộng**: với mọi \(a\), tồn tại \(a_+\) sao cho \(a + a_+ = 0\) (thực chất \(a_+ \equiv -a\)).
  - **Nghịch đảo nhân**: với mọi \(a \neq 0\), tồn tại \(a_*\) sao cho \(a \cdot a_* = 1\).
  - **Phần tử đơn vị** khác nhau cho hai phép: \(0\) (cộng) và \(1\) (nhân).
- Nếu mô-đun **không nguyên tố** \(n\), ta chỉ có **vành** \(\mathbb{Z}_n\); không phải mọi phần tử đều có nghịch đảo nhân.

## 2) Định lý nhỏ của Fermat (FLT)

- Với \(p\) **nguyên tố** và \(a \not\equiv 0 \pmod p\):
  \[
    a^{p-1} \equiv 1 \pmod p.
  \]
- Dạng hệ quả (đúng cho **mọi** \(a\)):
  \[
    a^{p} \equiv a \pmod p.
  \]
- **Chứng minh phác thảo (intuition nhóm)**: Tập các phần tử khác 0 trong \(\mathbb{F}_p\) tạo thành một **nhóm nhân** có \(p-1\) phần tử. Nhân toàn bộ nhóm với \(a\) (với \(a \neq 0\)) chỉ là một **hoán vị** của tập đó, nên tích các phần tử **không đổi**:
  \[
    1\cdot2\cdots(p-1) \equiv a\cdot2a\cdots(p-1)a \equiv a^{p-1}\cdot(1\cdot2\cdots(p-1)).
  \]
  Khử tích chung hai vế (hợp lệ vì nó khác 0 trong trường) ⇒ \(a^{p-1}\equiv 1 \pmod p\).

## 3) Bài toán & lời giải

### (A) Với \(p=17\)

1. **\(3^{17} \bmod 17\)**  
   Dùng hệ quả \(a^p \equiv a \ (p \text{ prime})\):  
   \[
     3^{17} \equiv 3 \pmod{17}.
   \]

2. **\(5^{17} \bmod 17\)**  
   Tương tự: \(\;5^{17} \equiv 5 \pmod{17}\).

3. **\(7^{16} \bmod 17\)**  
   Áp dụng trực tiếp FLT dạng chuẩn:  
   \[
     7^{16} \equiv 1 \pmod{17}.
   \]

### (B) Với \(p=65537\) (một **Fermat prime**, \(65537 = 2^{16}+1\))

Tính \(273246787654^{65536} \bmod 65537\).  
Vì \(p-1 = 65536\) và \(a = 273246787654 \not\equiv 0 \pmod{65537}\), theo FLT:
\[
  a^{p-1} \equiv 1 \pmod p \quad\Rightarrow\quad 273246787654^{65536} \equiv 1 \pmod{65537}.
\]
**Không cần máy tính**: chỉ cần FLT.

## 4) Kiểm chứng nhanh (Python)

```python
p = 17
assert pow(3, 17, p) == 3
assert pow(5, 17, p) == 5
assert pow(7, 16, p) == 1

p2 = 65537
a = 273246787654
assert pow(a, p2-1, p2) == 1
```

## 5) Lưu ý/Edge cases

- Nếu \(a \equiv 0 \pmod p\) ⇒ mọi lũy thừa \(a^k \equiv 0\) (với \(k \ge 1\)); dạng \(a^p \equiv a\) vẫn đúng (cả hai đều 0).
- Nếu mô-đun không nguyên tố \(n\): FLT không áp dụng; dùng Định lý Euler \(a^{\varphi(n)} \equiv 1 \pmod n\) (khi \(\gcd(a,n)=1\)).
- Thực hành: Python có `pow(a, e, m)` tính \(a^e \bmod m\) rất nhanh (bình phương & nhân lặp).

## 6) Kết quả & Flag

- \(3^{17} \bmod 17 = 3\)
- \(5^{17} \bmod 17 = 5\)
- \(7^{16} \bmod 17 = 1\)
- \(273246787654^{65536} \bmod 65537 = \mathbf{1}\)

**Flag: 1**