# multiplication table
a = int(input('Type a integer number to known it multiplication table: '))
for d in range(1, 11):
    c = a * d
    print('{} X 16{} = {}'.format(d, a, c))
