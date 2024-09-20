# Planet Earth Revolves Leisurely

"What beauty. I saw clouds and their light shadows on the distant dear earth.... The water looked like darkish, slightly gleaming spots.... When I watched the horizon, I saw the abrupt, contrasting transition from the earth's light-colored surface to the absolutely black sky. I enjoyed the rich color spectrum of the earth. It is surrounded by a light blue aureole that gradually darkens, becoming turquiose, dark blue, violet, and finally coal black." - Yuri Gagarin

## Hints

## Dev Notes

## Solution

We're only given the `planet` file, which appears to be obfuscated Perl code in the shape of multiple Earths. 

At the top, there is
```perl
eval eval '"'.
...
<planets below>
...
```

It is evaling the result of an eval, so let's change the outer eval to a print
```perl
print eval '"'.
...
<planets below>
...
```

Running this,  `perl planet_edited`, we get the actual source code
```perl
$/=$ARGV[0];
@_=("51.01",'52.01',"51.01",'50.01',"44.01",'90.11',"82.7",'50.01',"91.8",'28.01',"86.01",'00.7',"24.7",'00.11',"57.9",'09.9',"00.11",'57.9',"45.01",'53.7',"27.01",'91.8',"28.01",'12.7',"52.01",'24.7',"00.11",'57.9',"45.8",'82.7',"57.9",'53.7',"86.01",'41.7',"12.7",'77.01',"81.11");
@__=map{~~reverse sprintf("%.2f",sqrt(unpack('C')))}$/=~m[.]gs;
sub i{print "Incorrect\n";exit}
for($i=0;$i<~~@_;++$i){i if($__[$i]ne$_[$i])}
i if(~~@_!=~~@__);
print "Correct\n";
```

We can reverse the logic and recover the flag:
```python
enc = ("51.01",'52.01',"51.01",'50.01',"44.01",'90.11',"82.7",'50.01',"91.8",'28.01',"86.01",'00.7',"24.7",'00.11',"57.9",'09.9',"00.11",'57.9',"45.01",'53.7',"27.01",'91.8',"28.01",'12.7',"52.01",'24.7',"00.11",'57.9',"45.8",'82.7',"57.9",'53.7',"86.01",'41.7',"12.7",'77.01',"81.11")

dec = ''

for e in enc:
    e = float(e[::-1])**2
    dec += chr(round(e))

print(dec) # gigem{5eCur17y_by_o6sCu4i7y_I5_6r34t}
```


flag:
`gigem{5eCur17y_by_o6sCu4i7y_I5_6r34t}`
