# Improving dictionary
datas = dict()
games = list()
team = list()
while True:
    # cleaning the dictionary in each loop
    datas.clear()
    # adding a value on dictionary
    datas['name'] = str(input('Player name: '))
    # adding a value on tot
    tot = int(input(f'How many games {datas["name"]} played'))
    # creating a loop to add the goals in each match
    games.clear()
    for c in range(0, tot):
        # adding the goals of each match in list games
        games.append(int(input(f'How many goal in match {c}?')))
    # adding the goals on dictionary
    datas['goals'] = games[:]
    # adding up the goals
    datas['total'] = sum(games)
    # putting the dictionary in list
    team.append(datas.copy())
    # creating a loop to question Y or N
    while True:
        answer = str(input('Continue? [Y/N]:')).upper()[0]
        # variable if user type wrong value
        if answer not in 'YyNn':
            str(input('Invalid answer, continue? [Y/N]:'))
        # variable if user type some of right values
        if answer in 'NY':
            break
    # variable to stop the program
    if answer == 'N':
        break
print('-' * 40)
print('cod', end='')
for i in datas.keys():
    print(f'{i:<15}', end='')
print()
print('\033[33m=\033[m' * 40)
for k, v in enumerate(team):
    print(f'{k:>4}', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
        print()
print('-' * 40)
while True:
    searching = int(input('Show datas from which player?[999 to stop]: '))
    if searching == 999:
        break
    if searching >= len(team):
        print(f'Error, there is no plaer with this code {searching}')
    else:
        print(f' -- PLAYER TABLE {team[searching]["name"]}')
        for i, g in enumerate(team[searching]['goals']):
            print(f'    Inthe game {i} make {g} goals')
    print('-' * 40)
print('<< CHECK BACK OFTEN >>')
