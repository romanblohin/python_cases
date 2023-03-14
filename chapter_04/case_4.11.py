pizzas = ['pepperoni', 'margarita', '4 chesse']

friend_pizzas = pizzas[:]

pizzas.append('pineapple')
friend_pizzas.append('onion')

print('My favorite pizzas are:')
for pizza in pizzas:
	print(pizza)

print('My friend’s favorite pizzas are:')
for pizza in friend_pizzas:
	print(pizza)
