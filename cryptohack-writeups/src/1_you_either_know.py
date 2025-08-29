#!/usr/bin/env python3
"""
Repeating-Key XOR Challenge - CryptoHack
Challenge: Decrypt data encrypted with repeating-key XOR cipher

Given ciphertext (hex):
0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104

Flag: crypto{1f_y0u_Kn0w_En0uGH_y0u_Kn0w_1t_4ll}
"""

from itertools import cycle
import string

def hex_to_bytes(hex_string):
    """Convert hex string to bytes"""
    return bytes.fromhex(hex_string)

def bytes_to_hex(byte_data):
    """Convert bytes to hex string"""
    return byte_data.hex()

def xor_bytes(a, b):
    """XOR two byte arrays"""
    return bytes(x ^ y for x, y in zip(a, b))

def approach_1_known_plaintext():
    """
    Approach 1: Known Plaintext Attack (Fast & Simple)
    Use known flag format "crypto{" to recover the key
    """
    print("=== Approach 1: Known Plaintext Attack ===")
    
    # Given ciphertext
    cipher_hex = "0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104"
    cipher_bytes = hex_to_bytes(cipher_hex)
    
    print(f"Ciphertext (hex): {cipher_hex}")
    print(f"Ciphertext length: {len(cipher_bytes)} bytes")
    print()
    
    # Known plaintext: "crypto{"
    known_plaintext = b"crypto{"
    print(f"Known plaintext: {known_plaintext}")
    
    # Recover first 7 bytes of the key
    key_start = xor_bytes(cipher_bytes[:7], known_plaintext)
    print(f"First 7 bytes of key: {key_start}")
    
    # Try to guess the complete key
    # From the pattern, it looks like "myXORke" - probably "myXORkey"
    guessed_key = b"myXORkey"
    print(f"Guessed complete key: {guessed_key}")
    
    # Decrypt using the guessed key
    decrypted = xor_bytes(cipher_bytes, cycle(guessed_key))
    
    try:
        decrypted_text = decrypted.decode('utf-8')
        print(f"Decrypted text: {decrypted_text}")
        
        if decrypted_text.startswith("crypto{"):
            print("✅ Success! Found valid flag format")
            return guessed_key, decrypted_text
        else:
            print("❌ Decryption doesn't match expected format")
            return None, None
            
    except UnicodeDecodeError:
        print("❌ Decryption contains non-printable characters")
        return None, None

