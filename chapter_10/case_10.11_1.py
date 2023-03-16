import json

favorite_number = input("Введите свое любимое число ")

filename = 'favorite_number.json'
with open(filename, 'w') as file_object:
	json.dump(favorite_number, file_object)


