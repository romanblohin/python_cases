import json

filename = 'favorite_number.json'

try:
	with open(filename) as file_object:
		favorite_number = json.load(file_object)
except FileNotFoundError:
	favorite_number = input("Введите любимое число ")
	with open(filename, 'w') as file_object:
		json.dump(favorite_number, file_object)
else:
	print(f"Ваше любимое число {favorite_number}")

