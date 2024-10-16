# Rejected

Author: Victor

Man I'm so tired of being rejected from all these job applications...

Note: The flag is in `/app/flag.txt`. Wrap the flag with `gigem{}`. All characters are alphanumeric. Emails may take a while to send. Please be patient.

## Dev Notes

This challenge uses mailgun for sending emails. If this challenge ever gets re-used you'll have to get new api keys as I'm only using the free-trial which will expire in a month.

## Solution

As revealed in `app.py` every request we submit is automatically loaded into a rejection letter and sent to us via email. Becuse there is no sanitization on input, I can just put `\input{flag.txt}` in the key skills field and wait for the flag to be sent to me.

flag:
`gigem{du3t0fund1ngc0nstr41nts}`
