#!/usr/bin/env python3
"""
XOR Properties Challenge - CryptoHack
Challenge: Use XOR properties to recover the flag from encrypted data

Given:
KEY1 = a6c8b6733c9b22de7bc0253266a3867df55acde8635e19c73313
KEY2 ^ KEY1 = 37dcb292030faa90d07eec17e3b1c6d8daf94c35d4c9191a5e1e
KEY2 ^ KEY3 = c1545756687e7573db23aa1c3452a098b71a7fbf0fddddde5fc1
FLAG ^ KEY1 ^ KEY3 ^ KEY2 = 04ee9855208a2cd59091d04767ae47963170d1660df7f56f5faf

Flag: crypto{x0r_i5_ass0c1at1v3}
"""

def hex_to_bytes(hex_string):
    """Convert hex string to bytes"""
    return bytes.fromhex(hex_string)

def bytes_to_hex(byte_data):
    """Convert bytes to hex string"""
    return byte_data.hex()

def xor_bytes(a, b):
    """XOR two byte arrays"""
    return bytes(x ^ y for x, y in zip(a, b))

def approach_1_direct_simplification():
    """
    Approach 1: Direct Simplification Using XOR Properties
    
    FLAG = (FLAG ^ KEY1 ^ KEY3 ^ KEY2) ^ KEY1 ^ (KEY2 ^ KEY3)
    
    This works because:
    - KEY1 ^ KEY1 = 0 (self-inverse)
    - (KEY2 ^ KEY3) ^ (KEY2 ^ KEY3) = 0 (self-inverse)
    - What remains is just FLAG
    """
    print("=== Approach 1: Direct Simplification ===")
    
    # Given values
    key1 = hex_to_bytes("a6c8b6733c9b22de7bc0253266a3867df55acde8635e19c73313")
    key2_xor_key1 = hex_to_bytes("37dcb292030faa90d07eec17e3b1c6d8daf94c35d4c9191a5e1e")
    key2_xor_key3 = hex_to_bytes("c1545756687e7573db23aa1c3452a098b71a7fbf0fddddde5fc1")
    encrypted_flag = hex_to_bytes("04ee9855208a2cd59091d04767ae47963170d1660df7f56f5faf")
    
    print(f"KEY1: {bytes_to_hex(key1)}")
    print(f"KEY2 ^ KEY1: {bytes_to_hex(key2_xor_key1)}")
    print(f"KEY2 ^ KEY3: {bytes_to_hex(key2_xor_key3)}")
    print(f"Encrypted Flag: {bytes_to_hex(encrypted_flag)}")
    print()
    
    # Direct simplification using XOR properties
    # FLAG = encrypted_flag ^ KEY1 ^ (KEY2 ^ KEY3)
    flag = xor_bytes(encrypted_flag, key1)
    flag = xor_bytes(flag, key2_xor_key3)
    
    print("Calculation:")
    print("1. FLAG = encrypted_flag ^ KEY1")
    print(f"   = {bytes_to_hex(encrypted_flag)} ^ {bytes_to_hex(key1)}")
    print(f"   = {bytes_to_hex(xor_bytes(encrypted_flag, key1))}")
    print()
    print("2. FLAG = result ^ (KEY2 ^ KEY3)")
    print(f"   = {bytes_to_hex(xor_bytes(encrypted_flag, key1))} ^ {bytes_to_hex(key2_xor_key3)}")
    print(f"   = {bytes_to_hex(flag)}")
    print()
    
    try:
        flag_text = flag.decode('utf-8')
        print(f"Decoded Flag: {flag_text}")
        return flag_text
    except UnicodeDecodeError:
        print(f"Flag (hex): {bytes_to_hex(flag)}")
        return bytes_to_hex(flag)

