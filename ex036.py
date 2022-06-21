# Bank loan to finance a house
ph = float(input('How much is the house?: R$: '))
s = float(input('How much is your salary?: R$: '))
a = int(input('In how many years you intend to pay?: '))

p = a * 12
p1 = ph / p
sp = s * 30 / 100

if p1 > sp:
    print('You need to pay {:.2f} per month'.format(p1))
    print('\033[31mYour loan was denied')
elif p1 <= sp:
    print('You need to pay {:.2f}'.format(p1))
    print('\033[32mYour loan was approved')
