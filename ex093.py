# Registration of a football player
datas = dict()
games = list()
datas['name'] = str(input('Player name: '))
tot = int(input(f'How many games {datas["name"]} played'))
for c in range(0, tot):
    games.append(int(input(f'How many goal in match {c}?')))
datas['goals'] = games[:]
datas['total'] = sum(games)
print('\033[33m=\033[m' * 40)
print(datas)
print('\033[33m=\033[m' * 40)
for k, v in datas.items():
    print(f'The field {k} has the value {v}.')
print('\033[33m=\033[m' * 40)
print(f'The player {datas["name"]} played {len(datas["goals"])} games')
for i, v in enumerate(datas['goals']):
    print(f'In game {i} the player {datas["name"]} did {v}')
print(f'A total of {datas["total"]}')