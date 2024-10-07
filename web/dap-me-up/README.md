# Dap Me Up

Bob,

Dap me up, but login with your account first to prove it's really you.

## Dev Notes

Only access to the HTTP server should be given.

## Solution

The name `dap me up` is a hint that this application is using LDAP. LDAP inputs, if not properly sanitized, can allow for malicious queries to be made much like SQL injection. In this case, we are trying to bypass authentication on the login page. To find some information about LDAP injection, we can visit the Hack Tricks [LDAP injection](https://book.hacktricks.xyz/pentesting-web/ldap-injection) page.

The first payload I attempted was just using `*` in both the username and password fields. This essentially is a wildcard that will match anything in the LDAP query. Unfortunately, the application is checking for `*` and returns "HACKING ATTEMPT DETECTED".

To properly solve this challenge, we must find a payload that does not use the `*` character. Looking at the hacktricks page above, there is a payload that takes a username and sets the password as `any` meaning that as long as we know the username, we can successfully log in. Based on the description of the challenge, there is a user named `bob` on the system. Using the username `bob`, the following payload allows us to bypass authentication:

```
username: admin)(!(&(|
password: any))
```

flag:
`gigem{c0n6r475_y0u_f0und_ld4p_1nj3c710n_w17h0u7_*}`
