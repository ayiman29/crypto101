# sha256.py

"""
SHA-256 Hash Function Implementation (Skeleton)

This module implements the SHA-256 cryptographic hash function.
You will fill in the actual algorithm steps.
"""

import struct

# Constants (first 32 bits of the fractional parts of the cube roots of the first 64 primes)
K = [
    # 64 constants here (fill in yourself)
]

def right_rotate(value, bits):
    """
    Right rotate a 32-bit integer value by a given number of bits.
    """
    # Implement bit rotation
    pass

def sha256_pad(message_bytes):
    """
    Pad the input message_bytes according to SHA-256 specification.
    Returns the padded byte array.
    """
    # Implement padding: append '1' bit, then '0's, then length in bits
    pass

def sha256_parse_blocks(padded_message):
    """
    Parse the padded message into 512-bit (64-byte) blocks.
    Returns a list of byte blocks.
    """
    # Split into 64-byte chunks
    pass

def sha256_compress(block, h):
    """
    Perform the SHA-256 compression function on a single 512-bit block.

    Parameters:
    - block: bytes, 64 bytes representing one block
    - h: list of 8 integers, current hash state

    Returns:
    - list of 8 integers, updated hash state
    """
    # Implement message schedule, main loop, and state update
    pass

def sha256(message):
    """
    Compute the SHA-256 hash of the input message (string or bytes).

    Parameters:
    - message: str or bytes

    Returns:
    - hex string of the digest (64 hex characters)
    """
    # 1. Convert input to bytes if needed
    # 2. Pad the message
    # 3. Parse into blocks
    # 4. Initialize hash values
    # 5. Process each block with compress function
    # 6. Produce final digest as hex string
    pass

if __name__ == "__main__":
    test_message = "abc"
    digest = sha256(test_message)
    print(f"SHA-256('{test_message}') = {digest}")