barsik = {'name': 'barsik', 'age': 3, 'color': 'grey', 'type': 'cat'}
rex = {'name': 'rex', 'age': 5, 'color': 'black', 'type': 'dog'}
martha = {'name': 'martha', 'age': 8, 'color': 'yellow', 'type': 'cow'}

pets = (barsik, rex, martha)

for pet in pets:
	print(f"\n A {pet['type']} by name {pet['name'].title()}:")
	print(f"\t Color: {pet['color']}")
	print(f"\t Age: {pet['age']}")