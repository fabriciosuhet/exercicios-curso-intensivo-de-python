favorite_languages = {
    'jen': 'python', 'sarah': 'c', 'fabricio': 'python', 'matheus': 'java',
}

others = ['kedson', 'bruno']
for name in favorite_languages.keys():
    print(f'Obrigado por participar da enquente {name.title()}!')
print('\n')

for other in others:
    if other not in favorite_languages:
        print(f'Venha participar da nossa enquete {other.title()}!')
