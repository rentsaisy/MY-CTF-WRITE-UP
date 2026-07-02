## Analysis

1. The challenge provides the RSA public key components: `n`, `e`, and the ciphertext `c`.
2. The clue **"generated in a rush"** suggests that the prime numbers `p` and `q` are very close to each other.
3. When the RSA primes are close, **Fermat Factorization** can be used to recover `p` and `q`.
4. Once the factors are recovered, the private key can be reconstructed to decrypt the ciphertext.

## Solution

1. Install the required dependency:
   ```bash
   pip install pycryptodome
   ```
2. Run the provided Python script to factorize `n` using Fermat's method.
3. Recover the private exponent `d` from the computed values of `p` and `q`.
4. Decrypt the ciphertext using the recovered private key.
5. The decrypted plaintext reveals the flag.

## Flag

```text
ctffit{f3rm4t_f4ct0r1z4t10n_wh3n_pr1m3s_4r3_t00_cl0s3_t0g3th3r}
```