person = {
    'jimi':'guitar',
    'song' : ['foxy lady', 'purple haze', 'little wing']
}

print('')

if 'guitar_used' not in person.keys():
    print("The guitars jimi used were no added in the dictionary")

for x in person['song']: 
    print(x)
print('\n')
for x in person.values():
    print(x)