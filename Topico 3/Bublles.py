# Bolha: compara o numero a esquerda com o da direita, se o da esquerda for maior
# devera andar para a direita até ser menor que o proximo à direita ou estar na
# última posição (Bolha : a mesma coisa mas de baixo para cima onde o maior fica
# em cima).
myList = [8, 10, 6, 2, 4]
print(myList)
# Organizando Crescente manualmente: 
'''
swapped = True
print()
while swapped :
    swapped : False
    for i in range(len(myList) -1):
        if myList[i] > myList[i + 1]:
            swapped = True
            myList[i], myList[i+1] = myList[i + 1], myList[i]
            print(myList)
print()
'''
# Organizando Crescente com Python :

myList.sort()
print(myList)
print()

# Organizando Decrescente com Python :

myList.reverse()
print(myList)
print()
