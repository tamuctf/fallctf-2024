# SecretPrime

Author: Alex

There's no way you can decrypt anything without the secret prime!

## Dev Notes

N/A

## Solution

```python
from Crypto.Util.number import bytes_to_long, long_to_bytes
from math import gcd
from pwn import *

context.log_level = "debug"
io = remote("127.0.0.1", 1337, ssl=False)
#io = remote("ctf.cybr.club", 443, ssl=True, sni="secretprime")

def encrypt(m):
    io.send(b"1\n" + long_to_bytes(m) + b"\n")
    io.recvuntil("Encrypted message: ")
    enc_hex = io.readline().strip()
    return bytes_to_long(bytes.fromhex(enc_hex.decode()))

def get_flag():
    io.send(b"2\n")
    io.recvuntil("Encrypted flag: ")
    enc_flag = io.readline().strip()
    return bytes_to_long(bytes.fromhex(enc_flag.decode()))

# Find key by choosing m as 1, which multiplies the key by 1
k = encrypt(1)
print("key:", k)

# Find prime by getting the greatest common divisor of two encrypted numbers
# before and after the modulus by the prime
i = 1
res1 = 0
res2 = k
while res2 > res1:
    i += 1
    res1 = res2
    res2 = encrypt(i)

p = gcd(i * k - res2, (i - 1) * k - res1)
print("prime:", p)

# Get the encrypted flag now, can't encrypt anything else after fetching the
# flag since the connection is closed
enc_flag = get_flag()
print("encrypted flag:", enc_flag)

# The flag will can be found by taking the inverse of the key and multiplying
# by the encrypted flag:
# c = (m * k) (mod p)
# c / k = m (mod p)
# c * k^(-1) = m (mod p)
key_inv = pow(k, -1, mod=p)
flag = key_inv * enc_flag % p

print(long_to_bytes(flag))
```

flag:
`gigem{n0t_50_s3cr3t_4ft3r_4ll}`
