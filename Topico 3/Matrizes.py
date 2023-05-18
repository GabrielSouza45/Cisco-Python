# Compreensão : Lista criada durante a execução do programa
squares = [x ** 2 for x in range(10)]
print(squares)
print()

EMPTY = []
board = []
for i in range(8):
    row = [EMPTY for i in range(8)]
    board.append(row)
print (board)

EMPTY2 = []
board2 = [[EMPTY2 for i in range(8)] for j in range(8)]
print(EMPTY2)

ROOK = "ROOK"
KNIGHT = "KNIGHT"
PAWN = "PAWN"
board2[0][0] = ROOK
board2[0][7] = ROOK
board2[7][0] = ROOK
board2[7][7] = ROOK

board2[4][2] = KNIGHT
print(board2)
