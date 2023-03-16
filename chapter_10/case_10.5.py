message = ""

while message != 'no':
	reason = input("Почему Вам нравится программировать? ")

	filename = 'reason_book.txt'
	with open(filename, 'a') as file_object:
		file_object.write(f"{reason}\n")

	message = input("Вы хотите продолжить ввод (yes/no)? ")