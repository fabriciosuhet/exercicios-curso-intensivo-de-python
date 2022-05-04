responses = {}

# Flag para informar que a enquete está ativa.
polling_active = True

while polling_active:
    # Pede o nome e as férias dos sonhos.
    name = str(input('Qual o seu nome? '))
    response = str(input('Se pudesse visitar um lugal do mundo,'
                         ' para onde você iria? '))
    # Armazena as respostas no dicionário.
    responses[name] = response

    # Descobre se quer adicionar outra resposta.
    repeat = str(input('Você gostaria de adicionar mais locais '
                       'que gostaria de visitar? (s/n)')).lower()
    if repeat == 'n':
        polling_active = False  # Desativa a flag da enquete

# Enquete finalizada, mostra os resultados.
print('\n=== Resultado da enquete ===')
for name, response in responses.items():
    print(f'{name.title()} gostaria de ir para: {response.title()}')
