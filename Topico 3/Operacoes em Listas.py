# Uma variável comum copia seu valor se for clonada, uma lista copia seu endereço
# de memória, por isso se alterar uma lista copiada, alterará a lista original tbm
list1 = [1]

a = 1
b = a
a = 2
print(b)
print()

list1 = [1]
list2 = list1
list1[0] = 2
print(list2)
print()

# Criando uma 'Fatia(list[:])'(copiando o conteúd de uma lista)

list1 = [1]
list2 = list1[:]
list1[0] = 2
print(list1)
print()

# Copiando apenas uma parte definida list[start : end] onde end = posição-1

list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(list1)
list2 = list1[0 : 8]
list3 = list1[0 : -1]
print(list2)
print(list3)
print()

# Deletando fatias

list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
del list1[1 : 6]
print(list1)
print()

list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
del list1[:]
print(list1)
print()

# Deletando Lista inteira

list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
del list1
# print(list1) -> Dá erro

# Verificando elementos na minha lista ( IN e NOT IN )

list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(5 in list1)       # -> True
print(5 not in list1)   # -> False
print(12 in list1)      # -> False
print()


# Verificar Maior Valor 

list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
maior = list1[0]

for i in list1:
    if i > maior:
        maior = i
print(maior)
print()

# Verificar Maior Valor com Fatia

list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
maior = list1[0]

for i in list1[1:]:  #-> Não compara o primeiro valor com ele mesmo
    if i > maior:
        maior = i
print(maior)
print()

# Encontrar a localização de um valor dentro da lista

list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
valor = 5
encontrado = False

for i in range(len(list1)):
    if list1[i] == valor:
        encontrado = True
        break
if encontrado :
    print("Valor encontrado no índice: ", i)
else :
    print("Valor ausente. ")
print()

# Valores na loteria ########################################

loteria = [5, 11, 9, 42, 3, 49]
numEscolhidos = [3, 7, 11, 42, 34, 49]
numAcertos = ["Número:", 0, "índice:", 0]
listAcertos = []
listEscolhidos = []

for i in range(len(loteria)):
    if numEscolhidos[i] == loteria[i]:
        numEsc = int(numEscolhidos[i]) 
        numAcertos[1] = numEsc
        numAcertos[3] = i
        listAcertos.append(numAcertos[:])
print("Valores acertados: ")
print(listAcertos)
   



























