# Showing pair and odd numbers
numbers = []
pair = []
odd = []
while True:
    number = numbers.append(int(input('Type a number: ')))
    question = str(input('Continue? [Y/N]: ')).strip().lower()[0]
    while question not in 'YyNn':
        question = str(input('Invalid answer, Continue? [Y/N]: ')).strip().lower()[0]
    if question in 'Nn':
        break
for position, item in enumerate(numbers):
    if item % 2 == 0:
        pair.append(item)
    elif item % 2 == 1:
        odd.append(item)
print(f'You typed {numbers}')
print(f'The pair numbers is {pair}')
print(f'The odd numbers is {odd}')
