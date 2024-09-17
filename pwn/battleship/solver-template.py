#!/usr/bin/env python3

from pwn import *

context.log_level = "debug"

exe = ELF("./battleship")
#libc = ELF("./libc.so.6")
#ld = ELF("./ld-2.28.so")

context.binary = exe

def conn():
    if args.LOCAL:
        io = process([exe.path])
        gdb.attach(io, "b main")

    else:
        io = remote("tamuctf.com", 443, ssl=True, sni="battleship")
    
    return io

io = conn()
io.interactive(prompt="")

