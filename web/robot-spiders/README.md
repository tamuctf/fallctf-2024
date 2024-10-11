# Robot Spiders

I was trying to catch up on the news, but I can't read any of the articles on my usual site.
The website said something about licensing and AI?

## Hints

- This challenge does not require interacting with any AI systems, just a bit of research.

## Dev Notes

Simple web challenge running on Flask, no special concerns.

## Solution

The challenge checks the user-agent string to grant access.

Can set it in firefox by:
- Go to about:config
- Set general.useragent.override to "GPTBot"

Then access the page to get the flag

flag:
`gigem{n0b0dy_r34d5_7h3_fu11_4r71c13_4nyw4y}`
