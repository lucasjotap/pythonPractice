rivers = { 
    'nile' : 'egypt',
    'sao francisco' : 'brazil',
    'thames' : 'england'
}

for key, values in rivers.items():
    print(f"{key.title()} runs in {values.title()}")
print("\n")
for key in rivers.keys():
    print(f"{key.title()} is a river")
print("\n")
for value in rivers.values():
    print(f"{value.title()} is a country")