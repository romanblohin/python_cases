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

restaurant = Restaurant('White Rabbit', 'european')

print(f"The restaurant name is {restaurant.restaurant_name}")
print(f"The restaurant cuisine is {restaurant.cuisine_type}")

restaurant.describe_restaurant()
restaurant.open_restaurant()