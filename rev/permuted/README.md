# Permuted

Hey, what are some other synonyms for scrambled?

## Dev Notes

Run `make extract` to get the binary.

## Solution

Based on the c file here is a short python script to get the orginal flag:

```
def main():
    shuffled = [
        '_', 'b', 'm', '_', '4', 'A', 'd', 'g', 'e', 'a', 'g', '1', '4', 'g', 'm', 'g',
        'c', 'n', '3', 'r', 'a', '}', 'i', 'n', 'l', '_', '4', 'n', '{', '1', 'd', 's'
    ]
    perm1 = [8, 20, 26, 28, 31, 11, 7, 0, 25, 30, 22, 3, 16, 5, 4, 1, 18, 19, 13, 6, 10, 2, 24, 27, 17, 23, 9, 15, 14, 29, 21, 12]
    perm2 = [17, 27, 31, 29, 10, 0, 8, 14, 15, 26, 18, 22, 6, 13, 5, 23, 9, 12, 7, 30, 11, 24, 2, 21, 1, 3, 4, 20, 25, 19, 28, 16]

    flag = [''] * 33

    for i in range(32):
        flag[perm2[perm1[i]]] = shuffled[i]

    print("Flag:", ''.join(flag[:-1]))

if __name__ == "__main__":
    main()
```

flag:
`gigem{scr4mbl3d_4ga1n_And_4ga1n}`
