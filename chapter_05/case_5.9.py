users = []

if users:
	for user in users:
		if user != 'admin':
			print(f'Hello {user.title()}, thank you for logging in again')
		else:
			print('Hello admin, would you like to see a status report?')
else:
	print('We need to ind some users!')