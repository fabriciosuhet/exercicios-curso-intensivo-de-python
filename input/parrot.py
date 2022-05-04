"""message = input('Diga me algo, e eu vou repetir de volta pra você: ')
print(message)"""

"""name = input('Por favor, digite seu nome: ')
print(f'Olá, {name}!')"""

"""prompt = 'Se você nós dizer quem você é, podemos personalizar as mensagens' \
         'que você vê'

prompt += '\nQual o seu primeiro nome? '
name = input(prompt)
print(f'Olá, {name}!')"""

height = int(input('Qual sua altura, em polegadas? '))
if height >= 36:
    print('\nVocê é alto suficiente para andar.')
else:
    print('\nVocê poderá andar quando for mais velho.')
