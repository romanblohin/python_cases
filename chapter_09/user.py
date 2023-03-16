class User:
	'''A class for describe user'''
	def __init__(self, first_name, last_name, sex, age, location):
		'''Инициализация параметров'''
		self.first_name = first_name
		self.last_name = last_name
		self.sex = sex
		self.age = age
		self.location = location
		self.login_attempts = 0 
			
	def describe_user(self):
		'''Вывод информации о пользователе'''
		print(f"\n{self.first_name.title()} {self.last_name.title()}")
		print(f"\tSex: {self.sex.title()}")
		print(f"\tAge: {self.age}")
		print(f"\tLocation: {self.location.title()}")

	def greet_user(self):
		'''Приветствие пользователя'''
		print(f"\nHello {self.first_name.title()} {self.last_name.title()}!")

	def increment_login_attempts(self):
		'''Increment of user login attempts'''
		self.login_attempts += 1

	def reset_login_attempts(self):
		'''Reset user login attempts'''
		self.login_attempts = 0