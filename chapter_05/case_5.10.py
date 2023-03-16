current_users = ['julia', 'irina', 'Admin', 'alex', 'vosTok']
new_users = ['anTon', 'Irina', 'greg', 'Julia', 'mike']

current_users_lower = []

for user in current_users:
	current_users_lower.append(user.lower())

print(current_users_lower)

for user in new_users:
	if user.lower() in current_users_lower:
		print('Имя уже занято, выберите другое имя')
	else:
		print(f'Имя {user} свободно, вы можете продолжить регистрацию')
