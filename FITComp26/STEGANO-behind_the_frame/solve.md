## Analysis

1. The challenge provides an image containing a billboard with partially hidden text.
2. Inspecting the image metadata using `exiftool` reveals a suspicious string stored in the `UserComment` field.
3. The extracted string appears to be Base64-encoded, suggesting that it contains hidden information.

## Solution

1. Examine the image metadata using:
   ```bash
   exiftool billboard.jpg
   ```
2. Locate the suspicious string in the `UserComment` field.
3. Decode the Base64 string using CyberChef or any Base64 decoder.
4. The decoded output reveals the flag.

## Flag

```text
ctffit{is_1t_tro33e_bruhhh}
```