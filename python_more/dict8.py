favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

# Code is broken
#for name in favorite_languages:
#   if name[0].lower() == 'j' or 's':
#        print("%s is a friend." % (name))
#    else:
#        print("%s isn't a friend but an acquaintance."% (name))


# This works as intended a little better.
friends = []
for name in favorite_languages:
    if name == 'sarah':
        print("Hey Sarah")
        friends.append(name)
    elif name == 'jen':
        print("Hey Jen")
        friends.append(name)

print(friends)