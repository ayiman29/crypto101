class ECDSA:
    def __init__(self, curve_params):
        # Initialize curve parameters (e.g., prime p, curve coefficients a, b, base point G, order n)
        pass

    def generate_keypair(self):
        # Generate a private key (random integer in [1, n-1])
        # Compute the public key as the scalar multiplication of the base point G by the private key
        pass

    def sign(self, message, private_key):
        # 1. Hash the message using a secure hash function (e.g., SHA-256)
        # 2. Generate a random per-message nonce k in [1, n-1]
        # 3. Compute the curve point R = k * G
        # 4. Calculate r = x-coordinate of R modulo n
        # 5. Compute s = k^(-1) * (hash + r * private_key) modulo n
        # 6. Return the signature (r, s)
        pass

    def verify(self, message, signature, public_key):
        # 1. Hash the message using the same hash function
        # 2. Extract r and s from the signature
        # 3. Check that r and s are in the valid range (1 to n-1)
        # 4. Compute w = s^(-1) modulo n
        # 5. Compute u1 = hash * w modulo n and u2 = r * w modulo n
        # 6. Compute the curve point X = u1 * G + u2 * public_key
        # 7. The signature is valid if r == x-coordinate of X modulo n
        pass