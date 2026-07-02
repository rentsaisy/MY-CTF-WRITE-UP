## Analysis

1. The challenge provides a ciphertext, a leaked plaintext prefix, and the cipher specification.
2. From `cipher_spec.py`, it is identified that the encryption uses a **36-bit NLFSR**.
3. The known plaintext in `leak.txt` allows recovery of the initial keystream by XORing it with the ciphertext.
4. The recovered keystream is sufficient to reconstruct the NLFSR state and decrypt the remaining ciphertext.

## Solution

1. Read `cipher_spec.py` to understand how the NLFSR generates the keystream.
2. XOR the known plaintext from `leak.txt` with the ciphertext to recover the initial keystream.
3. Reconstruct the NLFSR seed from the recovered keystream.
4. Generate the full keystream and decrypt the ciphertext.
5. Submit the recovered token to the server after solving the Proof-of-Work challenge.
6. The server returns the flag.

## Flag

```text
ctffit{NLFSR_ST4T3_R3C0V3RY_Z3_2024}
```