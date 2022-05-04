prompt = '\nInforme os ingredientes que deseja na pizza:'
prompt += '\nDigite "quit" quando finalizar!'

while True:
    toppings = input(prompt)
    if toppings == 'quit':
        break
    else:
        print(f'{toppings.title()} foi adicionado à sua pizza. Obrigado!')
