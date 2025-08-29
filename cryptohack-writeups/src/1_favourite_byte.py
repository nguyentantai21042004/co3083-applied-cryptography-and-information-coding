#!/usr/bin/env python3
"""
Single-Byte XOR Challenge - CryptoHack
Challenge: Decrypt data encrypted with single-byte XOR cipher

Given ciphertext (hex):
73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d

Flag: crypto{0x10_15_my_f4v0ur173_by7e}
"""

def hex_to_bytes(hex_string):
    """Convert hex string to bytes"""
    return bytes.fromhex(hex_string)

def bytes_to_hex(byte_data):
    """Convert bytes to hex string"""
    return byte_data.hex()

def xor_single_byte(data, key):
    """XOR data with a single byte key"""
    return bytes(b ^ key for b in data)

def approach_1_brute_force_simple():
    """
    Approach 1: Simple Brute Force
    Try all possible keys (0-255) and look for readable text
    """
    print("=== Approach 1: Simple Brute Force ===")
    
    # Given ciphertext
    cipher_hex = "73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d"
    cipher_bytes = hex_to_bytes(cipher_hex)
    
    print(f"Ciphertext (hex): {cipher_hex}")
    print(f"Ciphertext length: {len(cipher_bytes)} bytes")
    print()
    
    # Try all possible keys
    found_flags = []
    
    for key in range(256):
        decrypted = xor_single_byte(cipher_bytes, key)
        try:
            decrypted_text = decrypted.decode('utf-8')
            
            # Check if it looks like a flag
            if decrypted_text.startswith("crypto{"):
                found_flags.append((key, decrypted_text))
                print(f"🎯 Found flag with key {key} (0x{key:02x}): {decrypted_text}")
            elif "crypto" in decrypted_text.lower():
                print(f"⚠️  Possible flag with key {key} (0x{key:02x}): {decrypted_text}")
                
        except UnicodeDecodeError:
            # Skip non-printable characters
            pass
    
    print(f"\nTotal flags found: {len(found_flags)}")
    return found_flags

def approach_2_brute_force_with_analysis():
    """
    Approach 2: Brute Force with Text Analysis
    Score each decryption based on character frequency and readability
    """
    print("=== Approach 2: Brute Force with Text Analysis ===")
    
    cipher_hex = "73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d"
    cipher_bytes = hex_to_bytes(cipher_hex)
    
    # Common English characters (including crypto flag format)
    common_chars = set("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789{}_")
    
    best_score = 0
    best_key = 0
    best_text = ""
    
    print("Analyzing all possible keys...")
    
    for key in range(256):
        decrypted = xor_single_byte(cipher_bytes, key)
        
        try:
            decrypted_text = decrypted.decode('utf-8')
            
            # Calculate score based on readable characters
            readable_chars = sum(1 for c in decrypted_text if c in common_chars)
            total_chars = len(decrypted_text)
            
            if total_chars > 0:
                score = readable_chars / total_chars
                
                # Bonus for crypto flag format
                if decrypted_text.startswith("crypto{"):
                    score += 0.5
                if decrypted_text.endswith("}"):
                    score += 0.3
                
                if score > best_score:
                    best_score = score
                    best_key = key
                    best_text = decrypted_text
                    
        except UnicodeDecodeError:
            continue
    
    print(f"Best decryption found:")
    print(f"Key: {best_key} (0x{best_key:02x})")
    print(f"Score: {best_score:.3f}")
    print(f"Text: {best_text}")
    
    return best_key, best_text, best_score

