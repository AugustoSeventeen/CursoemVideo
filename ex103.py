# Analyzing a player's name and gols.


def fold(name='<Unknown>', gols=0):
    print(f'\033[31mThe player \033[m\033[36m{name}\033[m \033[31mdid\033[m \033[36m{gols}\033[m \033[31m gols in the '
          f'game.\033[m')


print('\033[33m=\033[m' * 126)
player_name = str(input("\033[34mName's player?: \033[m"))
print('\033[33m=\033[m' * 126)
gols_player = str(input('\033[35mHow many gols the player did?: \033[m'))
print('\033[33m=\033[m' * 126)
if gols_player.isnumeric():
    gols_player = int(gols_player)
else:
    gols_player = 0
if player_name.strip() == '':
    fold(gols=gols_player)
else:
    fold(player_name, gols_player)

