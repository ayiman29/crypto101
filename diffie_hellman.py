# diffie_hellman.py

# Step 1: Define global parameters
# - Prime number (p)
# - Primitive root modulo p (g)
def define_global_parameters():
    pass  # TODO: Choose suitable values for p and g


# Step 2: Generate private key for a user
# - Choose a random private key (a secret integer)
def generate_private_key():
    pass  # TODO: Generate a secure random integer


# Step 3: Compute public key
# - Use the formula: A = g^a mod p
def compute_public_key(private_key, g, p):
    pass  # TODO: Compute and return the public key


# Step 4: Compute shared secret
# - Use the formula: s = B^a mod p (where B is the other party's public key)
def compute_shared_secret(their_public_key, own_private_key, p):
    pass  # TODO: Compute and return the shared secret


# Optional Step: Simulate key exchange between Alice and Bob
def simulate_key_exchange():
    # TODO: Set up global parameters

    # TODO: Alice generates private and public key
    # TODO: Bob generates private and public key

    # TODO: Exchange public keys

    # TODO: Both compute shared secret

    # TODO: Print or verify if both shared secrets match
    pass


if __name__ == "__main__":
    simulate_key_exchange()