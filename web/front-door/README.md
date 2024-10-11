# Front Door

I managed to connect to an internal server, but the control panel is still locking me out.
I need to find a way to trick the server into thinking I'm coming from inside the network.

## Dev Notes

This is a simple web challenge using Flask, competitors just need to be able to access the site.

## Solution

This site uses a virtual host to check for internal requests. Can add the `Host` header to bypass the check.

```sh
curl http://127.0.0.1:3000 -H 'Host: server.internal'
```

flag:
`gigem{h057_15_ju57_4_50c14l_c0n57ruc7}`
