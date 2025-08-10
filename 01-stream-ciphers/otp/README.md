# One-Time Pad (OTP)

Educational implementation of the One-Time Pad cipher and a demonstration of why reusing a key is insecure.

## Files

- **otp.c** — OTP encryption/decryption.
- **otp_reuse_attack.py** — Key reuse attack.

## Usage (C)

```bash
gcc otp.c -o otp
./otp e plaintext.txt key.txt ciphertext.bin
./otp d ciphertext.bin key.txt decrypted.txt
```

## Attack Demo (Python)

```bash
python otp_reuse_attack.py
```

## Learning Goals

- OTP provides perfect secrecy _only_ if key is random, as long as the message, and never reused.
- Reusing the key leaks XOR of plaintexts, enabling recovery with partial knowledge.

## Disclaimer

> [!WARNING]
> Not for production use.
