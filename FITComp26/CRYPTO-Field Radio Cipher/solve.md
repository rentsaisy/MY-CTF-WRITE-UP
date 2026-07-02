## Analysis

1. The challenge contains two encrypted channels labeled **ROTATED** and **KEYED**.
2. The **ROTATED** channel indicates a Caesar (ROT) cipher, while the **KEYED** channel uses a Vigenère cipher.
3. The first channel must be decrypted first to obtain the keyword required for the second channel.

## Solution

1. Brute-force the Caesar cipher by trying all 25 possible shifts.
2. The correct plaintext is obtained with **ROT-16**, revealing the keyword **SHELTER**.
3. Use **SHELTER** as the Vigenère key to decrypt the second channel.
4. The decrypted message contains the flag.

## Flag

```text
ctffit{f13ld_r4d10_k33ps_4id_fl0w1ng}
```