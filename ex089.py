# Reading names and notes of many people, showing the average and showing the note of people.
datas = []
while True:
    name = str(input('What is the name?: '))
    first_note = float(input('What is the 1° note?: '))
    second_note = float(input('What is the 2° note?: '))
    average = (first_note + second_note) / 2
    datas.append([name, [first_note, second_note], average])
    question = str(input('Continue? [Y/N]: ')).strip().lower()[0]
    if question not in 'YyNn':
        question = str(input('Invalid answer! Continue? [Y/N]: '))
    if question in 'Nn':
        break
print(f'=' * 40)
print(f'{"N°":<4}{"Name":<10}{"Average":>8}')
print(f'=' * 40)
for i, a in enumerate(datas):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')
while True:
    print('-' * 35)
    question2 = int(input('Show witch student grande? [999 to stop]: '))
    if question2 == 999:
        break
    if question2 <= len(datas) - 1:
        print(f'{datas[question2][0]} is {datas[question2][1]}')
