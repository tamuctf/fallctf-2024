# Elbereth

I was walking by the graveyard when a strangely dressed man with a mad look in his eye pushed this file into my hands, babbling about some kind of "amulet".

## Hints



## Solution

First, gunzip the bonD0.5.gz file to get bonD0.5 [bones file](https://nethackwiki.com/wiki/Bones). By looking in the file it can be seen that it was made with wizard mode. By putting the bones file in the correct location (`/var/games/nethack`) where it is checked and using wizard mode to go to the correct level (5) there is a random chance (1/3) of loading the bones file. Once the bones file loads after a few tries then the flag is displayed.

Steps to getting the flag:

Move `bonD0.5.gz` to `/var/games/nethack` (see the `FILES` section of `man nethack`)

Run in [wizard mode](https://nethackwiki.com/wiki/Wizard_mode) with `sudo nethack -D`

In game:
- Create a character
- Teleport to level 5 (from the filename) by typing `#wizlevelport`
- Answer `y` to `Get bones? [yn]`, and `n` to `Unlink bones? [yn]`
  - If this prompt doesn't appear, enter `#wizmakemap` to reload the level
- Get a map of the level with `#wizmap`
- The flag is visible when in the character's line of sight
  - If it's not immediately visible, move around by using hjkl (vim keys)
    - Or teleport by pressing ctrl+t
  - The flag may be moved by monsters, so it might be necessary to reload the level with `#wizmakemap`

flag:
`gigem{GN0mE_wiTH_A_wanD_oF_deAth!?}`
