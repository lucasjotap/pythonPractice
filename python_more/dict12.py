# Creating an empty list for storing aliens
alien = []

# Creating aliens and stating a new variable called alien_number.
for alien_number in range(10):
    new_alien = {'color':'green', 'points': 5, 'speed' : 'slow'}
    alien.append(new_alien)

# Selecting the first three aliens that have been appended to the list of new aliens.
for x in alien[:3]:
    if x["color"].lower() == 'green':
        x['color'] = "blue"
        x['points'] = 10
        x["speed"] = "medium"
    
for x in alien[:5]:
    print(x)