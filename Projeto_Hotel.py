
def reservar(rsvEdfc, rsvAnd, rsvQat, quartosReservados, listaDeReservas):
    reservado = True
    
    hotel[rsvEdfc - 1][rsvAnd - 1][rsvQat - 1] = reservado
    quartosReservados[1] = (rsvEdfc)
    quartosReservados[3] = (rsvAnd)
    quartosReservados[5] = (rsvQat)
    listaAuxiliar = quartosReservados[:]
    listaDeReservas.append(listaAuxiliar)
    
    return (quartosReservados, listaDeReservas)
    
hotel = [[[ False for quartos in range(5)] for andares in range(5)] for edificios in range(3)]
#print(hotel)
quartosReservados = ["Edifício:", 0, "Andar:", 0, "Quarto:", 0]
listaDeReservas = []
reservados = 0
totalQuartos = len(hotel) * len(hotel[0]) * len(hotel[0][0])
quartosDisponiveis = 0
loop = 0

qtdReservar = int(input("Olá, quantos quartos deseja reservar hoje? "))
while loop < qtdReservar:
    print() 
    quartosDisponiveis = totalQuartos - reservados 
    print("Quartos já reservados: ", reservados)
    print("Quartos disponíveis: ", quartosDisponiveis)
    print()
    rsvEdfc = int(input("Em qual edifício gostaria de alugar o quarto? (1 à {edificio}): ".format(edificio=len(hotel))))
    rsvAnd  = int(input("Em qual andar gostaria de alugar o quarto? (1 à {andar}): ".format(andar=len(hotel[0]))))
    rsvQat  = int(input("Em qual quarto gostaria de se alojar? (1 à {quarto}): ".format(quarto=len(hotel[0][0]))))
    
    if hotel[rsvEdfc - 1][rsvAnd - 1][rsvQat - 1] == True :
        print("Desculpe, este quarto não está disponível no momento, por favor, escolha outro quarto.")
        continue
    reservar(rsvEdfc, rsvAnd, rsvQat, quartosReservados, listaDeReservas)
    reservados += 1
    loop+=1

print()
print("Quartos reservados: ")
print(listaDeReservas)

