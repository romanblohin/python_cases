from random import choice, randint

number_letter_list = ['A', 'B', 'C', 'D']

#Генерируем список чисел, которые участвуют в лотереи
for i in range(10):
	new_number = randint(1, 100)
	if new_number not in number_letter_list:
		number_letter_list.append(new_number)

#Генерируем счасливую комбинацию
lucky_combination = ""

for i in range(4):
	lucky_combination += str(choice(number_letter_list)) + " "

print(number_letter_list)
print(f"Счастливая комбинация: {lucky_combination}")

lucky_ticket = ""
tries = 0

#Генерируем комбинации пока не совпадет со счастливой комбинацией, считаем попытки 
while lucky_ticket != lucky_combination:
	lucky_ticket = ""
	tries += 1
	for i in range(4):
		lucky_ticket += str(choice(number_letter_list)) + " "
	print(f"{tries}. {lucky_ticket}")


print(f"Количество попыток {tries}")
