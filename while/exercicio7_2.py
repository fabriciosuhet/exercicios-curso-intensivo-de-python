prompt = '\nInforme quantas pessoas irão jantar:' \
         '\nDigite "quit" para finalizar o programa!'

while True:
    peoples = str(input(prompt).lower())
    if peoples == 'quit':
        print('Finalizando... Obrigado!')
        break
    elif peoples > '8':
        print('Vocês deverão esperar por uma mesa!')
    else:
        print('Sua mesa está pronta!')
