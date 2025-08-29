# XOR Starter - CryptoHack Challenge Write-up

## 📋 Challenge Description

**Challenge Name:** XOR Starter  
**Category:** Symmetric Ciphers  
**Difficulty:** Easy  
**Points:** 5

**Problem Statement:**
> XOR is a bitwise operator which returns 0 if the bits are the same, and 1 otherwise. In textbooks the XOR operator is denoted by ⊕, but in most challenges and programming languages you will see the caret ^ used instead.
> 
> For longer binary numbers we XOR bit by bit: 0110 ^ 1010 = 1100. We can XOR integers by first converting the integer from decimal to binary. We can XOR strings by first converting each character to the integer representing the Unicode character.
> 
> Given the string "label", XOR each character with the integer 13. Convert these integers back to a string and submit the flag as `crypto{new_string}`.

## 🔍 Understanding XOR Operation

### XOR Truth Table
| A | B | A ⊕ B |
|---|---|-------|
| 0 | 0 |   0   |
| 0 | 1 |   1   |
| 1 | 0 |   1   |
| 1 | 1 |   0   |

### Key Properties of XOR
- **Commutative:** A ⊕ B = B ⊕ A
- **Associative:** (A ⊕ B) ⊕ C = A ⊕ (B ⊕ C)
- **Identity:** A ⊕ 0 = A
- **Self-inverse:** A ⊕ A = 0
- **Distributive:** A ⊕ (B ⊕ C) = (A ⊕ B) ⊕ C

## 🧮 Solution Approach

### Step 1: Understand the Process
1. Take each character from the string "label"
2. Convert character to its ASCII/Unicode value
3. XOR that value with integer 13
4. Convert the result back to a character
5. Concatenate all results to form the final string

### Step 2: Manual Calculation

Let's work through each character:

**String:** "label"  
**XOR Key:** 13 (binary: 1101)

| Char | ASCII | Binary    | XOR with 13 | Result Char |
|------|--------|-----------|-------------|-------------|
| l    | 108    | 01101100  | 01101100 ⊕ 00001101 = 01100001 | a (97) |
| a    | 97     | 01100001  | 01100001 ⊕ 00001101 = 01101100 | l (108) |
| b    | 98     | 01100010  | 01100010 ⊕ 00001101 = 01101111 | o (111) |
| e    | 101    | 01100101  | 01100101 ⊕ 00001101 = 01101000 | h (104) |
| l    | 108    | 01101100  | 01101100 ⊕ 00001101 = 01100001 | a (97) |

**Result:** "aloha"

## 💻 Implementation

### Method 1: Manual Implementation
```python
def xor_with_13():
    label = "label"
    result = ""
    for char in label:
        xor_result = ord(char) ^ 13
        result += chr(xor_result)
    return result
```

### Method 2: Using pwntools Library
```python
from pwn import xor
label = b"label"
result = xor(label, 13)
```

### Method 3: List Comprehension
```python
result = ''.join(chr(ord(c) ^ 13) for c in "label")
```

## 🎯 Solution

**Input String:** "label"  
**XOR Key:** 13  
**Result:** "aloha"  
**Flag:** `crypto{aloha}`

## 🔧 Running the Solution

```bash
cd cryptohack-writeups/symmetric-ciphers/xor
python3 xor_starter.py
```

**Expected Output:**
```
=== XOR Starter Challenge Solution ===

Original string: label
XOR result: aloha
Flag: crypto{aloha}

Using pwntools:
Original: b'label'
XOR with 13: b'aloha'
Flag: crypto{aloha}

=== Manual XOR Implementation ===
Character | ASCII | Binary | XOR with 13 | Result
--------------------------------------------------
    l     |  108  | 01101100 |  97 (01100001) |   a
    a     |   97  | 01100001 | 108 (01101100) |   l
    b     |   98  | 01100010 | 111 (01101111) |   o
    e     |  101  | 01100101 | 104 (01101000) |   h
    l     |  108  | 01101100 |  97 (01100001) |   a

🎯 Final Answer: crypto{aloha}
```

## 📚 Learning Points

### 1. **Bitwise Operations**
- XOR is fundamental in cryptography
- Understanding binary representation is crucial
- Bit-by-bit operations on data

### 2. **Character Encoding**
- Characters are represented as integers (ASCII/Unicode)
- Conversion between characters and integers using `ord()` and `chr()`
- String manipulation in Python

### 3. **Cryptographic Concepts**
- XOR is used in many encryption algorithms
- Simple XOR can be a building block for more complex ciphers
- Understanding how to reverse XOR operations

### 4. **Python Skills**
- String iteration and manipulation
- List comprehensions
- Error handling with try-except
- Using external libraries (pwntools)

## 🔍 Verification

To verify our solution:
```python
# Verify: XOR result with 13 should give back original
original = "label"
result = "aloha"
verification = ''.join(chr(ord(c) ^ 13) for c in result)
print(verification == original)  # Should print: True
```

## 🚀 Next Steps

After completing this challenge, you can explore:
- **XOR Properties:** Understanding why XOR is useful in cryptography
- **Stream Ciphers:** How XOR is used in encryption
- **Frequency Analysis:** Breaking simple XOR ciphers
- **Advanced XOR:** Multi-byte keys and repeating key XOR

## 📖 References

- [CryptoHack XOR Starter](https://cryptohack.org/challenges/symmetric/)
- [Python Bitwise Operators](https://docs.python.org/3/reference/expressions.html#binary-bitwise-operations)
- [ASCII Table](https://www.asciitable.com/)
- [XOR in Cryptography](https://en.wikipedia.org/wiki/XOR_cipher)

---

**Challenge Completed! 🎉**  
**Flag:** `crypto{aloha}`

