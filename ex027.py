# Read a name and say the first and second name
x = str(input('Enter your full name: ')).strip().split()
y = ' '.join(x)
z = y.rfind(' ')
a = len(y)
b = a - z
c = a - b

print('First name: {}' .format(x[0]))
print('Your last name is: {}' .format(y[c:]))
