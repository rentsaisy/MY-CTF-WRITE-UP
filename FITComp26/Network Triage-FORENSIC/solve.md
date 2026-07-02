## Analysis

1. The challenge provides a network capture (`Capture.pcap`) that needs to be analyzed.
2. Inspecting the capture reveals numerous DNS packets containing hexadecimal-encoded data.
3. The hexadecimal values appear to be part of the exfiltrated message and need to be reconstructed.

## Solution

1. Open the capture file in Wireshark.
2. Apply the `dns` display filter to view only DNS traffic.
3. Extract the hexadecimal data from the DNS packets.
4. Use a Python script to decode the hexadecimal string into plaintext.
5. The decoded output reveals the flag.

## Flag

```text
ctffit{ng0_n3tw0rk_3xf1l_c4ught}
```