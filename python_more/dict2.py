person = {}

person['name'] = 'Mary'
person['location'] = 'Texas'
person['car'] = 'Tesla Model S'

print(person['name'] + "'s car is a " + person['car'] + '.')

# Changing value in dictionary.
person['car'] = 'Land Rover'


# Creating a little program for the dictionary.

if person['name'] == 'Mary':
    person['points_earned'] = 10
    print('Hello Mary!')
    print(f"You have earned {person['points_earned']} points {person['name']}")

    if person['car'] == 'Land Rover':
        print(f"You drive a {person['car']}")
        if True:
            plus = 1
            person['points_earned'] += plus
            print(f"This is your total score so dar {person['points_earned']}")
    else:
        print(f"You drive a {person['car']}")