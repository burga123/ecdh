# Elliptic Key Diffie-Hellman
This project implements the Elliptic Curve Diffie-Hellman (ECDH) key exchange algorithm.

## Features

- Secure key exchange using elliptic curves
- Lightweight and efficient implementation
- Compatible with various elliptic curves

## Installation

To install the project, clone the repository:

```bash
git clone https://github.com/yourusername/elliptickeydiffiehellman.git
cd elliptickeydiffiehellman
```

## Usage

Here's a basic example of how to use the ECDH implementation:

```python
from S256Point import P, G, N
import secrets

# Assign the base point and curve point
curve = G


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

```

## Contributing

Contributions are welcome! Please open an issue or submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact

For any questions or suggestions, please contact bleibin81@gmail.com .
