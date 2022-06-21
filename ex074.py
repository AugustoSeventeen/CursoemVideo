# Largest and smallest value in tuple
from random import randint
r = (randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10))
print('The drawn values were: ', end='')
print(r, end=' ')
print(f'\nThe largest value is {max(r)}\nThe smallest value is {min(r)}')
