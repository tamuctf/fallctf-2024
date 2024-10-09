# Sus Processes

Memory Dump Link:
https://drive.google.com/file/d/19Ea-SZ-senEAwZMZQInU5zCfFWbO9LR2/view?usp=share_link

Find the running processes that are a bit odd.

Note: Volatility3 is a useful tool.

## Solution

The solution is as easy as using Volatility to list all running processes in the memdump.

`vol -f memdump.mem windows.pslist.PsList`

The output of the Volatility command returns three processes which contain segments of the flag in their name which can be combined for the full flag.

flag:
`gigem{y0ufountmeinthem3mory}`
