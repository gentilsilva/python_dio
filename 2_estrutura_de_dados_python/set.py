# Sets (conjuntos) eliminam duplicidades
# Não garente a ordem
set([1, 2, 3, 1, 4]) # {1, 2, 3, 4}
set("abacaxi") # {"b", "a", "c", "x", "i"}
set(("palio", "gol", "celta", "palio")) # {"palio", "gol", "celta"}
linaguagens = {"python", "java", "python"}
print(linaguagens)

# Conjuntos (sets) em python não suportam indexação nem fatiamento
# Precisamos converter o set para uma lista
numeros = {1, 2, 3, 2}
numeros = list(numeros)
print(numeros[0])

# Só que é possível iterar com o for
carros = {"gol", "celta", "palio"}
for carro in carros:
    print(carro)

for indice, carro in enumerate(carros):
    print(f"{indice} - {carro}")

# Podemos fazer operações de matemática como set
conjunto_a = {1, 2, 3}
conjunto_b = {2, 3, 4}
conjunto_a.union(conjunto_b) # {1, 2, 3, 4}
conjunto_a.intersection(conjunto_b) # {2, 3}
conjunto_a.difference(conjunto_b) # {1}
conjunto_b.difference(conjunto_a) # {4}

conjunto_a = {1, 2, 3}
conjunto_b = {4, 1, 2, 5, 6, 3}
conjunto_a.issubset(conjunto_b) # True
conjunto_b.issubset(conjunto_a) # False
conjunto_a.issuperset(conjunto_b) # False
conjunto_b.issuperset(conjunto_a) # True

conjunto_a = {1, 2, 3, 4, 5}
conjunto_b = {6, 7, 8, 9}
conjunto_c = {1, 0}
conjunto_a.isdisjoint(conjunto_b) # True
conjunto_b.isdisjoint(conjunto_c) # False

# Outros métodos
sorteio = {1, 23}
sorteio.add(25) # {1, 23, 25}
sorteio.add(42) # {1, 23, 25, 42}
sorteio.add(25) # {1, 23, 25, 42} Ignora valores repetidos
sorteio.clear() # Limpa o set
sorteio.copy() # Cria uma cópia do set
numeros.discard(1) # discarta o valor correspondente do set - não da erro se o número não existir
numeros.pop() # Retira o valor do set pelo início
numeros.remove(1) # Retira o valor correspondente do set - da erro se o número naõ existir
len(numeros)

1 in numeros # True
10 in numeros # False
