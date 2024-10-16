# BTFRS

Author: Noam

There is a BTFRS filesystem that has the flag on it. How can you access the file?

Link: https://drive.google.com/file/d/1igLGc1efsKWsJD2-gpM_YBn6mI97iHZo/view?usp=sharing

Note: https://en.wikipedia.org/wiki/Btrfs

## Solution

The first step is to set up a loop device for the image: `losetup /dev/loop1 flag.img`

The second step is to mount the loop device: `mount /dev/loop1 /tmp/lmao`

Finally the flag can be read from `file.png` in `/tmp/lmao`

flag:
`gigem{mounted_btfrs_image_klsa71}`
