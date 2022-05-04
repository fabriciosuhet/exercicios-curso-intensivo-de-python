"""favorite_languages = {'jen': 'python', 'sarah': 'c', 'edward': 'ruby', 'phil': 'python', }
print(f"A linguagem favorita de Sarah é {favorite_languages['sarah'].title()}.")"""


favorite_languages = {
    'jen': ['python', 'ruby'], 'sarah': ['c'], 'edward': ['ruby', 'go'],
    'phil': ['python', 'haskell'],
}

for name, languages in favorite_languages.items():
    print(f"\n {name.title()} sua linguagem favorite é: ")
    for language in languages:
        print(f"\t {language.title()}")

