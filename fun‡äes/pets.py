# def describe_pet(animal_type, pet_name):
# """Exibe informações sobre um animal de estimação"""
# print(f'\nEu tenho um {animal_type}.')
# print(f'\nMeu {animal_type} se chama {pet_name.title()}.')


"""describe_pet('hamster', 'harry')
describe_pet('cachorro', 'lupita')
describe_pet('harry', 'hamster')"""


# describe_pet(animal_type='hamster', pet_name='harry')


def describe_pet(pet_name, animal_type='cachorro'):
    """Exibe inforamções sobre um animal de estimação"""
    print(f'Eu tenho um {animal_type}.')
    print(f'Meu {animal_type} se chama {pet_name.title()}.')


describe_pet(pet_name='lilie')

# Um cachorro chamado Willie
describe_pet('willie')
describe_pet(pet_name='willie')

# Um hamster chamado harry
describe_pet('harry', 'hamster')
describe_pet(pet_name='harry', animal_type='hamster')
describe_pet(animal_type='hamster', pet_name='harry')
