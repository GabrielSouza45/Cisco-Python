# Funções em python devem ser declaradas antes de seu chamado no código
def somar(a, b):
    soma = a + b
    return soma

print(somar(5, 5))

# Passagem de parametro por palavra-chave

def dividir(dividendo, divisor):
    divisao = dividendo / divisor
    return divisao

print(dividir(dividendo = 5, divisor = 2))
print(dividir(divisor = 5, dividendo = 2))

# Pré Definição de valores nas funções

def nome(nome, sobrenome):
    print("Olá,", nome, sobrenome)
nome("Gabriel", "Souza")

def nomeDefinido(nome="Gabriel", sobrenome="Freitas"):
    print("Olá,", nome, sobrenome)
nomeDefinido()

def nomePreDefinido(nome="Gabriel", sobrenome="Freitas"):
    print("Olá,", nome, sobrenome)
nomePreDefinido(nome="Henrique")
nomePreDefinido(sobrenome="Souza")
nomePreDefinido(nome="Henrique", sobrenome="Joaquim")

# null == None

# Funções e escopos: a palavra-chave global
# Permite a modificação de variáveis dentro do escopo da função

def my_function():
    var = 2
    print("Eu conheço aquela variável?", var)
var = 1
my_function()
print(var)


def my_functionComGlobal():
    global var
    var = 2
    print("Eu conheço aquela variável?", var)
var = 1
my_functionComGlobal()
print(var)

##

def my_function(my_list_1):
    print("Print #1:", my_list_1)
    print("Print #2:", my_list_2)
    del my_list_1[0] # Pay attention to this line.
    print("Print #3:", my_list_1)
    print("Print #4:", my_list_2)
 
 
my_list_2 = [2, 3]
my_function(my_list_2)
print("Print #5:", my_list_2)

# Recursão uma função que chama ela mesmo

def fib(n):
    if n < 1:
        return None
    if n < 3:
        return 1
    return fib(n - 1) + fib(n - 2)
for n in range(1, 10):
 print(n, "->", fib(n))


























