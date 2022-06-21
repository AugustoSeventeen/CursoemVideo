# Reading the name, age and genre
s = 0
biggest = 0
name = ''
age = 0
for c in range(1, 5):
    print('{}° Person'.format(c))
    n = str(input('Name: '))
    a = int(input('Age: '))
    g = str(input('Genre F/M: '))
    s += a
    if c == 1 and g in 'Mn':
        biggest = a
        name = n
    if g in 'Mn' and a > biggest:
        biggest = a
        name = n
    if g in 'Ff' and a < 20:
        age += 1
print('The average of the ages is ', s / 4)
print('{} is the older man and has {} years old!'.format(name, biggest))
print('There are {} women under 20 years old'.format(age))
