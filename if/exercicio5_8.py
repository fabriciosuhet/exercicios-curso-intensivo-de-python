names = ['fabricio', 'bruna', 'gabriel', 'bruno', 'admin']
for name in names:
    if name == 'admin':
        print(f'Olá {name}, gostaria de ver um relatório de status?')
    else:
        print(f'Olá {name.title()}, seja bem vindo')
