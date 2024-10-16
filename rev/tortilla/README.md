# TortillaBlockchainBitcoinMinerThreeThousand

Author: Alex

I downloaded this funny-looking game that was created with Pygame and then packaged with PyInstaller. However, sometimes when I'm playing, it seems to lag! Can you figure out what's going on?

## Dev Notes

Windows exe, please let me know if anything like audio or playing experience needs to be adjusted.

## Solution

The first step is to run `pyinstxtractor` on the exe to get out all of the packaged files. Then strings can be run on `game.pyc` to see a long base 64 string which decodes to the following:

```python
**u=os.urandom;s=__import__('hashlib').sha256
if u(1)[0]&1:
    while True:
        b=u(16)
        if (w:=s(b).hexdigest())[:5]=='00000':
            r=random.Random();r.seed(w[:4])
            f=[106,249,63,146,69,98,115,160,251,217,159,16,21,80,242,49,194,5,133,181,161,213,6,145,172,9,105,215,140,244,134,65,220,89,6,195,133,238,214,116,51,215,166,162,80,3,123,79,71,131,23,194,251,26,62,89,148,153,92]
            e=[]
            for i in range(len(f)):
                e.append(f[i]^r.randint(0,255))
            print(w,bytes(e),s(bytes(e)).hexdigest())
            os.system("start /wait cmd /c exit")
            break**
```

The code can then be rewritten to automatically print the flag:

```python
import random

r = random.Random()
r.seed('0000')

f = [106,249,63,146,69,98,115,160,251,217,159,16,21,80,242,49,194,5,133,181,161,213,6,145,172,9,105,215,140,244,134,65,220,89,6,195,133,238,214,116,51,215,166,162,80,3,123,79,71,131,23,194,251,26,62,89,148,153,92]

for i in range(len(f)):
    print(chr(f[i] ^ r.randint(0,255)), end="")

print()
```

flag:
`gigem{me_when_the_command_prompt_flashes_for_a_millisecond}`
