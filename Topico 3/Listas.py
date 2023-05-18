myList = [] #cria uma lista vazia
numbers = [10, 5.1, 8.5, "2", 1]
print (numbers)
myList2 = []

'''
soma =0
for i in numbers :
    soma = soma + int(i)
    print (soma)
print (soma)
'''
#
'''
print("Antiga posição 2: ",numbers[2])
numbers[2] = 13
print("Nova posição 2: ",numbers[2])
print()

print("Length: ", len(numbers)) # len(lista) pega o tamanho da lista
print()

print("Antiga posição 1: ",numbers[1])
del numbers[1]
print("Nova posição 1: ",numbers[1])
print()

print("Length Atual: ", len(numbers))
print("Lista Atual :", numbers)
print()

# Índices negativos percorrem a lista de trás para frente
print("Ultimo da lista: ", numbers[-1]) # Índice -1 mostra o último item da lista
print("Penúltimo da lista: ", numbers[-2]) # Índice -2 mostra o penúltimo item da lista
print()

# Adicionar elementos na lista:
# append() -> Adiciona no final da lista 
numbers.append(45)
print(numbers)
print()

# insert() -> adiciona na localização desejada (local, valor)
numbers.insert(0, 222)
print(numbers)
print()
'''
#

# myList
'''
for i in range(5): # adiciona todos um após o outro
    myList.append(i+1)
    print(myList)
print(myList)
print()
'''

# MyList2

for i in range(5): # adiciona todos na posição zero
    myList2.insert(0, i+1)
    print(myList2)
print(myList2)
print()


for i in myList2: # Percorre a myList2
    print(i)
print()

#Inversão de valores

print(myList2)
myList2[0], myList2[4] = myList2[4], myList2[0] #Inverte a primeira posição com a última
myList2[1], myList2[3] = myList2[3], myList2[1] #Inverte a segunda posição com a penúltima
print(myList2)
print()

# Inversão valores de forma automática com for

length = len(myList2)
for i in range (length //2) :
    myList2[i], myList2[length - i - 1] = myList2[length - i - 1], myList2[i]
print(myList2)
print()




























