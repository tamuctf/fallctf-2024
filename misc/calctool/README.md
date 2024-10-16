# calctool

Author: Alex

Whenever you start using bigger numbers, that's when you have to pull a calculator out.

## Dev Notes

Try getting RCE to make sure read-only works but if not getting the flag is fine.

## Solution

Reading the server code, the function `sympify` is used to evaluate mathmatical equations. This function is dangerous because it uses `eval` on the backend which allows for the execution of arbitrary code. This is shown in my solve script: [solve.py](./solve.py)

flag:
`gigem{BTW_if_4ny1_j0in3d_th3_Str3am_rec3nt1y_c4lc_is_s14ng_for_calcul4t0r}`
