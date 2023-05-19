# Basicamente um HashMap
dicionario = {"chave": "valor"}
telefones = {"Gabriel": 11995674832, "Debora": 11987654321}
vazio = {}

print(dicionario)
print(telefones["Gabriel"])
print(vazio)

# Evitar buscar pos chaves nao existentes

dictionary = {"gato": "chat", "cachorro": "chien", "cavalo": "cheval"}
words = ['gato', 'lion', 'cavalo']
 
for word in words:
    if word in dictionary:
        print(word, "->", dictionary.get(word))  # .get()
    else:
        print(word, "não está no dicionário")

# .keys() - Percorrer um dicionario usando FOR 

for key in telefones.keys():
    print(key, "->", telefones[key])

# .items() - Retorna tuplas onde cada uma é uma dupla key_value

dictionary2 = {"gato": "chat", "cachorro": "chien", "cavalo": "cheval"}
 
for english, french in dictionary2.items():
    print(english, "->", french)

# Trocar valor de uma chave

dictionary2['gato'] = 'minou'
print(dictionary2)

# sorted() - Ordenando um dicionario

dictionary = {"gato": "chat", "cachorro": "chien", "cavalo": "cheval"}
 
for key in sorted(dictionary.keys()):
    print(dictionary[key])
 
# Adicionar nova key_value

dictionary = {"gato": "chat", "cachorro": "chien", "cavalo": "cheval"}
 
dictionary['swan'] = 'cygne'
dictionary.update({"pato": "canard"})
print(dictionary)
 
# .copy() - copia um dicionario

dictionary3 = dictionary
print(dictionary3)
print()

# Deletando uma key_value

del dictionary['cachorro']
print(dictionary)
print()

# popitem() - Deleta o ultimo elemento do dicionario

dictionary.popitem()
print(dictionary)

# .clear() - Deleta todos os elementos

dictionary.clear()
print(dictionary)








