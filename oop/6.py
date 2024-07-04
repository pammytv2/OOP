
names = ['Alice','Bob','Charlie']
ages = [25,30,35]
city = ['new york', 'los Angeles','Chicago']

for name,age,city in zip(names,ages,city):
    print(f'{name} is {age} years old  and lives in {city}')
