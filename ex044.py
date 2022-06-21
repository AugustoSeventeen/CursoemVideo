# Form of payment
a = float(input('How much is: R$: '))
b = int(input('\033[36m1\033[m if is \033[36mMoney/Check\033[m\n\033[31m2\033[m if is \033[31mCard\033[m\n\033['
              '34m3\033[m if \033[34m2x in Card\033[m\n\033[35m4\033[m if \033[35m3x or more in Card\033[m: '))
if b == 1:
    p = a - (a * 10 / 100)
    print('The price with discount is R$:{:.2f}'.format(p))
elif b == 2:
    p1 = a - (a * 5 / 100)
    print('The with discount is R$:{:.2f}'.format(p1))
elif b == 3:
    print('There is no discount, the price is R$:{:.2f}'.format(a))
elif b == 4:
    p2 = a + (a * 20 / 100)
    print('The final price with fees is R$:{:.2f}'.format(p2))
else:
    print('\033[32mInvalid option\033[m')
