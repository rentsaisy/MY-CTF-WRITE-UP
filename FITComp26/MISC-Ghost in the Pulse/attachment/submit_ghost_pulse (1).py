import socket
import re
import hashlib
import itertools
import time

HOST = "130.94.95.128"
PORT = 9001
PREDICTED_CODE = 644499136

POW_RE = re.compile(r"SHA256\('([0-9a-fA-F]+)'\s*\+\s*nonce\)\s*starts with\s*'([0-9a-fA-F]+)'")


def recv_until_idle(sock, idle_timeout=1.0, max_wait=10.0):
    """Read from socket until no new data arrives for idle_timeout seconds."""
    sock.settimeout(idle_timeout)
    chunks = []
    start = time.time()
    while time.time() - start < max_wait:
        try:
            data = sock.recv(4096)
            if not data:
                break
            chunks.append(data)
        except socket.timeout:
            break
    return b"".join(chunks)


def solve_pow(prefix: str, target_prefix: str) -> str:
    target_len = len(target_prefix)
    for n in itertools.count():
        nonce = str(n)
        h = hashlib.sha256((prefix + nonce).encode()).hexdigest()
        if h[:target_len] == target_prefix:
            return nonce


def main():
    with socket.create_connection((HOST, PORT), timeout=10) as s:
        banner = recv_until_idle(s)
        text = banner.decode(errors="replace")
        print(text, end="")

        m = POW_RE.search(text)
        if not m:
            print("\n[!] Could not find PoW challenge in banner. Aborting.")
            return

        prefix, target_prefix = m.group(1), m.group(2)
        print(f"\n[*] Solving PoW: SHA256('{prefix}' + nonce) startswith '{target_prefix}' ...")
        nonce = solve_pow(prefix, target_prefix)
        print(f"[*] Found nonce: {nonce}")

        s.sendall((nonce + "\n").encode())

        resp = recv_until_idle(s)
        resp_text = resp.decode(errors="replace")
        print(resp_text, end="")

        if "FAILED" in resp_text.upper():
            print("\n[!] PoW rejected by server.")
            return

        # Send the predicted rolling code next
        print(f"\n[*] Submitting predicted code: {PREDICTED_CODE}")
        s.sendall((str(PREDICTED_CODE) + "\n").encode())

        final = recv_until_idle(s, idle_timeout=2.0, max_wait=15.0)
        print(final.decode(errors="replace"), end="")


if __name__ == "__main__":
    main()
