guests = ['Egor Krid', 'Mask', 'Baiden', 'Enshtein', 'Putin', 'Shoigu']

print('Вынуждены с сожалением сообщить, что на обед приглашены всего два гостя')

print(f'Дорогой мистер {guests.pop()} сообщаем об отмене приглашения')
print(f'Дорогой мистер {guests.pop(0)} сообщаем об отмене приглашения')
print(f'Дорогой мистер {guests.pop(0)} сообщаем об отмене приглашения')
print(f'Дорогой мистер {guests.pop(1)} сообщаем об отмене приглашения')

print(f'Dear Mr. {guests[0]}, I wish to invite you to a dinner')
print(f'Dear Mr. {guests[1]}, I wish to invite you to a dinner')

del guests[0]
del guests[0]

print(guests)