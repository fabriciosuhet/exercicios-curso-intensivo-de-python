def get_formatted_name(first_name, last_name):
    full_name = f'{first_name} {last_name}'
    return full_name.title()


# Este é um loop infinito!
while True:
    print('\nPor favor me diga seu nome'
          '\nDigite "q" para sair.')
    f_name = str(input('Primeiro nome: ')).lower()
    if f_name == 'q':
        break
    l_name = str(input('Último nome: ')).lower()
    if l_name == 'q':
        break
    formatted_name = get_formatted_name(f_name, l_name)
    print(f'Olá, {formatted_name}!')
