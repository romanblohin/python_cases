degree_three = [value ** 3 for value in range(1, 11)]

print('The first three items in the list are:')

for item in degree_three[:3]:
	print(item)

print('\nThree items from the middle of the list are:')

for item in degree_three[3:6]:
	print(item)

print('\nThe last three items in the list are:')

for item in degree_three[-3:]:
	print(item)