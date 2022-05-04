responses = {}

# Define uma flag para indicar que a enquete está ativa

polling_active = True

while polling_active:
    # Pede o nome da pessoa e a resposta
    name = str(input('\nQual o seu nome? '))
    response = str(input('Qual montanha você gostaria de escalar um dia? '))
    # Armazena a resposta no dicionário
    responses[name] = response

    # Descobre se outra pessoa vai responder à enquete
    repeat = str(input('Você gostaria de deixar outra pessoa responder? (s/n)')).lower()
    if repeat == 'n':
        polling_active = False

# A enquete foi concluída. Mostra os resultados
print('\n--- Resultados da enquete ---')
for name, response in responses.items():
    print(f'{name.title()} gostaria de escalar {response.capitalize()}.')
