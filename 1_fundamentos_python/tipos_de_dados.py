texto: str
numerico_inteiro: int
numerico_flutuante: float
numerico_flutuante_dois: complex
sequencia: list
sequencia_dois: tuple
sequencia_tres: range
mapa: dict
colecao: set
colecao_dois: frozenset
booleano: bool
binario: bytes
binario_dois: bytearray
binario_tres: memoryview

# print(5 // 2)

# Operadores de identidade
# is - is not --- compara se ocupam a mesma região de memória

# Operadores lógicos
# and - or

# Operadores de associação
# in - not in --- verifica se uma coisa pertence ou está contida em outra

# Estrutura de repetição for in range()
# range() recebe argumentos (inicio, final, step) (final obrigatório)


# Métodos de manipulação de String
curso = "pYhHon"
curso.upper() # -> "PYTHON"
curso.lower() # -> "python"
curso.title() # -> "Python"

curso = "   Python "
curso.strip() # -> "Python"
curso.lstrip() # -> "Python "
curso.rstrip() # -> "   Python"

curso = "Python"
curso.center(10, "#") # -> "##Python##"
".".join(curso) # -> "P.y.t.h.o.n"

nome = "Aloha autumn summer hi"
nome_2 = "Gentil Souza Reis Neto e Silva"
nome[0] # -> "A"
nome[:6] # -> "Aloha "
nome[13:] # "summer hi"
nome[7:12] # -> "utumn"
nome[7:12:2] # -> "uun"
nome[:] # -> "Aloha autumn summer hi"
nome[::-1] # -> "ih remmus nmutua aholA"

month = input()
A = "A"

months_dict = {
    "1": "January",
    "2": "February",
    "3": "March",
    "4": "April",
    "5": "May",
    "6": "June",
    "7": "July",
    "8": "August",
    "9": "September",
    "10": "October",
    "11": "November",
    "12": "December",
}

for mes in months_dict:
  if mes == str(month):
    print(months_dict[mes])

# A.endswith()