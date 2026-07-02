## Analysis

1. The challenge uses a **Linear Congruential Generator (LCG)** to generate rolling authentication codes.
2. The provided firmware reveals the LCG formula, while the log contains the generated values with some corrupted entries.
3. By analyzing the valid sequence, the LCG parameters (`a`, `c`, and `m`) can be recovered.
4. Once the parameters are known, the next authentication code can be predicted and used to authenticate with the server.

## Solution

1. Inspect `firmware_leak.py` to identify the LCG algorithm and the modulus hint.
2. Extract the valid sequence from the `GHOST-PULSE-07` section in `handshake.log`.
3. Recover the LCG parameters (`a`, `c`, and `m`) from the sequence.
4. Use the recovered parameters to predict the next rolling code.
5. Connect to the server, solve the Proof-of-Work challenge, and submit the predicted code.
6. The server accepts the code and returns the flag.

## Flag

```text
ctffit{GH0ST_PULS3_SYNC_2024}
```