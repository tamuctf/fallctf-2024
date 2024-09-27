# Encoding

I decided to send a message to my friend, and encoded my message to make it harder to understand! Here it is:
```
NzQgNzYgNzQgNzIgN2EgN2IgNjUgNjIgNjcgMzEgMzMgNWYgNzUgNzIgNmIgNWYgNmYgNmUgNjYgNzIgMzYgMzQgNWYgNzIgNjEgNzAgNjIgNzEgNzYgNjEgNzQgMjEgMjEgMjEgN2Q=
```
Can you figure out what message I sent?

## Hints

- This tool is helpful: https://gchq.github.io/CyberChef/

## Solution

Put the encoded text into the CyberChef link provided in the hint. By the use of magic it gives Base64 decoding then Hex. After that by applying rot13 the flag is shown.

flag:
`gigem{rot13_hex_base64_encoding!!!}`
