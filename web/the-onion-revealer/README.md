# The Onion Revealer

I got scammed while buying some completely legal goods on a niche e-commerce website; the details aren't important.
The admins refused to help me, so I'd like to unmask them and take down their whole operation in retribution.
This little service they run seems like a good starting point.

## Hints

- This challenge requires downloading a special web browser.

## Dev Notes

This challenge must be hosted on its own infrastructure with a dedicated public IP, such as a cloud-hosted VPS.
The machine will serve the site both as a TOR hidden service and via direct/normal HTTP.

Nginx Configuration
```
server {
    listen 80;
    listen [::]:80;

    server_name _;

    location / {
        proxy_pass http://127.0.0.1:3000/;
        proxy_set_header direct-access-no-tor true;
    }
}

server {
    listen 80;
    listen [::]:80;

    server_name [onion domain];

    location / {
        proxy_pass http://127.0.0.1:3000/;
        proxy_set_header direct-access-no-tor false;
    }
}
```

TORrc Configuration
```
HiddenServiceDir [any directory] # a folder for TOR hidden service settings, can be placed anywhere
HiddenServicePort 9030 127.0.0.1:80 # external traffic to port 9030 is redirected to 127.0.0.1:80 internally
```

Both direct HTTP traffic and TOR traffic go through Nginx, so the direct-access-no-tor header is used to tag whether traffic came through TOR, so that direct IP connections can be identified and served the flag instead.

## Solution

This section will contain the reviewers solution. The flag section below should stay the same. Just replace `gigem{testing_flag}` with the challenge flag.

flag:
`gigem{testing_flag}`
