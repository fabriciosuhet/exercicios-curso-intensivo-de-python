cities = {
    'brasilia': {
        'country': 'brasil', 'population': '3.094.325',
        'fact': 'brasília é uma das únicas cidades modernas do mundo'
                ' a receber o título de Patrimônio Cultural da Humanidade'
                ' pela UNESCO'
    },
    'são paulo': {
        'country': 'brasil', 'population': '11.253.503',
        'fact': 'os Paulistas consomem mais de 1 milhão de pizzas por dia'
    },
    'santa catarina': {
        'country': 'brasil', 'population': '7.338.443',
        'fact': 'em 1526, o italiano Sebastião Caboto denominava em seus mapas'
                ' as terras catarinenses como “Porto dos Patos”'
    },
}

for name, city_info in cities.items():
    print(f"{name.title()} fica no {city_info['country'].title()}, "
          f"tem uma população de {city_info['population']} pessoas "
          f"e um fato interessante sobre é: \n\t{city_info['fact'].capitalize()}.\n")
