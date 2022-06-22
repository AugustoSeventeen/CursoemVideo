# Read 4 value and save in a list, tell what is the highest and lowest, and position
numbers = []
for question in range(0, 5):
    questions = int(input('Enter a number: '))
    numbers.append(questions)
print(f'The highest value is \033[32m{max(numbers)}\033[m and it is in \033[34m{numbers.index(max(numbers)) + 1}ª\033[m'
      f' position')
print(f'The lowest value is \033[32m{min(numbers)}\033[m and it is in \033[34m{numbers.index(min(numbers)) + 1}ª\033[m'
      f' position')
