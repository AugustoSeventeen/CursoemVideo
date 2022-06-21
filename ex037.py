# Do a number converter
a = int(input('\033[33mWhat number would you like to converter?: \033[m'))
b = int(input('[ 1 ] for BINARY numbers\n[ 2 ] for OCTAL numbers or\n[ 3 ] for HEXADECIMAL:\nI choose: '))
if b == 1:
    print('{} in Binary number is {}'.format(a, bin(a)[2:]))
elif b == 2:
    print('{} in OCTAL number is {}'.format(a, oct(a)[2:]))
elif b == 3:
    print('{} in HEXADECIMAL number is {}'.format(a, hex(a)[2:]))
else:
    print('\033[31mInvalid option, try again.\033[m')
