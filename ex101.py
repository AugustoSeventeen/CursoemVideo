# Analyzing whether a person can vote.
from datetime import date


def vote(year):
    age = date.today().year - birth_year
    if age < 16:
        return f'\033[31mDenied Vote!\033[m'
    elif 16 <= age < 18 or age > 65:
        return f'\033[33mOptional Vote!\033[m'
    else:
        return f'\033[32mMandatory Vote!\033[m'


birth_year = int(input('\033[36mWhat year were you born?: \033[m'))
print(vote(birth_year))