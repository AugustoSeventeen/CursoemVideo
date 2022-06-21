# Military enlistment
from datetime import date
print('=' * 36)
print(' ' * 6, '\033[32mMilitary enlistment\033[m')
print('=' * 36)
a = int(input('Type in witch year you were born: '))
z = date.today().year - a
if z < 18:
    x = (18 - z) + date.today().year
    print('\033[33mYou do not need to enlist yet. Your year to enlist is\033[m', x)
elif z == 18:
    print('\033[32mYou are in the right time to enlist\033[m')
elif z > 18:
    b = (18 - z) + date.today().year
    print('\033[31mYour time to enlist has already passed!. Your time to enlist was\033[m', b)
