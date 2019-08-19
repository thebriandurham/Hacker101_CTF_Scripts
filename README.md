# CTF_Scripts
Scripts made for Hacker101 CTF Challenges

## username_enum.py
Created for Hacker101 CTF Pet Pro. Got tired of BurpSuite's rate limiting on base version and Hydra's messy cmdline. Quick script to check for a given dork in HTML response from a login form to enumerate a valid username on the server.

## password_enum.py
Created for Hacker101 CTF Pet Pro. Same use as username_enum.py, but used to guess the password once a valid username is found

## cred_length_finder.py
Created for Hacker101 CTF Micro-CMS v2. Assumes valid injectable username field and some poor back-end configuration. Determines the length of valid user:pass credential pair.

## ugly_brute.py
Created for Hacker101 CTF Micro-CMS v2. Could have just used a list-based brute forcer, but wanted to code a manual blind SQLi-like attempt. Assumes a very simple charset and a known credential length that is not complex (e.g. username and pass are both 5 characters long).
