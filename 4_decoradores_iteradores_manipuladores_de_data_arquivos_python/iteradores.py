# Iteradores em python são objetos que contém um número contável de valores
# que podem ser iterados, o que significa que você pode percorrer todos os valores.
# Existem dois métodos especiais "__iter__()" e "__next()"

# É útil para economizar memória evitando carregar todas as linha do arquivo
# Iterar linha a linha do arquivo.

class FileIterator:
    def __init__(self, filename):
        self.file = open(filename)

    def __iter__(self):
        return self

    def __next__(self):
        line = self.file.readline()
        if line == "":
            return line
        else:
            self.file.close()
            raise StopIteration

# Uso do FileIterator
# for line in FileIterator('large_file.txt'):
#     print(line)

class MeuIterador:
    def __init__(self, numeros: list[int]):
        self.numeros = numeros
        self.contador = 0

    def __iter__(self):
        return self

    def __next__(self):
        try:
            numero = self.numeros[self.contador]
            self.contador += 1
            return numero * 2
        except IndexError:
            raise StopIteration

for i in MeuIterador([38, 13, 11]):
    print(i)
