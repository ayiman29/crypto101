# rsa.py
from sympy import isprime, nextprime
"""
RSA Algorithm Implementation (Crypto101)

This file implements:
1. Key generation
2. Encryption
3. Decryption
"""

# Import necessary libraries
# (you might use 'random', 'math', or 'sympy' for prime generation)

# Utility functions
# - gcd(a, b)
# - modinv(a, m)
# - is_prime(n)  (optional for prime testing)

# Key Generation
def generate_keypair(bit_length):
    """
    Generate RSA key pair of given bit length.
    Returns (public_key, private_key).
    Each key is a tuple (exponent, n).
    """
    # 1. Choose two large primes p and q
    # 2. Compute n = p * q
    # 3. Compute phi(n) = (p-1)*(q-1)
    # 4. Choose e such that gcd(e, phi(n)) == 1
    # 5. Compute d ≡ e⁻¹ mod phi(n)
    # 6. Return (e, n), (d, n)
    pass

# Encryption
def encrypt(message, public_key):
    """
    Encrypt an integer message with the public key.
    Returns ciphertext.
    """
    # c = m^e mod n
    pass

# Decryption
def decrypt(ciphertext, private_key):
    """
    Decrypt an integer ciphertext with the private key.
    Returns original message.
    """
    # m = c^d mod n
    pass

# Example usage
if __name__ == "__main__":
    # 1. Generate keys
    # 2. Pick a message (as an integer)
    # 3. Encrypt it
    # 4. Decrypt it
    # 5. Print results
    pass