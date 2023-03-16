from random import randint 

class Die:
	'''Класс описывает игральные кости с заданным количеством граней'''
	def __init__(self, sides = 6):
		'''Инициализация элемента класса Die'''
		self.sides = sides

	def roll_die(self):
		'''Функция возвращает случайное число в заданном диапазоне'''
		print(f"\tВыпало число - {randint(1, self.sides)}")

print("Бросаем кубик с 6 гранями")
six_side_cube = Die(6)
for i in range(10):
	six_side_cube.roll_die()

print("\nБросаем кубик с 10 гранями")
ten_side_cube = Die(10)
for i in range(10):
	ten_side_cube.roll_die()

print("\nБросаем кубик с 20 гранями")
twenty_side_cube = Die(20)
for i in range(10):
	twenty_side_cube.roll_die()
