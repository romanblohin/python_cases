from random import choice, randint

number_letter_list = ['A', 'B', 'C', 'D']

for i in range(10):
	new_number = randint(1, 100)
	if new_number not in number_letter_list:
		number_letter_list.append(new_number)

lucky_ticket = ""

for i in range(4):
	lucky_ticket += str(choice(number_letter_list)) + " "

print(number_letter_list)

print(f"Выигрывает билет под номером {lucky_ticket}")

