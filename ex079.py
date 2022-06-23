# Read number, don't repeat number and put in ascending order
numbers = []
while True:
    number = int(input('\033[32mType a number: \033[m'))
    while number in numbers:
        number = int(input('\033[31mThis number already exist, type other: \033[m'))
    if number not in numbers:
        numbers.append(number)
    question = str(input('Continue [Y/N]: ')).strip().upper()[0]
    if question in 'Nn':
        break
    while question not in 'Yy':
        question = str(input('Continue [Y/N]: ')).strip().upper()[0]
print(f'You Typed {numbers}')

# Here first I put a True loop for question, created a list with this question, while number is in list a say for people
# type other number till this number not in list, if the number not in list I add this number in list with function
# lis.append() and the number people choose, after this make the question if person want to stay typing numbers, if the
# answer is in 'Nn' I break the True loop, if answer not Yy or Nn I put a loop to stay questioning till the person
# answer correctly, if question is in 'Yy' the True loop continue
