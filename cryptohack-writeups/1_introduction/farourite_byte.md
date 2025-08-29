# Write-up: Single-Byte XOR Challenge

When I saw this challenge, I recognized it immediately as a **single-byte XOR cipher** problem. The task is to decrypt a piece of data that was hidden by XORing every byte with the same secret key byte.  

We are given the ciphertext in hex:  

```
73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d
```

---

## Step 1: Understand the Problem

The challenge states that the flag was XORed with a *single byte*. A single byte can only take values from **0 to 255** (since a byte is 8 bits, and 2^8 = 256 possible values).  

That means the key space is very small, so I can brute-force every possible key to see which one decrypts the ciphertext into a meaningful flag.  

---

## Step 2: Convert Hex to Bytes

The ciphertext is given in hex, so the first step is to decode it into raw bytes. In Python:  

```python
cipher_hex = "73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d"
cipher_bytes = bytes.fromhex(cipher_hex)
```

---

## Step 3: Brute-Force All Keys (0–255)

Now I try every possible key and XOR it with the ciphertext. If the output looks like readable ASCII and especially starts with `crypto{`, I know I’ve found the flag.  

Example brute force loop:  

```python
for key in range(256):
    decoded = ''.join(chr(b ^ key) for b in cipher_bytes)
    if decoded.startswith("crypto{"):
        print(key, decoded)
```

---

## Step 4: Result

After running the brute force, I found the correct key and the flag decrypted to:  

```
crypto{0x10_15_my_f4v0ur173_by7e}
```

---

## Final Thoughts

This challenge is a classic introduction to XOR-based ciphers. The key takeaway is that when XOR is used with a single byte key, brute force is always feasible because the key space is so small (only 256 options).  

**Final Flag:**  
```
crypto{0x10_15_my_f4v0ur173_by7e}
```
