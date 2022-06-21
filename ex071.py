# Cash Machine
print('\033[34m=\033[m' * 40)
print('{:^40}'.format('\033[32mCASH MACHINE\033[m'))
print('\033[34m=\033[m' * 40)
v = int(input('Which amount do you want to withdraw? R$: '))
c50 = v // 50
v1 = v - (c50 * 50)
c20 = v1 // 20
v2 = v1 - (c20 * 20)
c10 = v2 // 10
v3 = v2 - (c10 * 10)
c1 = v3 // 1
v4 = v3 - (c1 * 1)
print(f'You will withdraw\n{c50} R$:50\n{c20} R$:20\n{c10} R$:10\n{c1} R$:1')
