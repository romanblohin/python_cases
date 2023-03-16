
age = 13

if age < 2:
	period = 'младенец'
elif age < 4:
	period = 'малыш'
elif age < 13:
	period = 'ребенок'
elif age < 20:
	period = 'подросток'
elif age < 65:
	period = 'взрослый'
elif age >= 65:
	period = 'пожилой человек'

print(f'Вы {period}')