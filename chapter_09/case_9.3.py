class User:
	'''A class for describe user'''
	def __init__(self, first_name, last_name, sex, age, location):
		'''Инициализация параметров'''
		self.first_name = first_name
		self.last_name = last_name
		self.sex = sex
		self.age = age
		self.location = location 
			
	def describe_user(self):
		'''Вывод информации о пользователе'''
		print(f"\n{self.first_name.title()} {self.last_name.title()}")
		print(f"\tSex: {self.sex.title()}")
		print(f"\tAge: {self.age}")
		print(f"\tLocation: {self.location.title()}")

	def greet_user(self):
		'''Приветствие пользователя'''
		print(f"\nHello {self.first_name.title()} {self.last_name.title()}!")

esmith = User('eddie', 'smith', 'male', 43, 'san-francisco')
aivanov = User('anton', 'ivanov', 'male', 15, 'irkutsk')
omorozova = User('olga', 'morozova', 'female', 25, 'moscow')

esmith.describe_user()
aivanov.describe_user()
omorozova.describe_user()

esmith.greet_user()
aivanov.greet_user()
omorozova.greet_user()