# hmac.py

def h_mac(key, message, hash_function):
    # 1. Define block size for the hash function (e.g., 64 bytes for SHA-256)
    
    # 2. If key length > block size, hash the key
    
    # 3. If key length < block size, pad the key with zeros to block size
    
    # 4. Create inner padding by XOR-ing the key with 0x36 repeated to block size
    
    # 5. Create outer padding by XOR-ing the key with 0x5c repeated to block size
    
    # 6. Compute inner hash: hash_function(inner_padding + message)
    
    # 7. Compute outer hash: hash_function(outer_padding + inner_hash)
    
    # 8. Return the final HMAC value
    pass