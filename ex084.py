# Reading name and weight, showing how many people, the heaviest ones and the lightest one
people = []
data = []
counter = 0
heaviest = lightest = 0
while True:
    # question.
    data.append(str(input('What name?: ')))
    data.append(float(input('What weight?: ')))
    # Finding the heavier and lightest one.
    if len(people) == 0:
        heaviest = lightest = data[1]
    else:
        if data[1] > heaviest:
            heaviest = data[1]
        if data[1] < lightest:
            lightest = data[1]
    # Counter.
    counter += 1
    # Put Data list into People lis.
    people.append(data[:])
    # Cleaning Data list.
    data.clear()
    # Questioning if person want to continue.
    question = str(input('Continue? [Y/N]: ')).strip().lower()[0]
    # Loop in the same question if person Don't answer correctly.
    while question not in 'NnYy':
        question = str(input('Invalid answer, continue? [Y/N]: '))
    # To stop if person choose 'no'.
    if question in 'Nn':
        break
# Datas about the survey:
print(f'You registered {counter} people')
print(f'The heaviest person/people has \033[32m{heaviest}\033[m Kg and is/are: ', end='')
# Finding the heaviest name:
for person in people:
    if person[1] == heaviest:
        print(f'\033[34m{person[0]}\033[m', end=' ')
print(f'The lightest person/people has \033[32m{lightest}\033[m Kg and is/are')
# Finding the lightest name:
for person in people:
    if person[1] == lightest:
        print(f'\033[34m{person[0]}\033[m', end='')
