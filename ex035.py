# See if 3 lines can form a triangle
a = float(input('First line: '))
b = float(input('Second line: '))
c = float(input('Third line: '))
if a < b + c and b < a + c and c < a + b:
    print('\033[32mThis 3 lines can form a Triangle!')
else:
    print('\033[31mThis 3 lines can not form a Triangle!')
