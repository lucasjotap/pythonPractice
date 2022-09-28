game = {}

game['producer'] = "rockstar"
game['game'] = 'RDR2'

print (game)
del game['producer']
print(game)

for x, y in game.items():
    print(x)
    print(y)