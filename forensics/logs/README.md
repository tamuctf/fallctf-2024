# Logs

Author: Noam

There are 936 communications captured from 2011-01-01 to 2013-06-04 between 4 different schools. Each one has an ID corresponding to the message sent with the email and phone of both the receiver and sender. There is one malicious message in this log file. Can you find which one and provide the ID as the flag?

Flag format: `gigem{ID}`

## Solution

We know that there is only one malicious message in the log file. We can see the frequency of a value appearing in the CSV in many ways, I used bash commands.

To check the frequency of Sender Emails: `cat log.csv | sed 's/,/ /g' | awk '{print $2}' | sort | uniq -c | sort`

To check the frequency of Sender Phone numbers: `cat log.csv | sed 's/,/ /g' | awk '{print $3}' | sort | uniq -c | sort`

When looking at the Sender Phone numbers, there are three phone numbers which appear only once, while there are two Sender Emails which only appear once, meaning one of the Sender Phone numbers is inaccurate or forged. 
When we check the log entry with phone number `979-674-1902`, we see that the Sender Email is `raymond.figueroa@cmu.edu`, and that for every other appearance of that email, the Sender Phone number is `979-674-9379`. We can only conclude that the log with number `979-674-1902` is malicious. 

flag:
`gigem{6638FEOK}`
