river = {
    'nilo': 'egito', 'rio amazonas': 'brasil', 'são francisco': 'brasil',
}

for key, value in river.items():
    print(f'O rio {key.title()} corre pelo {value.title()}.')
print('\n')


for key in river.keys():
    print(f'{key.title()}')
print('\n')

for value in river.values():
    print(f'{value.title()}')
