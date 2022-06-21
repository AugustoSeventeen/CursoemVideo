# Read 4 values and fold them in a Tuple
q = (int(input('Enter a number: ')), int(input('Type another number: ')),
     int(input('Type a third number: ')), int(input('Type the last number: ')))
print(f'You typed {q}')
print(f'The value 9 appears {q.count(9)} times.')
if 3 in q:
    print(f'The value 3 appears on the position {q.index(3) + 1}° for the first time!')
else:
    print('There is no value 3')
print('The pair numbers were: ', end='')
for p in q:
    if p % 2 == 0:
        print(p, end='')
        print(', ' if p > 3 else '.', end='')
