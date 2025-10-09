## Challenge: The Greatest Common Divisor (GCD)

### Description
Tính Ước Chung Lớn Nhất (GCD) của hai số nguyên dương `a` và `b` bằng thuật toán Euclid.  
Test với `a=12`, `b=8`, sau đó tính với `a=66528`, `b=52920`.

### Solution
Sử dụng định nghĩa:
> gcd(a, b) = gcd(b, a mod b)  
> cho đến khi b = 0.

```python
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

print(gcd(66528, 52920))