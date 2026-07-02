## Analysis

1. The challenge provides four QR codes, each containing a fragment of the encoded message.
2. Scanning each QR code reveals that every fragment is part of a Base64-encoded string.
3. Combining all four fragments forms a complete Base64 string.
4. Decoding the Base64 string reveals the flag.

## Solution

1. Scan all four QR codes using Google Lens or any QR code scanner.
2. Concatenate the four Base64 fragments in the correct order.
3. Decode the combined Base64 string using CyberChef or any Base64 decoder.
4. The decoded output contains the flag.

## Flag

```text
ctffit{r3l13f_m4n1f3st_qr_s0lv3d}
```