# Cinephile

The Security Operations Center (SOC) got a packet capture (pcapng) of someone at work not actively working. It looks like their might be a movie being watched on an unsecure connection. What are the creatures approaching from the southeast?

File: https://drive.google.com/file/d/1qXoLfHoCzua_rZhtPM33Ny4s6kkciMqo/view?usp=sharing

Flag format: gigem{words_seperated_by_underscores}

Useful resources:
- https://www.wireshark.org/
- https://en.wikipedia.org/wiki/Telnet

## Solution

If we open the packet capture file using Wireshark, we can see that there is a lot of network traffic, and that Telnet is one of the protocols being used. Since information sent over Telnet is unencrypted and visible, we can look at the information being sent by right-clicking on a Telnet packet and clicking `Follow->TCP Stream`. We then see that an ASCII version of Star Wars is being transmitted over Telnet. If we search for the string `southeast`, we see C-3PO mention people coming from the southeast, and R2-D2 can be seen mentioning the group coming from the southeast, which is `sand people`. 

flag:
`gigem{sand_people}`
