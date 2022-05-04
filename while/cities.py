prompt = '\nDigite o nome das cidades que você já tenha visitado:'
prompt += '\n(Digite "quit" quando você terminar.)'

while True:
    city = input(prompt)
    if city == 'quit':
        break
    else:
        print(f'Eu adoraria ir para {city.title()}!')

