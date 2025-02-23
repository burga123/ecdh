from S256Point import P, G, N
import secrets

# Assign the base point and curve point
curve = G

# Example operation on a point
# t = 6 * curve
# print(f"t: {t}")

# Generate Alice's and Bob's secrets
alice_secret = secrets.randbelow(N)
bob_secret = secrets.randbelow(N)

# Generate Bob's public key
bobpubkey = bob_secret * curve
print(f"Bob's Public Key: {hex(bobpubkey.x.element)}")

# Generate Alice's public key
alicepubkey = alice_secret * curve
print(f"Alice's Public Key: {hex(alicepubkey.x.element)}")

# Compute shared keys
aliceshkey = alice_secret * bobpubkey
bobshkey = bob_secret * alicepubkey

# Validate shared key equality
print(f"Alice's Shared Key: {hex(aliceshkey.x.element)}")
print(f"Bob's Shared Key: {hex(bobshkey.x.element)}")
print(f"Shared keys match: {bobshkey == aliceshkey}")
