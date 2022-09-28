person  = {
    'first_name' : 'john',
    'second_name' : 'lennon',
    'age' : 40,
    'city' : 'liverpool'
}

print(f"{person['first_name'].title()} {person['second_name'].title()}  was {person['age']} and he was born in {person['city'].title()}")

print("%s %s"% (person['first_name'].title(), person['second_name'].title()))