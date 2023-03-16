from admin import Admin


esmith = Admin('eddie', 'smith', 'male', 43, 'san-francisco')

esmith.privileges.privileges = ['разрешено добавлять сообщения', 'разрешено удалять пользователей', 
		'разрешено банить пользователей']

print(f"\nПрава пользователя {esmith.first_name.title()} {esmith.last_name.title()}:")
esmith.privileges.show_privileges()