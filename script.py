board = []
def create_board():
    for i in range(3):
        row = []
    for j in range(3):
        row.append('-')
    board.append(row)
    return board

burd = create_board()
print(burd)