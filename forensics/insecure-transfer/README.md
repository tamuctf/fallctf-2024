# Insecure Transfer

Author: Noam

An employee named Kevin Lewis sent a file through the unsecured File Transfer Protocol (FTP) and the network traffic was captured. Can you figure out Kevin Lewis’s gmail password?

Flag format: `gigem{password}`

Notes:
- https://www.wireshark.org/
- https://en.wikipedia.org/wiki/File_Transfer_Protocol
- https://en.wikipedia.org/wiki/Password_cracking

## Solution

The first step to solving this challenge is to open the packet capture in wireshark. Looking at all the FTP traffic, an anonymous login is made and then a file is uploaded. The file can be extracted using `File > Export Objects > FTP-DATA`. After extracting the file we can search it for `lewis` which returns two emails. The correct email is `k.lewis@gmail.com` because the user we are looking for has the first name `Kevin`. The final step is to crack the password hash, and I used `crackstation.net` to do so. Cracking the password provides us with `apasswordnoonewilleverfigureout`.

flag: `gigem{apasswordnoonewilleverfigureout}`
