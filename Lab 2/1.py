n = 6
row = 5

'''
for i in range(1, n):
    print('*' * i)




for i in range (row,0,-1):    #range(star,stop,step)
    print('*' *i)
'''


for i in range(row):
    print(' ' * (row - i - 1) + '*' * (2 * i + 1))

'''

for i in range(row , 0, -1):
    print(' ' * (row - i) + '*' * (2 * i - 1))
    '''
