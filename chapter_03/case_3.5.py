guests = ['Mask', 'Enshtein', 'Trump']

couldnt_come = guests[1]
guests[1] = "Kirkorov"

print(f'Dear Mr. {guests[0]}, I wish to invite you to a dinner')
print(f'Dear Mr. {guests[1]}, I wish to invite you to a dinner')
print(f'Dear Mr. {guests[-1]}, I wish to invite you to a dinner')

print(f'Mr {couldnt_come} could not come')