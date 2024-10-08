# ROP 2

I added function arguments to make it harder to get the flag! Fortunately, ROP gadgets can be used to control function arguments.

## Solution

The source code provides us with some nice gadgets (`pop rdi`, `pop rsi`, `pop rdx`). These can be used to force the binary to call `set_admin()` and `win()`. For `win` to work, `admin` needs to be set to `1`. To set `admin` to the correct value, `set_admin` must be called with the correct parameters. It is possible to set the parameters by using the `rdi`, `rsi`, and `rdx` gadgets. The script I used to perform this attack can be found in [solve.py](./solve.py)


flag:
`gigem{rop_gadgets_follow_calling_convention}`
