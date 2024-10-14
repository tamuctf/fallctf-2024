# ret2shellcode

You have a really small overflow this time! Can you execute code on the stack?

## Solution

The goal of this challenge is to successfully overwrite the stack pointer to point to shellcode we have written. 

The first step of this challenge is to parse the address of `message` which is printed out in the binary in the first printf function: "This is a valuable piece of information: \<address\>".

The next step is to create the payload. Because variable `message` can hold 80 characters and the `fgets` reads 100 characters, we can overwrite the stored instruction pointer. As such, we can first write the shellcode, and then add a random character in order to fill up the remaining bytes until we begin to overflow the stored instruction pointer. We then overwrite the stored instruction pointer to be the address of variable `message`, which contains our shellcode at the beginning of the variable. As such, the binary will return to the shellcode in the variable and be executed, thus giving us a shell, allowing us to remotely execute commands on the machine.

We can then run `cat flag.txt` in order to print out the flag.

flag:
`gigem{shellcode_in_stack!!}`
