# Arithmetic progression
a = int(input('Enter the first term: '))
b = int(input('Enter the reason: '))
d = a + (10 - 1) * b
for c in range(a, d, b):
    print(c, end=', 4')
