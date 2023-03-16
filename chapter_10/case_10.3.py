
guest_name = input("Введите Ваше имя ")

filename = 'guest.txt'
with open(filename, 'w') as file_object:
	file_object.write(f"{guest_name}\n")


