car = "Audi"

if car == "Audi":
	print("My car is Audi. That's True")

if car != "BMW":
	print("My car is not BMW. That's True")

if car.lower() == "audi":
	print("My car is Audi. That's True")

age = 20

if age < 21: print("You are too young")
if age > 18: print("You are old")
if age >= 20: print("You are old")
if age <= 20: print("You are too young")

if car.lower() == "audi" and age == 20: print("Great! You are awesome")
if car.lower() == "bmw" or age == 20: print("Great! You are awesome")

toppings = ['mushrooms', 'olives', 'green peppers',
                      'pepperoni', 'pineapple', 'extra cheese']
topping = 'mushrooms'

if topping in toppings: print(f'{topping.title()} is in the list')
if 'french fries' not in toppings: print('french fries is not in the list')
