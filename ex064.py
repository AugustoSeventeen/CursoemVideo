# Adding numbers and disregarding 999
from time import sleep
a = int(input('Type a number: '))
cont = add = 0
while a != 999:
    add += a
    cont += 1
    a = int(input('Type a number: '))
print('Processing...')
sleep(2)
print('You typed {} and sum is {}'.format(cont, add))
