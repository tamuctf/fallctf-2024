# Next Prime

Author: Noam

The following prime number was given:

`7948992548489485950921349586776478634516625616506621719276263753`

What is the next prime number right after this one?

Note: https://en.wikipedia.org/wiki/Prime_number

Flag format: `gigem{<next prime>}`

## Solution

```python
from sympy import nextprime
p = 7948992548489485950921349586776478634516625616506621719276263753
print(nextprime(p))
```

flag: 
`gigem{7948992548489485950921349586776478634516625616506621719276263851}`
