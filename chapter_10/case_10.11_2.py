import json

filename = 'favorite_number.json'

with open(filename) as file_object:
	favorite_number = json.load(file_object)

print(f"Я знаю ваше любимое число! Это {favorite_number}")