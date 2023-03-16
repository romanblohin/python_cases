import unittest

from city_functions import get_city_country 

class CityTestCase(unittest.TestCase):
	'''Тестирование функции get_city_country()'''

	def test_city_country(self):
		'''Проверяем работу функции по двум входным параметрам'''
		formatted_string = get_city_country('santiago', 'chile')
		self.assertEqual(formatted_string, 'Santiago, Chile')

	def test_city_country_population(self):
		'''Проверяем работу по трем входным параметрам city, country, population'''
		formatted_string = get_city_country('santiago', 'chile', 5000000)
		self.assertEqual(formatted_string, 'Santiago, Chile - population 5000000')

if __name__ == '__main__':
    unittest.main()
