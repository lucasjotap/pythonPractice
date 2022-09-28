person_one  = {
    'first_name':'queen',
    'second_name':'elizabeth',
    'age': 96,
    'city':'london'
}

person_two  = {
    'first_name':'dakota',
    'second_name':'fanning',
    'age': 28,
    'city':'conyers'
}

person_three  = {
    'first_name':'kristen',
    'second_name':'stewart',
    'age': 31,
    'city':'l.a'
}

people = [person_one, person_two, person_three]

print("These are some of the prominet women from the XXI century:")

for x in people:
    print(f"{x['first_name'].title()} {x['second_name'].title()} is from {x['city'].title()} and was born in {2022 - x['age']}")
