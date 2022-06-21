# Read a number
n = int(input('Type a number: '))

u = n // 1 % 10
t = n // 10 % 10
h = n // 100 % 10
th = n // 1000 % 10


print('Unity: {}' .format(u))
print('Ten: {}' .format(t))
print('Hundred: {}' .format(h))
print('Thousand: {}' .format(th))




