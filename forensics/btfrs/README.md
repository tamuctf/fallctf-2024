# BTFRS

There is a BTFRS filesystem that has the flag on it. How can you access the file?

Link:
https://drive.google.com/file/d/1-81JVhZh1_NUVbH3LV1kaPlh9z7SRpw3/view?usp=sharing

Tips:
- https://en.wikipedia.org/wiki/Btrfs
- https://en.wikipedia.org/wiki/Base64

## Solution

The first step is to set up a loop device for the image: `losetup /dev/loop1 flag.img`

The second step is to mount the loop device: `mount /dev/loop1 /tmp/lmao`

Finally the flag can be read and decoded from base64: `cat /tmp/lmao/flag.txt | base64 -d`

flag:
`gigem{c0n6r475_0n_63771n6_7h3_3x74_fl46_7y8z13}`
