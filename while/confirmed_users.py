unconfirmed_users = ['alice', 'brian', 'candace', ]
confirmed_users = []

# Verifica cada usuário até que não haja mais usuários não confirmados
# Transfere cada usuário verificado para a lista de usuários confirmados

while unconfirmed_users:
    current_user = unconfirmed_users.pop()
    print(f'Verificando usuário: {current_user.title()}')
    confirmed_users.append(current_user)

# Exibe todos os usuários confirmados

print('\nOs usuários a seguir estão confirmados: ')
for confirmed_user in confirmed_users:
    print(confirmed_user.title())
