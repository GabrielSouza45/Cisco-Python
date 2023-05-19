# Compreensão : Lista criada durante a execução do programa
squares = [x ** 2 for x in range(10)]
print(squares)
print()
'''
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
'''
# Termometro
'''
temperatura = [[0.0 for hora in range(20)] for dia in range(31)]
print(temperatura)
'''
# Matrizes Tridimensionais
'''
hotel = [[[ False for quartos in range(20)] for andares in range(15)] for edificios in range(3)]
#print(hotel)
print()

qtdReservar = int(input("Olá, quantos quartos deseja reservar hoje? "))

quartosReservados = ["Edifício:", 0, "Andar:", 0, "Quarto:", 0]
listaDeReservas = []
reservar = True
reservados = 0
w = 0

print() 
while w < qtdReservar:
    print("Quartos já reservados: ", reservados)
    print()
    rsvEdfc = int(input("Em qual edifício gostaria de alugar o quarto? (1, 2 ou 3) "))
    rsvAnd  = int(input("Em qual andar gostaria de alugar o quarto? (1 à 15) "))
    rsvQat  = int(input("Em qual quarto gostaria de se alojar? (1 à 20) "))
    
    if hotel[rsvEdfc - 1][rsvAnd - 1][rsvQat - 1] == True :
        print("Desculpe, este quarto não está disponível no momento, tente algum outro.")
        continue
    
    hotel[rsvEdfc - 1][rsvAnd - 1][rsvQat - 1] = reservar
    quartosReservados[1] = (rsvEdfc)
    quartosReservados[3] = (rsvAnd)
    quartosReservados[5] = (rsvQat)
    listaAuxiliar = quartosReservados[:]
    listaDeReservas.append(listaAuxiliar)

    reservados += 1 
    w+=1
print("Quatidade de quartos reservados: ", reservados)
print("Quartos reservados: ")
print(listaDeReservas)

#print(hotel)
quartosReservados = ["Edifício:", 0, "Andar:", 0, "Quarto:", 0]
listaDeReservas = []
reservados = 0

print ()

for edi in range(3):
    for floor in range(15):
        for qat in range(20):
            if hotel[edi][floor][qat] == True:
                quartosReservados[1] = (edi+1)
                quartosReservados[3] = (floor+1)
                quartosReservados[5] = (qat+1)
                listaAuxiliar = quartosReservados[:]
                listaDeReservas.append(listaAuxiliar)
                reservados += 1
print("Quatidade de quartos reservados: ", reservados)
print("Quartos reservados: ")
print(listaDeReservas)
'''

my_list = [[0, 1, 2, 3] for i in range(2)]
print(my_list[2][0])

