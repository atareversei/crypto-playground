# Module 1 — Stream Ciphers

Educational implementations and attacks based on Module 1 of Dan Boneh's Stanford Cryptography course.

## Contents

- **OTP:**
  - `otp.c` — One-Time Pad implementation at the byte level.
  - `otp_reuse_attack.py` — Demonstrates breaking OTP if key is reused.
- **PRG:**
  - `prg.go` — Simple PRG using AES-CTR.
- **CTR:**
  - `ctr.go` — CTR mode encryption/decryption.
  - `ctr_iv_reuse_attack.py` — Attack on CTR mode with IV reuse.
- **WEP:**
  - `wep_attack_simulation.py` — Simplified WEP IV collision exploit.

## Learning Goals

- Understand why OTP is perfectly secure if used correctly.
- See how PRGs turn short keys into long key streams.
- Learn CTR mode and why IV uniqueness matters.
- Connect real-world crypto failures (WEP) to the theory.

## Disclaimer

> [!WARNING]
> These implementations are for educational purposes only and are **not secure** for real use.

## References

- Dan Boneh, "Cryptography I", Stanford University, Module 1
- [https://en.wikipedia.org/wiki/Stream_cipher](https://en.wikipedia.org/wiki/Stream_cipher)
