from random import choice, randint

number_letter_list = ['A', 'B', 'C', 'D']

for i in range(10):
	new_number = randint(1, 100)
	if new_number not in number_letter_list:
		number_letter_list.append(new_number)

lucky_ticket = ""

print(number_letter_list)
print("Выигрывает билет под номером", end=' ')

for i in range(4):
	print(choice(number_letter_list), end=' ')
