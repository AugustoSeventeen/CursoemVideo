# worker data
from datetime import date
data = dict()
data['name'] = str(input('Name: '))
birth_year = int(input('Year birth: '))
data['age'] = date.today().year - birth_year
work_card = data["CTPS"] = int(input('Work card (0 to no): '))
if work_card == 0:
    print('\033[33m=\033[m' * 40)
    print(f'Name has value {data["name"]}')
    print(f'Age has value {data["age"]}')
    print(f'CTPS has value {data["CTPS"]}')
else:
    data['hire_year'] = int(input('Year of hire: '))
    data['salary'] = float(input('Salary: '))
    data["retire"] = (data['hire_year'] - birth_year) + 35
    print('\033[33m=\033[m' * 40)
    print(f'Name has value {data["name"]}')
    print(f'Age has value {data["age"]}')
    print(f'CTPS has value {data["CTPS"]}')
    print(f'Year of hire has value {data["hire_year"]}')
    print(f'Salary has the value {data["salary"]}')
    print(f'Retirement has the value {data["retire"]}')
