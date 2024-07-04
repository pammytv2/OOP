
person = {'name' :  'Alice','age':30, 'city':'New york'}
print('Name:',person['name'])

person['age'] = 31
print('Updated age:',person['age'])

for key, value in person.items():
    print(f'{key}:{value}')


