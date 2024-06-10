# Estrutura imutável - Tuplas também é um objeto, então posso armazenar tupla dentro de tupals

frutas = ("laranja", "pera", "uva" "maçã",) # => Coloca-se "," no final para evitar erros de interpretação do python na hora de executar o programa, pois () pode estar presente em presedência de operadores
letras = tuple("python")
numeros = tuple([1, 2, 3, 4])
pais = ("Brasil",)

# Acessando tuplas
frutas[0] # => laranja
frutas[2] # => uva
frutas[-1] # => maçã
frutas[-3] # => pera

matriz = (
    (1, "a", 2),
    ("b", 3, 4),
    (6, 5, "c"),
)

matriz[0] # => (1, "a", 2)
matriz[0][0] # => 1
matriz[0][-1] # => 2
matriz[-1][-1] # =>"c"

# também pode se usar fatiamento
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


# Métodos da classe de tuplas
carros.count("gol") # => Conta quantas vezes gol aparece dentro da tupla
carros.index("gol") # => Busca a primeira ocorrência de gol na tupla e retorna seu indice
len(carros) # => Retorna o tamanho da tupla

print(isinstance(carros, tuple))