class Restaurant:

	def __init__(self, restaurant_name, cuisine_type):
		'''Initialize restaurant name and cuisine type atributes'''
		self.restaurant_name = restaurant_name
		self.cuisine_type = cuisine_type

	def describe_restaurant(self):
		'''Show information about restaurant'''
		print(f"Restaurant {self.restaurant_name} with {self.cuisine_type} cuisine")

	def open_restaurant(self):
		'''Show information that restaurant is opened'''
		print(f"Restaurant {self.restaurant_name} is opened")

restaurant_in_moscow = Restaurant('White Rabbit', 'european')
restaurant_in_spb = Restaurant('Terrassa', 'american')
restaurant_in_krasnodar = Restaurant('Hank', 'seafood')

restaurant_in_krasnodar.describe_restaurant()
restaurant_in_spb.describe_restaurant()
restaurant_in_moscow.describe_restaurant()