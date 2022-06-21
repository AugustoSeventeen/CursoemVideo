# Price list with tuples
print('\033[34m=\033[m' * 51)
print('{:^55}'. format('\033[33mPRICE LIST\033[m'))
print('\033[34m=\033[m' * 51)
a = ('Pencil', 1.90, 'Eraser', 3.00, 'Ruler', 4.90, 'Pen', 2.10,
     'Notebook', 9.90, 'Backpack', 190.00, 'Pencilcase', 10.00)
for c in range(0, len(a)):
    if c % 2 == 0:
        print(f'{a[c]:.<40}', end='')
    else:
        print(f'R$: {a[c]:>7.2f}')
print('\033[34m=\033[m' * 51)
