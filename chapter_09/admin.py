from user import User

class Privileges:
	''''''
	def __init__(self):
		self.privileges = []

	def show_privileges(self):
		'''Show user privileges'''
		for privilege in self.privileges:
			print(f"\t- {privilege}")

class Admin(User):

	def __init__(self, first_name, last_name, sex, age, location):
		'''A class for describe admin user'''
		super().__init__(first_name, last_name, sex, age, location)
		self.privileges = Privileges()