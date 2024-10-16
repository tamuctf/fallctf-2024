# Polybius

Author: Noam

A sequence of numbers were found, but we can't make sense of it:

`2532252335111241254415141314313213321314312325442323331423342325441542315424341525`

What is the message?

Notes
- https://en.wikipedia.org/wiki/Polybius#Cryptography
- The first five charaters after decryption should be `GIGEM`, then the message.

Flag format: `gigem{message}`

## Solution

Used dCode polybius-cipher and used the automatic decryption.
Got GIGEMCONGRATSTHISISTHEGREEKTELEGRAPHYFLAG

flag:
`gigem{GIGEMCONGRATSTHISISTHEGREEKTELEGRAPHYFLAG}`
