## Analysis

1. The challenge involves two web vulnerabilities: **IDOR** and **SSRF**.
2. Browsing the incident list reveals that **incident 105** contains unusual information.
3. The incident references an internal URL, `http://127.0.0.1:9000/ops`, along with the message **"preview proxy can reach it"**.
4. This suggests that the `/api/preview` endpoint can be abused to access internal resources through SSRF.

## Solution

1. Open the challenge website and inspect the available API endpoints.
2. Access the incident list and view **incident 105**.
3. Copy the internal URL:
   ```
   http://127.0.0.1:9000/ops
   ```
4. Submit the URL to the preview endpoint.
5. Since the request is made by the server, it can access its own localhost service.
6. The response from the internal endpoint reveals the flag.

## Flag

```text
ctffit{cr1s1s_m4p_1d0r_t0_ssrf}
```

