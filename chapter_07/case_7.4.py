prompt = "Введите топинг который хотели бы заказать "

while True:
	topping = input(prompt)

	if topping == 'quit':
		break
	else:
		print(f"Топинг {topping} добавлен в пиццу")