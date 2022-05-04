favorite_number = {
    'fabricio': {
        'number1': 1, 'number2': 10,
    },
    'bruno': {
        'number1': 7, 'number2': 11,
    },
    'kedson': {
        'number1': 10, 'number2': 24,
    }
}

for name, number in favorite_number.items():
    print(f"Os números preferidos de {name.title()} são: "
          f"{number['number1']} e {number['number2']}!")
