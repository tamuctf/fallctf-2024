# ETAM Woes

I finished this encryption lab for ENGR 102, but I forgot what my original message was. Can you help me recover it?

All I have is this output:
```
Your encrypted message is: 4775582d597954741376664713745c74587a6e54233d576c3d7c556c6c3d686c5641616c65405471525d4c815b3d618a
```

## Hints

- ENGR 102 is a great class. 

## Solution

In the encrypter.py python file there is a commented portion of code for the decrypt function. By removing the comment and using the function by chaning encrypt(line) to decrypt(line) the decrypt function could now be used. Then by putting in the encrypted message string to the python program the flag is shown.

flag:
`gigem{G00d_Job_y0u_c4n_r3ad_PYth0n}`
