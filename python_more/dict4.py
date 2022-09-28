x = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

for key, value in x.items():

    if key == 'jen':
        # Tell her she's pretty.
        print(f"Hey {key.title()}, you're very pretty.")
        print(f"{key.title()} likes {value}.\n")
    elif key == 'sarah':
        print(f"You are pretty too {key.title()}")
        print(f"{key.title()} likes {value}.")
