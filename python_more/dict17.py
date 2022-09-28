maggie = {
    'animal' : 'dog', 
    'owner' : 'tom'
}

trevor = {
    'animal' : 'lizard', 
    'owner' : 'carl'
}

lassie = {
    'animal' : 'parrot', 
    'owner' : 'barbara'
}

moonie = {
    'animal' : 'cat', 
    'owner' : 'luke'
}

dictionaries = [maggie, trevor, lassie, moonie]

for x in dictionaries: 
    print(f"{x['owner'].title()} owns a pet {x['animal']}.")