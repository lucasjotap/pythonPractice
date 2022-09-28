favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}
friend = []
for x in favorite_languages.keys():
    if x.lower() == 'sarah':
        print(f"Hey {x}")
        friend.append(x)
        print(x[0].title())