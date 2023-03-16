message = ""

while message != 'no':
	guest_name = input("Введите Ваше имя ")

	greeting_message = f"Hello {guest_name.title()}"
	print(greeting_message)
	filename = 'guest_book.txt'
	with open(filename, 'a') as file_object:
		file_object.write(f"{greeting_message}\n")

	message = input("Вы хотите продолжить ввод (yes/no)? ")