# Swimming category
from datetime import date
p = int(input('Enter the year you were born: '))

i = range(9, 14)
j = range(15, 19)

x = date.today().year - p

if x < 9:
    print('Your category is \033[32mLITTLE\033[m')
elif x in i:
    print('Your category is \033[32MCHILDISH\033[m')
elif x in j:
    print('Your category is \033[32mJUNIOR\033[m')
elif x == 20:
    print('Your category is \033[32mSENIOR\033[m')
elif x > 20:
    print('Your category is \033[32mMASTER\033[m')
