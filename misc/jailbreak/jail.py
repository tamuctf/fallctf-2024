import string

code = input('Free calculator!\nNo arbitrary code execution allowed.\n>>> ')

code = ''.join([c for c in code if c in string.printable])

filter = ['eval', 'exec', 'import', 'open', 'system', 'os', 'builtins']
for f in filter:
    if f in code:
        print('No! Bad programmer!!!')
        break
print(eval(code))