def approach_2_step_by_step_key_recovery():
    """
    Approach 2: Step-by-Step Key Recovery
    
    1. Recover KEY2 from KEY2 ^ KEY1
    2. Recover KEY3 from KEY2 ^ KEY3
    3. Use all keys to decrypt the flag
    """
    print("=== Approach 2: Step-by-Step Key Recovery ===")
    
    # Given values
    key1 = hex_to_bytes("a6c8b6733c9b22de7bc0253266a3867df55acde8635e19c73313")
    key2_xor_key1 = hex_to_bytes("37dcb292030faa90d07eec17e3b1c6d8daf94c35d4c9191a5e1e")
    key2_xor_key3 = hex_to_bytes("c1545756687e7573db23aa1c3452a098b71a7fbf0fddddde5fc1")
    encrypted_flag = hex_to_bytes("04ee9855208a2cd59091d04767ae47963170d1660df7f56f5faf")
    
    print("Step 1: Recover KEY2")
    print(f"KEY2 ^ KEY1 = {bytes_to_hex(key2_xor_key1)}")
    print(f"KEY1 = {bytes_to_hex(key1)}")
    key2 = xor_bytes(key2_xor_key1, key1)
    print(f"KEY2 = (KEY2 ^ KEY1) ^ KEY1 = {bytes_to_hex(key2)}")
    print()
    
    print("Step 2: Recover KEY3")
    print(f"KEY2 ^ KEY3 = {bytes_to_hex(key2_xor_key3)}")
    print(f"KEY2 = {bytes_to_hex(key2)}")
    key3 = xor_bytes(key2_xor_key3, key2)
    print(f"KEY3 = (KEY2 ^ KEY3) ^ KEY2 = {bytes_to_hex(key3)}")
    print()
    
    print("Step 3: Decrypt the flag")
    print(f"Encrypted Flag = {bytes_to_hex(encrypted_flag)}")
    print(f"FLAG = encrypted_flag ^ KEY1 ^ KEY3 ^ KEY2")
    
    # Decrypt using all keys
    flag = xor_bytes(encrypted_flag, key1)
    flag = xor_bytes(flag, key3)
    flag = xor_bytes(flag, key2)
    
    print(f"FLAG = {bytes_to_hex(flag)}")
    print()
    
    try:
        flag_text = flag.decode('utf-8')
        print(f"Decoded Flag: {flag_text}")
        return flag_text
    except UnicodeDecodeError:
        print(f"Flag (hex): {bytes_to_hex(flag)}")
        return bytes_to_hex(flag)

def verify_solution():
    """Verify that both approaches give the same result"""
    print("=== Verification ===")
    
    flag1 = approach_1_direct_simplification()
    print()
    flag2 = approach_2_step_by_step_key_recovery()
    print()
    
    if flag1 == flag2:
        print("✅ Both approaches give the same result!")
        print(f"Final Flag: crypto{{{flag1}}}")
    else:
        print("❌ Approaches give different results!")
        print(f"Approach 1: {flag1}")
        print(f"Approach 2: {flag2}")
    
    return flag1

def demonstrate_xor_properties():
    """Demonstrate the XOR properties used in the solution"""
    print("=== XOR Properties Demonstration ===")
    
    # Test data
    a = 0b1010  # 10
    b = 0b1100  # 12
    c = 0b0110  # 6
    
    print("XOR Properties:")
    print(f"a = {a} (binary: {a:04b})")
    print(f"b = {b} (binary: {b:04b})")
    print(f"c = {c} (binary: {c:04b})")
    print()
    
    # Commutative: a ^ b = b ^ a
    print("1. Commutative: a ^ b = b ^ a")
    print(f"   {a} ^ {b} = {a ^ b} (binary: {(a ^ b):04b})")
    print(f"   {b} ^ {a} = {b ^ a} (binary: {(b ^ a):04b})")
    print(f"   Commutative: {a ^ b == b ^ a}")
    print()
    
    # Associative: (a ^ b) ^ c = a ^ (b ^ c)
    print("2. Associative: (a ^ b) ^ c = a ^ (b ^ c)")
    print(f"   ({a} ^ {b}) ^ {c} = {a ^ b} ^ {c} = {(a ^ b) ^ c}")
    print(f"   {a} ^ ({b} ^ {c}) = {a} ^ {b ^ c} = {a ^ (b ^ c)}")
    print(f"   Associative: {(a ^ b) ^ c == a ^ (b ^ c)}")
    print()
    
    # Self-inverse: a ^ a = 0
    print("3. Self-inverse: a ^ a = 0")
    print(f"   {a} ^ {a} = {a ^ a}")
    print(f"   Self-inverse: {a ^ a == 0}")
    print()
    
    # Identity: a ^ 0 = a
    print("4. Identity: a ^ 0 = a")
    print(f"   {a} ^ 0 = {a ^ 0}")
    print(f"   Identity: {a ^ 0 == a}")

if __name__ == "__main__":
    print("XOR Properties Challenge - CryptoHack")
    print("=" * 50)
    print()
    
    # Demonstrate XOR properties first
    demonstrate_xor_properties()
    print()
    
    # Solve the challenge using both approaches
    final_flag = verify_solution()
    print()
    print("🎯 Challenge Solved!")
    print(f"Flag: {{final_flag}}")
