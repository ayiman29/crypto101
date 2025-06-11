class AES:
    def __init__(self, key):
        # Step 1: Initialize with the secret key
        # - Key expansion (generate round keys)
        pass

    def encrypt_block(self, plaintext_block):
        # Step 2: Encrypt a single 16-byte block
        # - Initial round key addition
        # - 9 or 11 rounds (depending on key size) of:
        #   - SubBytes (byte substitution)
        #   - ShiftRows (row shifting)
        #   - MixColumns (column mixing)
        #   - AddRoundKey (round key addition)
        # - Final round (without MixColumns)
        pass

    def decrypt_block(self, ciphertext_block):
        # Step 3: Decrypt a single 16-byte block
        # - Initial round key addition
        # - 9 or 11 rounds (depending on key size) of:
        #   - InvShiftRows
        #   - InvSubBytes
        #   - AddRoundKey
        #   - InvMixColumns
        # - Final round (without InvMixColumns)
        pass

    def encrypt(self, plaintext):
        # Step 4: Encrypt data of arbitrary length
        # - Pad plaintext to multiple of 16 bytes (PKCS7 or similar)
        # - Split into blocks
        # - Encrypt each block using encrypt_block
        # - Combine ciphertext blocks
        pass

    def decrypt(self, ciphertext):
        # Step 5: Decrypt data of arbitrary length
        # - Split ciphertext into 16-byte blocks
        # - Decrypt each block using decrypt_block
        # - Remove padding from last block
        # - Combine plaintext blocks
        pass


# Usage example (fill in later):
# key = b'your 16/24/32-byte key here'
# aes = AES(key)
# ciphertext = aes.encrypt(b'your plaintext message')
# plaintext = aes.decrypt(ciphertext)
