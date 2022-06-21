# Reading name and price of products:
from time import sleep
pt = t = ptt = c = 0
cc = ''
while True:
    p = str(input('Product: '))
    price = int(input('Price R$: '))
    ptt += price
    pt += 1
    if price >= 1000:
        t += 1
    if pt == 1 or price < c:
        c = price
        cc = p
    q = ' '
    while q not in 'YyNn':
        q = str(input('More one? [Y/N]: ')).strip().lower()
    if q in 'Nn':
        break
print('Processing...')
print(f'The total price is {ptt}, there are {t} product more the R$: 1,000 and {cc} is the cheaper one.')
