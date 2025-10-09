## Challenge: Modular Congruences

### File name
`modular_arithmetic_congruences.md`

### Description
Tính các phép đồng dư sau:
> 11 ≡ x (mod 6)  
> 8146798528947 ≡ y (mod 17)

Sau đó lấy số nhỏ hơn trong hai giá trị \( x, y \) làm **flag**.

### Solution

```python
x = 11 % 6
y = 8146798528947 % 17

print("x =", x)
print("y =", y)
print("flag =", min(x, y))
```

### Explanation

- \( 11 ÷ 6 \) dư 5, nên \( 11 ≡ 5 \pmod{6} \)
- \( 8146798528947 ÷ 17 \) dư 4, nên \( 8146798528947 ≡ 4 \pmod{17} \)
- Giá trị nhỏ hơn trong (5, 4) là **4** ⇒ **flag = 4**