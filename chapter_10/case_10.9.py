files = ['cats.txt', 'dogs.txt', 'cows.txt']

for file in files:

	try:
		with open(file) as file_object:
			contents = file_object.read()
	except FileNotFoundError:
		pass
	else:
		print(f"\nFile {file}:")
		print(contents)