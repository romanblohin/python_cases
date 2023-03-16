import unittest

class Employee:
	'''Класс описывает сотрудника фирмы'''

	def __init__(self, first_name, last_name, salary):
		'''Инициализация класса, принимает параметры: имя, фамилия и годовая зарплата'''
		self.first_name = first_name
		self.last_name = last_name
		self.salary = salary

	def give_raise(self, new_salary=5000):
		'''Функция увеличивает годовую зарплату работника на величину new_salary
		new_salary по умолчанию равен 5000, не является обязательным аргументом'''
		self.salary += new_salary

	def show_salary(self):
		'''Функция выводит информацию о зарплате работника'''
		print(f"Годовая зарплата {self.first_name.title()} {self.last_name.title()} равна:")
		print(f"\t- {self.salary}$")

class EmployeeTestCase(unittest.TestCase):
	'''Тестируем класс Employee'''

	def setUp(self):
		'''Инициализируем объект класса Employee для дальнейшего использования в тестах'''
		self.employee = Employee('anton', 'ivanov', 15000)

	def test_give_default_raise(self):
		'''Проверяем функцию give_raise() класса Employee без указания надбавки.
		Надбавка по умолчанию составляет 5000$'''
		self.employee.give_raise()
		self.assertEqual(self.employee.salary, 20000)

	def test_give_custom_raise(self):
		'''Проверяем функцию give_raise() класса Employee с указанием надбавки 7000$'''
		self.employee.give_raise(7000)
		self.assertEqual(self.employee.salary, 22000)

if __name__ == '__main__':
    unittest.main()