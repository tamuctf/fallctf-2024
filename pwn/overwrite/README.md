# Overwrite

Author: Mukund

You can control your nickname, but not your username. I think. 

## Solution

We can overwrite the `username` array since the `fgets` reads in 32 characters but the `nickname` array is only 16 characters long, so anything read in after 16 characters gets put into the `username` array.

```py
io.sendline(b'A' * 16 + b'admin\n')
print(io.recvall().decode())
```

flag:
`gigem{clobbered_username_in_stack}`
