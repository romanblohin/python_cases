vacation = {}
message = ""

#Пишем цикл с опросом пользователей
while message.lower() != 'no':
	name = input("Введите свое имя ")
	place = input("Где Вы хотите провести свой отпуск? ")
	vacation[name] = place
	message = input("Вы хотите продолжить опрос? (yes/no) ")
print("")
#Выводим результаты опроса
for name, place in vacation.items():
	print(f"{name.title()} хотел бы провести отпуск в {place.title()}")