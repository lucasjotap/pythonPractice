# First we create a dictionary for each person's favorite places.
# This dictionary is special in that it has lists as values.
favorite_place = {
    'carrie':['central park', 'monaco', 'santa monica pier'],
    'louise':['love park', 'maui', 'santa monica pier'],
    'mary':['yellow stone', 'bordeaux', 'marseille']
}

# Secondly we create a for loop to loop through the keys and values
for name, favorite_place in favorite_place.items():
    print(f"\n{name.title()}'s favorite places are: ")
    # Since we grabbed the lists with 'favorite_place', all you have to do is loop through it.
    for favorite_places in favorite_place:
        print(favorite_places)