# Organizing number in pairs and odds.
numbers = [[], []]
number = 0
for order in range(1, 8):
    number = int(input(f'Enter the {order}° number: '))
    if number % 2 == 1:
        numbers[1].append(number)
    elif number % 2 == 0:
        numbers[0].append(number)
print(f'The odd number are {sorted(numbers[1])}')
print(f'The pair number are {sorted(numbers[0])}')
