# Checking a triangle's type
a = float(input('First line: '))
b = float(input('Second line: '))
c = float(input('Third line: '))

if a < b + c and b < a + c and c < b + a:
    print('\033[32mThis lines can form a Triangle\033[m')
    if a == b == c:
        print('Triangle type: \033[34mEQUILATERAL\033[m')
    elif a != b != c != a:
        print('Triangle type: \033[34mSCALENE\033[m')
    else:
        print('Triangle type: \033[34mISOSCELES\033[m')
else:
    print('\033[31mThis lines can not form a Triangle!\033[m')


