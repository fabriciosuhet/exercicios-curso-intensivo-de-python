pizzas = ['calabresa', 'frango catupiry', 'portuguesa']
friend_pizzas = pizzas[:]
pizzas.append('peperoni')
friend_pizzas.append('bacon')
print('Minhas pizzas favoritas são: ')
for pizza in pizzas:
    print(f'{pizza.capitalize()}')
print('\nAs pizzas favorita do meu amigo são: ')
for pizza in friend_pizzas:
    print(pizza.capitalize())
