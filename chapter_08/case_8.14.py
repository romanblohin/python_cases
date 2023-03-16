def make_car(brand, model, **car_info):
	'''Возвращает словарь с информацией о машине'''
	car_info['brand'] = brand
	car_info['model'] = model

	return car_info

car = make_car('subaru', 'outback', color='blue', tow_package=True)
print(car)
