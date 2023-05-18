blocos = int(input("Digite a quantidade de blocos: "))
camada = 0
i = 1
while(True):
    blocos = blocos - i
    camada = i
    if(blocos <= camada) :
        break
    else :
        print("camada ", camada, ", blocos: ", i)
    i = i + 1
print("Tamanho da pirâmide: ", camada-1, " blocos")

    
