favorite_places = {
    'kedson': {
        'location1': 'complexo', 'location2': 'exclusive',
    },
    'bruno': {
        'location1': 'guara', 'location2': 'hostel',
    },
    'fabricio': {
        'location1': 'exclusive', 'location2': 'gela',
    },
}

for name, favorite_locales in favorite_places.items():
    print(f"Os lugares preferido de {name.title()} é \n"
          f"\t{favorite_locales['location1'].title()} e"
          f"\t{favorite_locales['location2'].title()}!")
