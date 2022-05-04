#def get_formatted_name(first_name, last_name):
    #"""Devolve um nome completo formatado de modo elegante."""
    #full_name = f'{first_name} {last_name}'
    #return full_name.title()


"""musician = get_formatted_name('jimi', 'hendrix')
print(musician)"""


#def get_formatted_name(first_name, middle_name, last_name):
    #"""Devolve um nome completo formatado de modo elegante."""
    #full_name = f'{first_name} {middle_name} {last_name}'
    #return full_name.title()


"""musician = get_formatted_name('john', 'lee', 'hooker')
print(musician)"""


def get_formatted_name(first_name, last_name, middle_name=''):
    """Devolve um nome completo formatado de modo elegante."""
    if middle_name:
        full_name = f'{first_name} {middle_name} {last_name}'
    else:
        full_name = f'{first_name} {last_name}'
    return full_name.title()


musician = get_formatted_name('jimi', 'hendrix')
print(musician)

musician = get_formatted_name('john', 'hooker', 'lee')
print(musician)
