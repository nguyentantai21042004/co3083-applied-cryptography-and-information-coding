# Write-up: XOR Properties Challenge

When I first looked at this challenge, I immediately noticed that it was testing my understanding of XOR’s fundamental properties: **commutative, associative, identity, and self-inverse**. These properties allow me to rearrange and simplify chains of XOR operations without losing correctness.  

We are given:  

```
KEY1 = a6c8b6733c9b22de7bc0253266a3867df55acde8635e19c73313
KEY2 ^ KEY1 = 37dcb292030faa90d07eec17e3b1c6d8daf94c35d4c9191a5e1e
KEY2 ^ KEY3 = c1545756687e7573db23aa1c3452a098b71a7fbf0fddddde5fc1
FLAG ^ KEY1 ^ KEY3 ^ KEY2 = 04ee9855208a2cd59091d04767ae47963170d1660df7f56f5faf
```

Before doing any XOR, I made sure to decode all hex strings into bytes.  

---

## Approach 1: Direct Simplification Using Properties

The last line looks complicated, but with XOR properties it becomes simple:

```
FLAG = (FLAG ^ KEY1 ^ KEY3 ^ KEY2) ^ KEY1 ^ (KEY2 ^ KEY3)
```

Here’s why:
- By XORing again with `KEY1`, the duplicate `KEY1` cancels (`KEY1 ^ KEY1 = 0`).  
- By XORing with `(KEY2 ^ KEY3)`, I cancel out the `KEY2 ^ KEY3` part inside.  
- What remains is just the `FLAG`.  

So I only need to compute one XOR chain:  

```
FLAG = (ciphertext) ^ KEY1 ^ (KEY2 ^ KEY3)
```

That gives the final answer:

```
crypto{x0r_i5_ass0c1at1v3}
```

---

## Approach 2: Step-by-Step Key Recovery

I also tried a longer route, where I explicitly recovered each key:  

1. From `KEY2 ^ KEY1`, I can solve for `KEY2`:
   ```
   KEY2 = (KEY2 ^ KEY1) ^ KEY1
   ```
   (because XORing back with `KEY1` cancels it out).  

2. From `KEY2 ^ KEY3`, I can then solve for `KEY3`:
   ```
   KEY3 = (KEY2 ^ KEY3) ^ KEY2
   ```

3. Now that I know `KEY1`, `KEY2`, and `KEY3`, I can decrypt the flag:
   ```
   FLAG = (FLAG ^ KEY1 ^ KEY3 ^ KEY2) ^ KEY1 ^ KEY3 ^ KEY2
   ```

This also reduces correctly to just `FLAG`.  

---

## Final Thoughts

Both approaches lead to the same flag, but I found the first one much cleaner because it avoids unnecessary work. It really highlights the power of XOR’s algebraic properties: reordering, regrouping, and canceling terms makes the problem almost trivial.  

**Final Flag:**  
```
crypto{x0r_i5_ass0c1at1v3}
```
