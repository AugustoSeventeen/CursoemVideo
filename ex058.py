# In how many chances you got the right number
from random import randint
a = randint(1, 10)
b = 1
print('\033[36m=\033[m' * 40)
print(' ' * 12, '\033[31mGUESS GAME\033[m')
print('\033[36m=\033[m' * 40)
c = int(input('From 0 to 10, what number i am thinking?: '))
while c != a:
    c = int(input('\033[31mNo, try again: \033[m'))
    b += 1
print('\033[32mYou got it in {}° try! I thought in {}\033[m'.format(b, a))
