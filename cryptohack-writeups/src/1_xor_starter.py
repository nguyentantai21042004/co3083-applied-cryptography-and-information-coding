#!/usr/bin/env python3
"""
XOR Starter - CryptoHack Challenge
Challenge: XOR each character in the string 'label' with integer 13
"""

def xor_with_13():
    """
    XOR each character in the string 'label' with integer 13
    Returns the flag in the format crypto{result}
    """
    # The given string
    label = "label"
    
    # XOR each character with 13
    result = ""
    for char in label:
        # Convert character to Unicode integer, XOR with 13, then back to character
        xor_result = ord(char) ^ 13
        result += chr(xor_result)
    
    print(f"Original string: {label}")
    print(f"XOR result: {result}")
    print(f"Flag: crypto{{{result}}}")
    
    return result

def xor_with_pwntools():
    """
    Alternative solution using pwntools library
    """
    try:
        from pwn import xor
        
        label = b"label"
        result = xor(label, 13)
        print(f"\nUsing pwntools:")
        print(f"Original: {label}")
        print(f"XOR with 13: {result}")
        print(f"Flag: crypto{{{result.decode()}}}")
        
    except ImportError:
        print("\npwntools not available. Using manual implementation.")

def manual_xor_implementation():
    """
    Manual XOR implementation to understand the process
    """
    print("\n=== Manual XOR Implementation ===")
    
    label = "label"
    print("Character | ASCII | Binary | XOR with 13 | Result")
    print("-" * 50)
    
    for char in label:
        ascii_val = ord(char)
        binary = format(ascii_val, '08b')
        xor_val = ascii_val ^ 13
        xor_binary = format(xor_val, '08b')
        result_char = chr(xor_val)
        
        print(f"    {char}     |  {ascii_val:3d}   | {binary} | {xor_val:3d} ({xor_binary}) |   {result_char}")

if __name__ == "__main__":
    print("=== XOR Starter Challenge Solution ===\n")
    
    # Main solution
    result = xor_with_13()
    
    # Alternative solutions
    xor_with_pwntools()
    manual_xor_implementation()
    
    print(f"\n🎯 Final Answer: crypto{{{result}}}")