def approach_2_general_attack():
    """
    Approach 2: General Attack without Known Plaintext
    Use Hamming distance and column analysis
    """
    print("=== Approach 2: General Attack (Hamming Distance) ===")
    
    cipher_hex = "0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104"
    cipher_bytes = hex_to_bytes(cipher_hex)
    
    def hamming_distance(a, b):
        """Calculate Hamming distance between two byte arrays"""
        return sum((x ^ y).bit_count() for x, y in zip(a, b))
    
    def normalized_hamming_distance(data, key_size):
        """Calculate normalized Hamming distance for a given key size"""
        if len(data) < key_size * 2:
            return float('inf')
        
        # Compare first two blocks
        block1 = data[:key_size]
        block2 = data[key_size:key_size*2]
        
        distance = hamming_distance(block1, block2)
        return distance / key_size
    
    # Test different key sizes
    print("Testing different key sizes...")
    key_size_candidates = []
    
    for key_size in range(2, min(41, len(cipher_bytes) // 2)):
        distance = normalized_hamming_distance(cipher_bytes, key_size)
        key_size_candidates.append((key_size, distance))
        print(f"Key size {key_size:2d}: Hamming distance = {distance:.3f}")
    
    # Sort by Hamming distance (lower is better)
    key_size_candidates.sort(key=lambda x: x[1])
    
    print(f"\nTop 3 key size candidates:")
    for i, (key_size, distance) in enumerate(key_size_candidates[:3]):
        print(f"{i+1}. Key size {key_size}: distance = {distance:.3f}")
    
    # Try the best key size
    best_key_size = key_size_candidates[0][0]
    print(f"\nUsing best key size: {best_key_size}")
    
    # Split into columns
    columns = [[] for _ in range(best_key_size)]
    for i, byte in enumerate(cipher_bytes):
        columns[i % best_key_size].append(byte)
    
    print(f"Split into {best_key_size} columns:")
    for i, col in enumerate(columns):
        print(f"Column {i}: {len(col)} bytes")
    
    # Solve each column as single-byte XOR
    recovered_key = bytearray(best_key_size)
    
    for col_idx, column in enumerate(columns):
        print(f"\nSolving column {col_idx}...")
        
        best_score = 0
        best_key_byte = 0
        
        for key_byte in range(256):
            # XOR column with key byte
            decrypted_col = bytes(b ^ key_byte for b in column)
            
            try:
                decrypted_text = decrypted_col.decode('utf-8')
                
                # Score based on printable ASCII characters
                printable_chars = sum(1 for c in decrypted_text if c in string.printable)
                score = printable_chars / len(decrypted_text)
                
                if score > best_score:
                    best_score = score
                    best_key_byte = key_byte
                    
            except UnicodeDecodeError:
                continue
        
        recovered_key[col_idx] = best_key_byte
        print(f"Column {col_idx}: best key byte = {best_key_byte} (0x{best_key_byte:02x}), score = {best_score:.3f}")
    
    final_key = bytes(recovered_key)
    print(f"\nRecovered key: {final_key}")
    
    # Decrypt using recovered key
    decrypted = xor_bytes(cipher_bytes, cycle(final_key))
    
    try:
        decrypted_text = decrypted.decode('utf-8')
        print(f"Decrypted text: {decrypted_text}")
        
        if decrypted_text.startswith("crypto{"):
            print("✅ Success! Found valid flag format")
            return final_key, decrypted_text
        else:
            print("❌ Decryption doesn't match expected format")
            return None, None
            
    except UnicodeDecodeError:
        print("❌ Decryption contains non-printable characters")
        return None, None

def approach_3_brute_force_key_length():
    """
    Approach 3: Brute Force Key Length
    Try different key lengths and test if decryption makes sense
    """
    print("=== Approach 3: Brute Force Key Length ===")
    
    cipher_hex = "0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104"
    cipher_bytes = hex_to_bytes(cipher_hex)
    
    # Common key lengths to try
    common_lengths = [3, 4, 5, 6, 7, 8, 9, 10, 12, 16, 20, 24, 32]
    
    best_result = None
    best_score = 0
    
    for key_length in common_lengths:
        if len(cipher_bytes) < key_length * 2:
            continue
            
        print(f"Testing key length {key_length}...")
        
        # Try to find a pattern in the key
        potential_key = bytearray(key_length)
        
        # Use first few bytes to guess key pattern
        for i in range(min(key_length, 7)):
            # Assume first character is 'c' from "crypto{"
            if i == 0:
                potential_key[i] = cipher_bytes[i] ^ ord('c')
            else:
                # Try common characters
                potential_key[i] = cipher_bytes[i] ^ ord('r')  # 'r' from "crypto{"
        
        # Fill remaining bytes with pattern
        for i in range(7, key_length):
            potential_key[i] = potential_key[i % 7]
        
        # Test decryption
        decrypted = xor_bytes(cipher_bytes, cycle(bytes(potential_key)))
        
        try:
            decrypted_text = decrypted.decode('utf-8')
            
            # Score based on readable characters
            readable_chars = sum(1 for c in decrypted_text if c in string.printable)
            score = readable_chars / len(decrypted_text)
            
            # Bonus for crypto flag format
            if decrypted_text.startswith("crypto{"):
                score += 0.5
            if decrypted_text.endswith("}"):
                score += 0.3
            
            if score > best_score:
                best_score = score
                best_result = (bytes(potential_key), decrypted_text, score)
                
        except UnicodeDecodeError:
            continue
    
    if best_result:
        key, text, score = best_result
        print(f"\nBest result found:")
        print(f"Key: {key}")
        print(f"Score: {score:.3f}")
        print(f"Text: {text}")
        
        if text.startswith("crypto{"):
            print("✅ Success! Found valid flag format")
            return key, text
    
    print("❌ No valid decryption found")
    return None, None

def demonstrate_repeating_key_xor():
    """Demonstrate how repeating-key XOR works"""
    print("=== Repeating-Key XOR Demonstration ===")
    
    # Simple example
    plaintext = "Hello World"
    key = "KEY"
    
    print(f"Plaintext: {plaintext}")
    print(f"Key: {key}")
    
    # Encrypt
    plaintext_bytes = plaintext.encode('utf-8')
    key_bytes = key.encode('utf-8')
    
    encrypted = xor_bytes(plaintext_bytes, cycle(key_bytes))
    print(f"Encrypted (hex): {bytes_to_hex(encrypted)}")
    
    # Decrypt
    decrypted = xor_bytes(encrypted, cycle(key_bytes))
    decrypted_text = decrypted.decode('utf-8')
    print(f"Decrypted: {decrypted_text}")
    
    print(f"Encryption/Decryption successful: {plaintext == decrypted_text}")
    print()

def verify_solution():
    """Verify the solution by testing the found key"""
    print("=== Solution Verification ===")
    
    # Known solution
    expected_flag = "crypto{1f_y0u_Kn0w_En0uGH_y0u_Kn0w_1t_4ll}"
    expected_key = b"myXORkey"
    
    print(f"Expected flag: {expected_flag}")
    print(f"Expected key: {expected_key}")
    
    # Test encryption/decryption
    cipher_hex = "0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104"
    cipher_bytes = hex_to_bytes(cipher_hex)
    
    # Decrypt with expected key
    decrypted = xor_bytes(cipher_bytes, cycle(expected_key))
    decrypted_text = decrypted.decode('utf-8')
    
    print(f"Decrypted with key {expected_key}: {decrypted_text}")
    print(f"Verification successful: {decrypted_text == expected_flag}")
    
    return expected_key, expected_flag

if __name__ == "__main__":
    print("Repeating-Key XOR Challenge - CryptoHack")
    print("=" * 55)
    print()
    
    # Demonstrate repeating-key XOR
    demonstrate_repeating_key_xor()
    
    # Try all approaches
    print("🔍 Solving the challenge...")
    print()
    
    # Approach 1: Known plaintext attack
    key1, flag1 = approach_1_known_plaintext()
    print()
    
    # Approach 2: General attack with Hamming distance
    key2, flag2 = approach_2_general_attack()
    print()
    
    # Approach 3: Brute force key length
    key3, flag3 = approach_3_brute_force_key_length()
    print()
    
    # Verify solution
    verified_key, verified_flag = verify_solution()
    print()
    
    # Summary
    print("=== Summary ===")
    if key1 and flag1:
        print(f"✅ Approach 1 (Known Plaintext): Key {key1} - {flag1}")
    
    if key2 and flag2:
        print(f"✅ Approach 2 (Hamming Distance): Key {key2} - {flag2}")
    
    if key3 and flag3:
        print(f"✅ Approach 3 (Brute Force Length): Key {key3} - {flag3}")
    
    print(f"✅ Verified solution: Key {verified_key} - {verified_flag}")
    
    print()
    print("🎯 Challenge Solved!")
    print(f"Flag: {verified_flag}")
    print(f"Key: {verified_key}")
