"""
Demonstration of the One-Time Pad (OTP) key reuse vulnerability.

This script encrypts two different plaintext messages (p1 and p2) 
with the *same* random key, which violates OTP’s perfect secrecy rule.

By XORing the two ciphertexts, the script recovers the XOR of the two plaintexts.
Knowing part of one plaintext (known_p1) allows us to recover the corresponding
part of the other plaintext (recovered_p2_start). In this example, the attacker
knows the message format and the names of the receiver and sender, so they can
recover more portions of other encrypted messages.

This highlights why reusing OTP keys is insecure and leaks information,
even if the key is truly random.
"""

import os

def xor_bytes(a, b):
  return bytes([x ^ y for x, y in zip(a, b)])

p1 = b"FROM: agent_610 TO: agent_017 MSG: Hi, How are you doing?"
p2 = b"FROM: general TO: colonel MSG: SECRET MESSAGE.           "

key = os.urandom(len(p1))

c1 = xor_bytes(p1, key)
c2 = xor_bytes(p2, key)

p1_xor_p2 = xor_bytes(c1, c2)

known_p1 = b"FROM: agent_610 TO: agent_017 MSG: "
recovered_p2_start = xor_bytes(known_p1, p1_xor_p2[:len(known_p1)])
print("Recovered p2 start:", recovered_p2_start)