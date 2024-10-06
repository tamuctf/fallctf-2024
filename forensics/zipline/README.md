# Zipline

I've hidden my secret flag in this zip file. Can you find it?

## Solution

First by runnig `tar -xvf flag.tar.gz` the files can be retreived. When asked to replace flag.txt the "y" option was chosen each time. After this there were 4 directories a, b, c, and d as well as flag.txt file. Then used `grep -R gigem` to recurisvly search for any mention of gigem from the current location. Four fake flags were shown and the real flag stored in the d directory. Output of the command:

```
c/flag.txt:gigem{fake_flag}
a/flag.txt:gigem{fake_flag}
d/flag.txt:gigem{t00_many_l4y3rs_deep}
b/flag.txt:gigem{fake_flag}
flag.txt:gigem{another_fake_flag}
```

flag:
`gigem{t00_many_l4y3rs_deep}`
