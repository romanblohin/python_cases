favorite_numbers = {'jack': [10, 35, 18], 'john': [15, 3], 'kendra': [13, 28, 350, 14], 'maxim': [8, 230, 5], 'elena': [5]}

for name, numbers in favorite_numbers.items():
	print(f"\n {name.title()}'s favorite numbers:")
	for number in numbers:
		print(f"\t{number}")