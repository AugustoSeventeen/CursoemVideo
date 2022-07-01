# Learning dictionary
datas = dict()
datas['name'] = str(input('Name: '))
datas['average'] = float(input(f'''{datas["name"]}'s average: '''))
print(f'The name is {datas["name"]}')
print(f'The average is {datas["average"]}')
print('The situation is: ', end='')
if datas['average'] < 6:
    print('\033[31mDisapproved\033[m')
else:
    print('\033[32mApproved\033[m')
