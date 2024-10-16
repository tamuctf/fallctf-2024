# The Onion Revealer

Author: Damian

I got scammed while buying some completely legal goods on a niche e-commerce website; the details aren't important.
The admins refused to help me, so I'd like to unmask them and take down their whole operation in retribution.
This little service they run seems like a good starting point.

## Hints

- This challenge requires downloading a special web browser.

## Dev Notes

This challenge must be hosted on its own infrastructure with a dedicated public IP, such as a cloud-hosted VPS, so that users can meet the solve condition by connecting via its public IP.
The machine will serve the site both as a TOR hidden service and via direct/normal HTTP.

**Hosting Steps**
1. Requires Python, Tor, and Nginx installed (see configuration below)
2. Install Python dependencies (ideally in a venv): `pip install flask requests gunicorn`
3. Run the gunicorn HTTP server: `gunicorn -w 4 'app:app' -b '127.0.0.1:3000'`
4. Start the TOR server: `tor -f /etc/tor/torrc`

**Nginx Configuration**
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

**TORrc Configuration**
```
HiddenServiceDir [any directory] # a folder for TOR hidden service settings, can be placed anywhere, contains the keys that allow you to serve on your onion domain
HiddenServicePort 9030 127.0.0.1:80 # external traffic to port 9030 is redirected to 127.0.0.1:80 internally
```

Both direct HTTP traffic and TOR traffic go through Nginx, so the `direct-access-no-tor` header is used to tag whether traffic came through TOR, so that direct IP connections can be identified and served the flag instead.

## Solution

When accessing the onion link, we are presented with a webhook testing site. Based on the challenge description and the flavor text on the website, we can infer that the intention is to find the server's IP. Because this server will make web requests to a server of our choosing, we can set up a listener via `webhook.site` and make a request to our server. Once that request is received, it will reveal the underlying IP of the server. Requesting this IP gives us the flag.

flag:
`gigem{n0w_70_6r4b_h15_l4p70p}`
