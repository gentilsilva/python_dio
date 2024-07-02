# Capacidade de uma classe filha derivar ou herdar as características e comportamentos da classe pai(base)
# Representa bem os relacionamentos do mundo real
# Fornece reutilização de código, não preciamos escrever o mesmo código repetidamente. Além disso, 
# permite adicionar mais recursos a uma classe sem modificá-la
# *É de natureza transitiva, que significa que, se a classe B herda da classe A, todas as subclasses de B herdarão
# automaticamente da classe A.

class A:
    pass

# Herança simples
class B(A):
    pass

# Herança simples -> Quando uma classe filha herda somente de uma classe pai
# Herança múltipla -> Quando uma classef ilha herda de várias classes pais. Isso não é comum
# na maioria das outras linguagens, só que feito em python.

class C:
    pass

class D:
    pass

# Herança múltipla
class E(C, D):
    pass


# Hands-on - Herança simplse
class Veiculo:
    def __init__(self, cor: str, placa: str, numero_rodas: int):
        self.cor = cor
        self.placa = placa
        self.numero_rodas = numero_rodas

    def ligar_motor(self) -> None:
        print("Ligando o motor")

    def __str__(self) -> str:
        return f"{self.__class__.__name__}: {", ".join([f'{chave} = {valor}' for chave, valor in self.__dict__.items()])}"

class Motocicleta(Veiculo):
    pass

class Carro(Veiculo):
    pass

class Caminhao(Veiculo):
    def __init__(self, cor: str, placa: str, numero_rodas: str, carregado: bool):
        # Chama o construtor da classe veiculo -- Se necessário implementar um construtor na classe filha.
        # Se não, não é necessário fazer esta implementação
        super().__init__(cor, placa, numero_rodas)
        self.carregado = carregado

    def esta_carregado(self) -> None:
        print(f"{'Sim' if self.carregado else 'Não'} estou carregado")

moto = Motocicleta("Preta", "ABC-1234", 2)
carro = Carro("Branco", "XDE-0098", 4)
caminhao = Caminhao("Roxo", "GFD-8712", 8, True)

# print(moto)
# print(carro)
# print(caminhao)


# Hands-on - Herança Múltipla
class Animal:
    def __init__(self, numero_patas: int):
        self.numero_patas = numero_patas

    def __str__(self) -> str:
        return f"{self.__class__.__name__}: {", ".join([f'{chave} = {valor}' for chave, valor in self.__dict__.items()])}"

class Mamifero(Animal):
    # Para classes que serão herdadas em herança multipla, é necessário passar kwargs no lugar do atributo da classe pai(se houver), pois assim o python consegue 
    # instânciar de forma correta e receber todos os parâmetros do construtor
    # Se não quiser usar **kwargs, posso passar os atributos explicitamente
    def __init__(self, cor_pelo: str, **kwargs):
        super().__init__(**kwargs)
        self.cor_pelo = cor_pelo


class Ave(Animal):
    # Para classes que serão herdadas em herança multipla, é necessário passar kwargs no lugar do atributo da classe pai(se houver), pois assim o python consegue 
    # instânciar de forma correta e receber todos os parâmetros do construtor
    # Se não quiser usar **kwargs, posso passar os atributos explicitamente
    def __init__(self, cor_bico: str, **kwargs):
        super().__init__(**kwargs)
        self.cor_bico = cor_bico

class Cachorro(Mamifero):
    pass

class Gato(Mamifero):
    pass

class Leao(Mamifero):
    pass

class Ornitorrinco(Mamifero, Ave):
    pass

gato = Gato(numero_patas=4, cor_pelo="Preto")
print(gato)

# Quando se usa **Kwargs, os parâmetros devem ser passados de forma nomeada
ornitorrinco = Ornitorrinco(numero_patas=2, cor_pelo="Vermelho", cor_bico="Laranja")
print(ornitorrinco)

# A forma como python busca o construtor é da seguinte forma Ornitorrinco -> Mamifero -> Ave -> Animal -> Object
# ornitorrinco.__mro__