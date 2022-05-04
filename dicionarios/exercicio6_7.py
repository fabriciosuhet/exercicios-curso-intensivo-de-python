person_1 = {
    'first': 'fabricio', 'last': 'suhet', 'age': 22, 'city': 'brasilia',
}

person_2 = {
    'first': 'bruno', 'last': 'mario', 'age': 20, 'city': 'brasilia',
}

person_3 = {
    'first': 'kedson', 'last': 'mario', 'age': 23, 'city': 'brasilia',
}

people = [person_1, person_2, person_3]

for user_info in people:
    full_name = user_info['first'] + " " + user_info['last']
    age = user_info['age']
    location = user_info['city']
    print(f"\tNome completo: {full_name.title()}")
    print(f"\tIdade: {age}")
    print(f"\tCidade: {location.title()}\n")
