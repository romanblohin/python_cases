
files = ['cats.txt', 'dogs.txt']

for file in files:

	try:
		with open(file) as file_object:
			contents = file_object.read()
	except FileNotFoundError:
		print(f"\nFile {file} not found")
	else:
		print(f"\nFile {file}:")
		print(contents)