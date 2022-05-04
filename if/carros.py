"""cars = ['audi', 'bmw', 'subaru', 'toyota']
for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())"""

"""requested_topping = 'mushrooms'
if requested_topping != 'anchovies':
    print('Hold the anchovies')"""

banned_users = ['andrew', 'carolina', 'david']
user = 'marie'
if user not in banned_users:
    print(f'{user.title()}, você pode comentar uma resposta se quiser. ')