def approach_3_known_plaintext():
    """
    Approach 3: Known Plaintext Attack
    If we know the flag starts with "crypto{", we can find the key
    """
    print("=== Approach 3: Known Plaintext Attack ===")
    
    cipher_hex = "73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d"
    cipher_bytes = hex_to_bytes(cipher_hex)
    
    # We know the flag starts with "crypto{"
    known_plaintext = b"crypto{"
    
    print(f"Known plaintext: {known_plaintext}")
    print(f"Ciphertext starts with: {cipher_bytes[:7]}")
    
    # Find the key by XORing known plaintext with ciphertext
    potential_keys = []
    
    for i in range(len(cipher_bytes) - len(known_plaintext) + 1):
        # Try to find a consistent key
        key_candidates = []
        for j in range(len(known_plaintext)):
            key_candidate = cipher_bytes[i + j] ^ known_plaintext[j]
            key_candidates.append(key_candidate)
        
        # Check if all key candidates are the same (consistent key)
        if len(set(key_candidates)) == 1:
            key = key_candidates[0]
            potential_keys.append((i, key))
            print(f"Potential key {key} (0x{key:02x}) at position {i}")
    
    # Test the found keys
    for pos, key in potential_keys:
        decrypted = xor_single_byte(cipher_bytes, key)
        try:
            decrypted_text = decrypted.decode('utf-8')
            if decrypted_text.startswith("crypto{"):
                print(f"✅ Confirmed key {key} (0x{key:02x}) gives: {decrypted_text}")
                return key, decrypted_text
        except UnicodeDecodeError:
            continue
    
    return None, None

def demonstrate_single_byte_xor():
    """Demonstrate how single-byte XOR works"""
    print("=== Single-Byte XOR Demonstration ===")
    
    # Simple example
    plaintext = "Hello"
    key = 0x13
    
    print(f"Plaintext: {plaintext}")
    print(f"Key: {key} (0x{key:02x})")
    
    # Encrypt
    plaintext_bytes = plaintext.encode('utf-8')
    encrypted = xor_single_byte(plaintext_bytes, key)
    print(f"Encrypted (hex): {bytes_to_hex(encrypted)}")
    
    # Decrypt
    decrypted = xor_single_byte(encrypted, key)
    decrypted_text = decrypted.decode('utf-8')
    print(f"Decrypted: {decrypted_text}")
    
    print(f"Encryption/Decryption successful: {plaintext == decrypted_text}")
    print()

def verify_solution():
    """Verify the solution by testing the found key"""
    print("=== Solution Verification ===")
    
    # Known solution
    expected_flag = "crypto{0x10_15_my_f4v0ur173_by7e}"
    expected_key = 0x10
    
    print(f"Expected flag: {expected_flag}")
    print(f"Expected key: {expected_key} (0x{expected_key:02x})")
    
    # Test encryption/decryption
    cipher_hex = "73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d"
    cipher_bytes = hex_to_bytes(cipher_hex)
    
    # Decrypt with expected key
    decrypted = xor_single_byte(cipher_bytes, expected_key)
    decrypted_text = decrypted.decode('utf-8')
    
    print(f"Decrypted with key {expected_key}: {decrypted_text}")
    print(f"Verification successful: {decrypted_text == expected_flag}")
    
    return expected_key, expected_flag

if __name__ == "__main__":
    print("Single-Byte XOR Challenge - CryptoHack")
    print("=" * 50)
    print()
    
    # Demonstrate single-byte XOR
    demonstrate_single_byte_xor()
    
    # Try all approaches
    print("🔍 Solving the challenge...")
    print()
    
    # Approach 1: Simple brute force
    flags_approach1 = approach_1_brute_force_simple()
    print()
    
    # Approach 2: Brute force with analysis
    best_key, best_text, best_score = approach_2_brute_force_with_analysis()
    print()
    
    # Approach 3: Known plaintext attack
    key_approach3, text_approach3 = approach_3_known_plaintext()
    print()
    
    # Verify solution
    verified_key, verified_flag = verify_solution()
    print()
    
    # Summary
    print("=== Summary ===")
    if flags_approach1:
        print(f"✅ Approach 1 found {len(flags_approach1)} flag(s)")
        for key, flag in flags_approach1:
            print(f"   Key {key} (0x{key:02x}): {flag}")
    
    print(f"✅ Approach 2 best result: Key {best_key} (0x{best_key:02x}) - {best_text}")
    
    if key_approach3:
        print(f"✅ Approach 3 found key: {key_approach3} (0x{key_approach3:02x})")
    
    print(f"✅ Verified solution: Key {verified_key} (0x{verified_key:02x}) - {verified_flag}")
    
    print()
    print("🎯 Challenge Solved!")
    print(f"Flag: {verified_flag}")
    print(f"Key: {verified_key} (0x{verified_key:02x})")
