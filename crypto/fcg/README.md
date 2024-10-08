# FCG

Linear Congruential Generators are too weak so mine flips back and forth. Surely that's secure, right?

Note: Flag format is `gigem{}`

## Solution

LCGs are known to be weak so this challenge adds a quirk in which the value of `a` and `c` switch on every other interation of `next`. Funnily enough, switching the values of `a` and `c` in the LCG algorithm doesn't actually make the system any more secure. In fact, to solve this challenge, the algorithm used to [crack traditional LCG](https://github.com/TomasGlgg/LCGHack/blob/master/main.py) can be used here as well. The difference here is that we can use the the algorithm on every other index in flag as shown in my solve script: [solve.py](./solve.py)

flag:
`gigem{tw0_15_b3tt3r_th4n_1_righ7?}`
