# Next Prime

The following prime number was given:

`7948992548489485950921349586776478634516625616506621719276263753`

What is the next prime number right after this one?

Flag format: gigem{number}

Tip: https://en.wikipedia.org/wiki/Prime_number

## Solution

```python
from sympy import nextprime
p = 7948992548489485950921349586776478634516625616506621719276263753
print(nextprime(p))
```

flag: 
`gigem{7948992548489485950921349586776478634516625616506621719276263851}`
