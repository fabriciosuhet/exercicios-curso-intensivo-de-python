"""user_0 = {
    'username': 'efermi', 'first': 'enrico', 'last': 'fermi',
}

for key, value in user_0.items():
    print(f'\nKey: {key}')
    print(f'Value: {value}')"""


"""favorite_languages = {
    'jen': 'python', 'sarah': 'c', 'edward': 'ruby', 'phil': 'python',
}"""

"""for name, language in favorite_languages.items():
    print(f'A linguagem prefeida de {name.title()} é {language.title()}.')"""

"""for name in favorite_languages.keys():
    print(name.title())"""


favorite_languages = {
    'jen': 'python', 'sarah': 'c', 'edward': 'ruby', 'phil': 'python',
}

"""friends = ['phil', 'sarah']
for name in favorite_languages.keys():
    print(name.title())
    if name in friends:
        print(f"Oi {name.title()}, vi que sua linguagem preferida é "
              f"{favorite_languages[name]}!")"""

"""if 'erin' not in favorite_languages.keys():
    print('Erin, por favor pegue nossa enquente')"""

"""for name in sorted(favorite_languages.keys()):
    print(f'{name.title()}, obrigado por fazer a enquete. ')"""


print(f'As seguintes linguagens foram mencionadas: ')
"""for language in favorite_languages.values():
    print(language.title())"""

for language in set(favorite_languages.values()):
    print(language.title())
