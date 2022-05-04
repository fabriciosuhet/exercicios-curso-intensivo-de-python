pets = {
    'mel': {
        'type': 'cachorro', 'name': 'edilma',
    },
    'lupita': {
        'type': 'cachorro', 'name': 'karen',
    },
    'rio': {
        'type': 'passaro', 'name': 'fabricio',
    },
}

for pet, pet_info in pets.items():
    print(f"Nome do animal: {pet.title()}.")
    print(f"\tAnimal: {pet_info['type'].title()}.")
    print(f"\tDono: {pet_info['name'].title()}.\n")
