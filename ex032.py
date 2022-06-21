# Leap year
from datetime import date
x = int(input('Enter a year or type "0" to for the current year: '))

if x == 0:
    x = date.today().year
if x % 4 == 0 and x % 100 != 0 or x % 400 == 0:

    print('{} is a leap year!'.format(x))
else:
    print('{} is not a leap year!'.format(x))
