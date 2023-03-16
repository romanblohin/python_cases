from restaurant import Restaurant

restaurant = Restaurant('White Rabbit', 'european')

restaurant.describe_restaurant()
restaurant.open_restaurant()

restaurant.set_number_served(52)
restaurant.get_number_served()

restaurant.increment_number_served(18)
restaurant.get_number_served()