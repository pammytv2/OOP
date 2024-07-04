
citices = {
    'New York' : [32,25,30,28,35],
    'los Angeles':[75,68,72,70,80],
    'Chicago' :[20,18,22,25,15]

}

averages = {city:sum(temps)/len(temps) for city, temps in citices.items()}
print('Average temperatures',averages)
