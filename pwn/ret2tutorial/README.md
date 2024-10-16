# Ret2Tutorial

Author: Victor

Baby's first pwn challenge!

## Solution

For this challenge, the questions that are a part of the challenge help with understanding how to exploit the given binary.

When looking at the source code, we can see that the buffer for variable `message[]` is 32 bytes long, but `gets()` is called for input, allowing for an unlimited amount of bytes to be entered into the variable, leading to buffer overflow. 

Since the variable size is 32 bytes, we need to enter 40 bytes (32 for `message[]` and another 8 for the RBP register) in order to then overwrite RSP (stack pointer register), which is loaded into RIP (instruction pointer register) whenever the 'ret' instruction is called at the end of a function. Since RIP determines which instructions to execute next, we can overwrite RSP (which is after 40 bytes) with the address for the `win()` function, which will then allow us to execute the `win()` function when `ret` is called at the end of main, giving us the flag. 

We find the address for the `win()` function using GDB with command `info functions` to find the address that the win function starts at. We then send a payload with 40 characters, followed by this address. A solve for this challenge is in `solve.py`. 

flag:
`gigem{b3g1n_pwn1ng_n00bs}`
