# Armazena informações sobre uma pizza que está sendo pedida
pizza = {
    'crust': 'thick', 'toppings': ['murshrooms', 'extra chesse'],
}

# Resume o pedido
print(f"Você pediu a {pizza['crust']}-crust pizza com os seguintes recheios: ")
for topping in pizza['toppings']:
    print(f"\t {topping}")
