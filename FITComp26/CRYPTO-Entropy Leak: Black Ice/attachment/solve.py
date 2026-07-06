import socket
import hashlib
import itertools
import string

def solve_pow(prefix, difficulty='0000'):
    print(f"Solving PoW for prefix: {prefix}")
    chars = string.ascii_letters + string.digits
    for length in range(1, 20):
        for nonce_tuple in itertools.product(chars, repeat=length):
            nonce = ''.join(nonce_tuple)
            hash_val = hashlib.sha256((prefix + nonce).encode()).hexdigest()
            if hash_val.startswith(difficulty):
                print(f"Found nonce: {nonce} -> {hash_val}")
                return nonce
    return None

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.settimeout(60)
s.connect(('130.94.95.128', 9005))

banner = s.recv(4096).decode()
print("Server:", banner)

# Parse the prefix from the banner
# e.g. "PoW: SHA256('6fb06451498a56ec' + nonce) starts with '0000'"
import re
match = re.search(r"SHA256\('([^']+)' \+ nonce\)", banner)
prefix = match.group(1)

nonce = solve_pow(prefix)
s.sendall((nonce + '\n').encode())

response = s.recv(4096).decode()
print("Response:", response)

# Now send the token
s.sendall(b'NLFSR_STATE_RECOVERY_TOKEN_A1F37DX4Z\n')
response2 = s.recv(4096).decode()
print("Final:", response2)

s.close()