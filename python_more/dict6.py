fav_number = {
    'lee' : '4',
    'john' : '3',
    'ellie' : '7',
    'chloe' : '10',
    'paul' : '11'
}

for key, value in fav_number.items(): 
    print(f"{key.title()}'s favorite number is {value}.")
print("\n")
for key in fav_number.keys(): 
    print(f"{key.title()} is a key in the dictionary.")
print("\n")
for value in fav_number.values(): 
    print(f"{value} is a value in the dictionary.")