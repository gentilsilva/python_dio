# Set ou Conjunto, coleção de objetos que tem elementos únicos (Não podem ser duplicados)
# Set não tem ordem fixa, pode ser diferente a cada execução
# Se não chamar set() para a criação, set é criado com {}

set([1, 2, 3, 1, 3, 4]) # {1, 2, 3, 4}
set("abacaxi") # {"b", "a", "c", "x", "i"}
set(("palio", "gol", "celta", "palio")) # => {"gol", "celta", "celta"} - ordem não garantida

# Sets em python não suportam indexação e fatiamento. Não posso acessar diretamente, transformar set em lista
numeros = {1, 2, 3, 4}
numeros = list(numeros)

numeros[0] # => 1

# É possível percorrer com laços de repetição
carros = {"gol", "palio", "celta"}
for carro in carros:
    print(f"{carro}")

for indice, carro in enumerate(carros):
    print(f"{indice} - {carro}")


# Operações matemáticas com Set
conjunto_a = {1, 2}
conjunto_b = {3, 4}

conjunto_c = {1, 2, 3}
conjunto_d = {2, 3, 4}

conjunto_a.union(conjunto_b) # => {1, 2, 3, 4}
conjunto_c.intersection(conjunto_d) # => {2, 3}

conjunto_a.