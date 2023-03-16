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

restaurant = Restaurant('White Rabbit', 'european')

restaurant.describe_restaurant()
restaurant.open_restaurant()

restaurant.set_number_served(52)
restaurant.get_number_served()

restaurant.increment_number_served(18)
restaurant.get_number_served()