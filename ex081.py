# See how many elements, in decreasing order and if 5 is in that list
numbers = []
count = 0
while True:
    numbers.append(int(input('Type a number: ')))
    question = str(input('Continue? [Y/N]: '))
    count += 1
    if question in 'Nn':
        break
    while question not in 'YyNn':
        question = str(input('Invalid answer, Continue? [Y/N]: '))
numbers.sort(reverse=True)
print(f'You typed {count} values\nIn decreasing order is {numbers}')
print(f'The value 5 is not in the list' if 5 not in numbers else 'The value 5 is in the list')
