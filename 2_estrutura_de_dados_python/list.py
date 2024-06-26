# Lista é um objeto, então pode receber outros objetos - Estrutura mutável

frutas = ["laranja", "maçã", "uva", "pera"]
frutas = []
letras = list("python") # => cria uma lista onde cada letra da palavra python é um índice
numeros = list(range(10)) # => cria uma lista de elementos de 0 a 9
carro = ["Ferrai", "F8", 4200000, 2020, 2900, "São Paulo", True] # => Listas em python pode receber mais de um tipo de dados

frutas[0] # laranja
frutas[2] # uva
frutas[-1] # pera
frutas[-3] # maçã

matriz = [
    [1, "a", 3],
    ["b", 3, 4],
    [6, 5, "c"]
]

matriz[0] # [1, "a", 2]
matriz[0][0] # 1
matriz[0][-1] # 2
matriz[-1][-1] # "c"

# Fatiamento
lista = ["p", "y", "t", "h", "o", "n"]
lista[2:] # "t", "h", "o", "n"
lista[:2] # "p", "y"
lista[1:3] # "y", "t"
lista[0:3:2] # "p", "t"
lista[::] # "p", "y", "t", "h", "o", "n"
lista[::-1] # "n", "o", "h", "t", "y", "p"

# Percorrendo lista
carros = ["gol", "celta", "palio"]
for indice, carro in enumerate(carros):
    print(f"{indice} - {carro}")


# Compreensão de listas (List Comprehension)
# Tentativa padrão
numeros_dois = [1, 30, 21, 2, 9, 65, 34]
pares_um = []
for numero in numeros_dois:
    if numero % 2 == 0:
        pares_um.append(numero)
# Tentativa com comprehension
pares_dois = [numero for numero in numeros_dois if numero % 2 == 0]

# Tentativa padrão
quadrado_um = []
for numero in numeros_dois:
    quadrado_um.append(numero ** 2)
# Tentativa com comprehension
quadrado_dois = [numero ** 2 for numero in numeros_dois]

# Métodos listas
lista_um = []
lista.append("Item") # => adiciona Item na lista
lista.clear() # => Limpa a lista
lista_dois = lista.copy() # => Cria uma cópia da lista em uma instância diferente.
lista.count("Item") # => Conta quantas vezes Item aparece dentro da lista
lista.extend(["Item_2", "Item_3"]) # => Adiciona uma coleção a lista já existente, para não ter que adicionar um a um.
lista.index("Item") # => Busca a primeira ocorrência de Item na lista e retorna seu indice
lista.pop() # => Retira a partir do ultimo indice (Comportamento de uma pilha padrão) LIFO se não passar parâmetros, se passar o indice como argumento ele remove o item que pertence aquele indice
lista.remove("Item") # => Remove o item da lista
lista.reverse() # => Inverte a ordem da lista
lista.sort() # => Ordena a lista, por padrão é alfabética. Pode-se passar argumentos para modificar a ordem de ordenação
len(lista) # => Retorna o tamanho da lista
sorted(lista) # => função build-in para ordernar listas. Pode-se passar argumentos para modificar a ordem de ordenação



