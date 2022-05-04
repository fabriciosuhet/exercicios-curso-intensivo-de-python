current_users = ['fabricio', 'bruna', 'bruno', 'gabriel', 'tata']
new_users = ['kedson', 'mateus', 'fabricio', 'bruna']

for new_user in new_users:
    if new_user in current_users:
        print(f'usuario {new_user} indisponivel')
    else:
        print(f'usuario {new_user} disponivel')
