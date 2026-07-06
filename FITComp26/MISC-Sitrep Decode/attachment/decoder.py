import binascii, base64, codecs

with open("sitrep_burst.txt", "r") as f:
    hex_str = f.read().strip()

layer1 = bytes.fromhex(hex_str).decode('ascii')
print("[+] Layer 1 (hex decoded):", layer1)

layer2 = codecs.decode(layer1, 'rot_13')
print("[+] Layer 2 (ROT13 decoded):", layer2)

layer3 = base64.b64decode(layer2).decode('utf-8')
print("[+] Layer 3 (base64 decoded):", layer3)

# Extract flag
for line in layer3.splitlines():
    if "flag" in line.lower():
        flag = line.split(":")[-1].strip()
        print("\nflag :", flag)