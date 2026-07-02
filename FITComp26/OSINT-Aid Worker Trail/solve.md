## Analysis 

1. The challenge provides several public profiles from RelidgeHub, FieldGram, and VolunteerNet. 
2. The profiles are linked by comparing usernames, bios, and the `avatar_sha1` value. 
3. The accounts `ayu_logistics`, `convoy.ayu`, and `ap_relief2026` share the same `avatar_sha1`, indicating they belong to the same person. 
4. The bio of `ap_relief2026` contains a suspicious Base64-encoded string. 

## Solution 

1. Correlate the three profiles using the identical `avatar_sha1` value. 
2. Inspect the bio of `ap_relief2026` on VolunteerNet. 
3. Copy the Base64 string: ```text bm9kZSByZWNvdmVyeSBjb2RlIDo6IGN0ZmZpdHs0aWRfdzByazNyX3RyNDFsX2YwbGw wdzNkfQ== ``` 
4. Decode the string using a Base64 decoder. 
5. The decoded text reveals the flag. 

## Flag 
```text 
ctffit{4id_w0rk3r_tr41l_f0ll0w3d} 
```
