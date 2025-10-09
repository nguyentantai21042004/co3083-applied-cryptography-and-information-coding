# Modular Inverses — Write-up

**File name:** `modular_arithmetic_modular_inverses.md`

## 1) Lý thuyết nền tảng

Khi làm việc trong trường hữu hạn \( \mathbb{F}_p \) (với p là số nguyên tố), mọi phần tử khác 0 đều có **nghịch đảo nhân**.  
Ta cần tìm \( d \) sao cho:
\[
a \cdot d \equiv 1 \pmod{p}.
\]

**Ví dụ:**
\[
7 \cdot 8 = 56 \equiv 1 \ (\text{mod } 11) \Rightarrow 7^{-1} = 8.
\]

Vì tập \(\mathbb{F}_p^\*\) (các phần tử khác 0) tạo thành một **nhóm nhân** có \(p-1\) phần tử, mọi phần tử đều có nghịch đảo duy nhất.

## 2) Liên hệ với Fermat's Little Theorem (FLT)

Theo FLT, với \(a\) không chia hết cho \(p\):
\[
a^{p-1} \equiv 1 \pmod{p}.
\]
Nhân hai vế với \(a^{-1}\), ta được:
\[
a^{p-2} \equiv a^{-1} \pmod{p}.
\]

→ Đây là **cách nhanh nhất** để tính nghịch đảo modular khi \(p\) là số nguyên tố.

## 3) Áp dụng vào bài toán

**Tìm \(d = 3^{-1} \pmod{13}\).**

Dùng công thức:
\[
d \equiv 3^{13-2} = 3^{11} \pmod{13}.
\]

Tính tay (hoặc bằng code):
\[
3^{11} \bmod 13 = 9.
\]

→ \(3^{-1} \equiv 9 \pmod{13}\).

**Kiểm tra:**
\[
3 \times 9 = 27 \equiv 1 \pmod{13}.
\]

✅ **Đúng.**

## 4) Code kiểm chứng

```python
p = 13
a = 3
inverse = pow(a, p-2, p)
print("Inverse of 3 mod 13 =", inverse)
print("Check:", (a * inverse) % p)
```

## 5) Kết quả

**Flag: 9**