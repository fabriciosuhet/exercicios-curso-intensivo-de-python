"""alien_0 = {'color': 'green', 'points': 5}
print(alien_0['color'])
print(alien_0['points'])

new_points = alien_0['points']
print(f'você acabou de ganhar {new_points} pontos!')

alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)"""

"""alien_0 = {}

alien_0['color'] = 'green'
alien_0['points'] = 5
print(alien_0)"""

"""alien_0 = {'color': 'green'}
print(f"O alien é {alien_0['color']}.")
alien_0['color'] = 'yellow'
print(f"O alien agora é {alien_0['color']}.")"""

"""alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
print(f"Oiriginal posição: {alien_0['x_position']}")
if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    x_increment = 3

alien_0['x_position'] += x_increment
print(f"Nova posição x: {alien_0['x_position']}")"""


alien_0 = {'color': 'green', 'points': 5}
print(alien_0)
del alien_0['points']
print(alien_0)

