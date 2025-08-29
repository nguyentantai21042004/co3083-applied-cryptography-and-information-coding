# Write-up: Repeating-Key XOR (CTF)

*I* encountered this challenge after completing the single-byte XOR. The biggest difference: instead of a **single byte key**, here the data is encrypted using a **multi-byte repeating key** (repeating-key XOR). The hint "Remember the flag format" helped me exploit the **known-plaintext** `crypto{...}` to recover the key.

---

## Problem Statement
Ciphertext (hex):
```
0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104
```

Flag format: `crypto{...}`.

---

## Main Idea
- Repeating-key XOR: each plaintext byte P[i] is XORed with K[i mod len(K)].
- Knowing the prefix `crypto{` → XOR the first 7 bytes of ciphertext with `b"crypto{"` to reveal **first 7 bytes of the key** → deduce the complete key (usually a meaningful word that repeats).
- After knowing the key, XOR the entire ciphertext with the repeating key to obtain the plaintext.

---

## Method 1 – Known-plaintext (Fast & Simple)
1. Convert **hex → bytes**.  
2. Take `C[:7] ^ b"crypto{"` → obtain **first 7 bytes of the key**.  
3. From that, recognize the meaningful key **`myXORkey`** (8 bytes, repeating).  
4. XOR the entire `C` with the repeating key ⇒ get the flag.

> **Result:** `crypto{1f_y0u_Kn0w_En0uGH_y0u_Kn0w_1t_4ll}`

### Small Code Snippet (Python)
```python
from itertools import cycle

hex_ct = "0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104"
ct = bytes.fromhex(hex_ct)

# recover first 7 bytes of key from known-plaintext "crypto{"
k7 = bytes(c ^ p for c, p in zip(ct[:7], b"crypto{"))  # -> b"myXORke"
key = b"myXORkey"

pt = bytes(c ^ k for c, k in zip(ct, cycle(key)))
print(pt.decode())
```

---

## Method 2 – Without known-plaintext (General)
When the prefix is unknown, I use the standard "textbook" approach:
1. **Estimate key length** (2–40) using **normalized Hamming distance** between blocks; choose several candidates with lowest values.
2. **Split into columns** by position `i mod KEYSIZE` → each column becomes a **single-byte XOR problem**.
3. For each column, brute-force 0–255, score "English-like" (ASCII/chi-square) to get the best key byte.
4. Combine key bytes → complete key → XOR everything back to get plaintext.

### Mini Code Snippet (Framework)
```python
def hamming(a, b): return sum((x ^ y).bit_count() for x, y in zip(a, b))

# ... calculate scores, choose KEYSIZE candidates, split columns, solve each column (single-byte XOR),
# finally combine key and XOR back.
```

> Executing this method on the ciphertext also yields the key **`myXORkey`** and the plaintext is the flag above.

---

## Conclusion & Notes
- This challenge is **different** from single-byte XOR in **multi-byte repeating keys**.  
- **Known-plaintext** from `crypto{` helps save a lot of time.  
- The general method (Hamming distance + single-byte per column) still applies to challenges without hints.

**Final Flag:**
```
crypto{1f_y0u_Kn0w_En0uGH_y0u_Kn0w_1t_4ll}
```
