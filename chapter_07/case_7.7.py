sandwich_orders = ['pastrami', 'cheese', 'tuna', 'pastrami', 'egg', 'bacon', 'pastrami']
finished_sandwiches = []

print("Sandwich pastrami is not available now")
#Удаляем сэнвич пастрами из списка сэндвичей
while 'pastrami' in sandwich_orders:
	sandwich_orders.remove('pastrami')

#Готовим заказанные сэндвичи, сэндвичи из списка заказанных (sandwich_orders)
# переходят в список готовых (finished_sandwiches)
while sandwich_orders:
	sandwich = sandwich_orders.pop()

	print(f"I made your {sandwich} sandwich")
	finished_sandwiches.append(sandwich)

for sandwich in finished_sandwiches:
	print(sandwich)