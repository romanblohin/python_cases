guests = ['Mask', 'Enshtein', 'Trump']

guests.insert(0, 'Egor Krid')
guests.insert(2, 'Loza')
guests.append('Erdogan')

print(f'Dear Mr. {guests[0]}, I wish to invite you to a dinner')
print(f'Dear Mr. {guests[1]}, I wish to invite you to a dinner')
print(f'Dear Mr. {guests[2]}, I wish to invite you to a dinner')
print(f'Dear Mr. {guests[3]}, I wish to invite you to a dinner')
print(f'Dear Mr. {guests[4]}, I wish to invite you to a dinner')
print(f'Dear Mr. {guests[-1]}, I wish to invite you to a dinner')

print(f'На ужин приглашены {len(guests)} гостей')

print(guests)