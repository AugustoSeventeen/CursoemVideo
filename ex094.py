# Putting a dictionary inside a list
datas = dict()
datas_list = list()
female = list()
count = 0
sum = average = 0
over_average = list()
while True:
    datas['name'] = str(input('What name?: '))
    question_genre = datas['genre'] = str(input('What genre [F/M]: ')).lower().strip()
    if question_genre not in 'FfMm':
        datas['genre'] = str(input('Invalid answer, what genre [F/M]: ')).lower().strip()
    if datas['genre'] in 'Ff':
        female.append(datas['name'])
    datas['age'] = int(input('What age?: '))
    sum += datas['age']
    question = str(input('Continue? [Y/N]: ')).lower().strip()[0]
    datas_list.append(datas.copy())
    count += 1
    if question in 'Nn':
        break
print('\033[34m=\033[m' * 40)
print(f'Were registered {count}')
average = sum/count
print(f'''The age average is {average:.0f}''')
print(f'''The women is {female}''')
print(f'''Above-average people are {over_average}''')
