class Restaurant:

	def __init__(self, restaurant_name, cuisine_type):
		'''Initialize restaurant name and cuisine type atributes'''
		self.restaurant_name = restaurant_name
		self.cuisine_type = cuisine_type
		self.number_served = 0

	def describe_restaurant(self):
		'''Show information about restaurant'''
		print(f"Restaurant {self.restaurant_name} with {self.cuisine_type} cuisine")

	def open_restaurant(self):
		'''Show information that restaurant is opened'''
		print(f"Restaurant {self.restaurant_name} is opened")

	def get_number_served(self):
		'''Show amount of served peolpe'''
		print(f"The number of served is {self.number_served} people")

	def set_number_served(self, people):
		'''Set number of served peolpe'''
		self.number_served = people

	def increment_number_served(self, people):
		'''Increment number of served people'''
		self.number_served += people

class IceCreamStand(Restaurant):

	def __init__(self, restaurant_name, cuisine_type):

		super().__init__(restaurant_name, cuisine_type)
		self.flavours = []

	def get_flavours(self):
		'''Вывести список сортов мороженного'''
		for flavour in self.flavours:
			print(f"\t{flavour}")

cafe = IceCreamStand('Baskin Robins', 'ice cream')

cafe.flavours = ['vanilla', 'chocolate', 'fruity ice']

cafe.get_flavours()