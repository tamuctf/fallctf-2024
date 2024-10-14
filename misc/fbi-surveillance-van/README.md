# FBI Surveillance Van

One day, I bought an FBI surveillance van off eBay—don’t ask. Naturally, I decided to drive over to my friend’s house and have some fun. The van was packed with radio gear, including a bunch of antennas, so I pointed one toward his place and started scanning through frequencies.

That’s when I found something weird: a signal that spiked up and down. What really caught my attention was that it seemed to sync perfectly with the flashes from his monitor coming out the window. I stared at the van’s equipment and then back at his house, completely baffled.

Every time his screen flashed, the frequency would jump in sync, but I had no idea why. I spent hours messing with the software, trying to make sense of it. My simple prank turned into an obsession. Now the real challenge was figuring out what was causing this strange signal.

**Download: https://drive.google.com/file/d/13Ef3sGugmUB9UzVStvowQ9BmvAkhtSL4/view?usp=sharing**

Note: https://www.youtube.com/watch?v=vvOAIeVGRfw

## Hints

Use a sample rate of 2.4 MSPS (int16) and format the flag in all lowercase.

## Dev Notes

Make flag case insensitive.

## Solution

This challenge requires the use of a SDR video snooping tool called `tempest`. To solve the challenge, we must [download `tempest`](https://github.com/martinmarinov/TempestSDR) from Github. Based on the tip provided in the description, we need to load the provided `.wav` file into Tempest. When loading the file into tempest we must set a sample rate of `2400000` with the data type `int16`. Once the file is open we can set the resolution to `1920x1080@60Hz` and press start. On the screen, the flag will play.

flag:
`gigem{th3y_4r3_w4tch1ng}`
