# Read 4 value and save in a list, tell what is the highest and lowest, and position
numbers = []
lar = 0
low = 0
for question in (range(0, 5)):
    numbers.append(int(input('Enter a number: ')))
    if question == 0:
        lar = low = numbers[question]
    if numbers[question] > lar:
        lar = numbers[question]
    if numbers[question] < low:
        low = numbers[question]
print(f'The highest value is \033[32m{lar}\033[m and it is in', end=' ')
for position, item in enumerate(numbers):
    if item == lar:
        print(position, end=', ')
        print('positions', end=', ')
print(f'\nThe lowest value is \033[32m{low}\033[m and it is in ', end=' ')
for position, item in enumerate(numbers):
    if item == low:
        print(position, end=', ')
        print('positions', end=' ')
