## Challenge: Extended Euclidean Algorithm

### File name
`modular_arithmetic_extended_euclidean_algorithm.md`

### Description
Tính các hệ số Bézout `(u, v)` sao cho:
> p * u + q * v = gcd(p, q)

**Given values:**
- p = 26513
- q = 32321

Vì cả hai là số nguyên tố, ta kỳ vọng `gcd(p, q) = 1`.

### Solution

```python
def extended_gcd(a, b):
    if b == 0:
        return a, 1, 0
    else:
        g, x1, y1 = extended_gcd(b, a % b)
        x = y1
        y = x1 - (a // b) * y1
        return g, x, y

p = 26513
q = 32321
g, u, v = extended_gcd(p, q)
print("gcd:", g)
print("u:", u)
print("v:", v)
print("flag:", min(u, v))
```

### Explanation

Thuật toán Euclid mở rộng tìm được hệ số u, v sao cho:

```
26513 * (-8404) + 32321 * 6899 = 1
```

Giá trị nhỏ hơn trong hai số là **-8404**, do đó flag = **-8404**.
