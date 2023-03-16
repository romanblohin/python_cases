def make_car(brand, model, **car_info):
	'''Возвращает словарь с информацией о машине'''
	car_info['brand'] = brand
	car_info['model'] = model

	return car_info