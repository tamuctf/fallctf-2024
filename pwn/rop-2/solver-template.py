from pwn import *

context.log_level = "debug"
io = remote("ctf.cybr.club", 443, ssl=True, sni="rop-2")
io.interactive(prompt="")
