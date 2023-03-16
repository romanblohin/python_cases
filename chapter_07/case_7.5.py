prompt = "Укажите Ваш возраст "

active = True

while active:
	age = int(input(prompt))

	if age < 3:
		price = 0
	elif age < 12:
		price = 10
	elif age >= 12:
		price = 15

	active = False

print(f"Цена Вашего билета {price}$")
