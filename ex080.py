# Organize 5 value without use sort
numbers = []
for counter in range(1, 6):
    number = int(input('Type a number: '))
    if counter == 1 or number > numbers[-1]:
        numbers.append(number)
        print(f'The value was added in the end of the list.')
    else:
        position = 0
        while position < len(numbers):
            if position <= numbers[position]:
                numbers.insert(position, number)
                break
        position += 1
print(f'You typed {numbers}')
