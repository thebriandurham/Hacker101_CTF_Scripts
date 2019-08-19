# CTF_Scripts
Scripts made for various CTF Challenges

## username_enum.py
Created for Hacker101 CTF Pet Pro. Got tired of BurpSuite's rate limiting on base version and Hydra's messy cmdline. Quick script to check for a given dork in HTML response from a login form to enumerate a valid username on the server.

## password_enum.py
Created for Hacker101 CTF Pet Pro. Same use as username_enum.py, but used to guess the password once a valid username is found

## cred_length_finder.py
Created for Hacker101 CTF Micro-CMS v2. Assumes valid injectable username field and some poor back-end configuration. Determines the length of valid user:pass credential pair.
