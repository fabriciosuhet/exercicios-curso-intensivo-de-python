sandwich_orders = ['big mac', 'podrão', 'whooper', 'stacker', 'big tasty', ]
finished_sandwiches = []

while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    print(f'Preparando o sanduíche {current_sandwich.title()}...')
    finished_sandwiches.append(current_sandwich)

print('\n')
for finished_sand in finished_sandwiches:
    print(f'Sanduíches preparados: \n'
          f'\t{finished_sand.title()}')
