"""requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']
for requested_topping in requested_toppings:
    print(f'Adicionar {requested_topping}.')
print('\nFinalizando a preparação da sua pizza!')"""


"""requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']
for requested_topping in requested_toppings:
    if requested_topping == 'green peppers':
        print('Desculpe, nós não temos pimentão verde agora.')
    else:
        print(f'Adicionar {requested_topping}.')
print('\nFinalizando a preparação da sua pizza!')"""

requested_toppings = []
if requested_toppings:
    for requested_topping in requested_toppings:
        print(f'Adicionando {requested_topping}.')
        print('Finalizando sua pizza!')
else:
    print('Você tem certeza que quer uma pizza simples?')
