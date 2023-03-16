from random import choice, randint

def spin_drum(choice_list):
	'''Функция принимает спискок из букв и цифр.
	   возвращает комбинацию случайно выбранных букв и цифр из списка'''
	
	combination = ""

	for i in range(4):
		combination += str(choice(choice_list)) + " "

	return combination


number_letter_list = ['A', 'B', 'C', 'D']

#Генерируем список чисел, которые участвуют в лотереи
for i in range(10):
	new_number = randint(1, 100)
	if new_number not in number_letter_list:
		number_letter_list.append(new_number)

#Генерируем счасливую комбинацию
lucky_combination = spin_drum(number_letter_list)

lucky_ticket = ""
tries = 0

#Генерируем комбинации пока не совпадет со счастливой комбинацией, считаем попытки 
while lucky_ticket != lucky_combination:
	lucky_ticket = spin_drum(number_letter_list)
	tries += 1
	print(f"{tries}. {lucky_ticket}")

print("Числа которые участвуют в лотереи")
print(number_letter_list)

print(f"Выигрышная комбинация: {lucky_combination}")
print(f"Количество попыток {tries}")
