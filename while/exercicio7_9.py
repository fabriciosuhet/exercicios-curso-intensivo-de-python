sandwich_orders = ['big mac', 'pastrami', 'podrão', 'whooper', 'pastrami', 'stacker',
                   'big tasty', 'pastrami', ]

finished_sandwiches = []

# Percorre todos os sanduíches disponíveis em sandwich_orders
for sandwich in sandwich_orders:
    print(f'Sanduíches disponíveis: {sandwich.title()}')

print('\nInfelizmente estamos sem pastrami...\n')

# Remove todos os valores 'pastrami' da lista sandwich_orders
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

# Move todos os valores que sobraram depois de pastrami ser removido e
# adiciona numa nova lista
while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    finished_sandwiches.append(current_sandwich)

# Percorre a lista finished_sandwiches e mostra agora todos os valores disponíveis
for finished_sandwich in finished_sandwiches:
    print(f'Sanduíches disponíveis: '
          f'{finished_sandwich.title()}')
