# Tipos de sequência e mutabilidade
# Sequencias são dados que podem ser processados pelo for(Listas, matrizes, ect)

# Mutabilidade:
    # Mutáveis: são dados que podem sofrer alterações durante a execução do código
        # (operação in situ, posições -> list.append(1) ex.) 
    # Imutáveis: Tuplas, dados que não podem sofrer alterações durante a execução do codigo
        # (Listas que para serem modificadas, deverão ser criadas novamente do zero ex.)
#Tuplas
    # Deve ter seu valor finalizado com uma virgula(ou ponto)

tupla= (1, 2, 3, 4)
print (tupla)
# tupla.append(4) -> Dará um erro
# Operadores funcionais -> in, not in, +, *, len()

var = 123
 
t1 = (1, )
t2 = (2, )
t3 = (3, var)
 
t1, t2, t3 = t2, t3, t1
 
print(t1, t2, t3)
