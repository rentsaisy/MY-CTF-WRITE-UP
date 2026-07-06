import json
import re
from math import isqrt
from Crypto.Util.number import long_to_bytes

import os
script_dir = os.path.dirname(os.path.abspath(__file__))
with open(os.path.join(script_dir, "chall.txt"), "r") as f:
    raw = f.read()

# chall.txt pakai format JSON tapi ada trailing comma, jadi dibersihkan dulu
raw = re.sub(r",\s*}", "}", raw)
data = json.loads(raw)

n = int(data["n"], 16)
e = int(data["e"])
c = int(data["c"], 16)

print(f"[*] Loaded from chall.txt")
print(f"[*] n = {hex(n)[:30]}...")
print(f"[*] e = {e}")

# Fermat Factorization
a = isqrt(n)
if a * a < n:
    a += 1

while True:
    b2 = a * a - n
    b = isqrt(b2)
    if b * b == b2:
        p, q = a - b, a + b
        break
    a += 1

print(f"\n[+] p = {p}")
print(f"[+] q = {q}")

phi = (p - 1) * (q - 1)
d = pow(e, -1, phi)
m = pow(c, d, n)
print(f"\n[+] Flag: {long_to_bytes(m).decode()}")