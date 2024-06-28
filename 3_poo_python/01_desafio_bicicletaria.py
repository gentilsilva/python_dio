# Classe
class Bicicleta:
    # Métodos __#__ são métodos especiais chamados de Dunder or magic methods
    # Construtor, self é uma referência explicita para atributos/metodos que pertencem a instância do objeto
    # Sempre executado ao instânciar a classe
    def __init__(self, cor: str, modelo: str, ano: int, valor: float):
        # self. -> atributos da classe
        self.cor = cor
        self.modelo = modelo
        self.ano = ano
        self.valor = valor

    # Comportamentos
    def buzinar(self) -> None:
        print("Plim plim...")

    def parar(self) -> None:
        print("Parando bicicleta...")
        print("Bicicleta parada!")

    def correr(self) -> None:
        print("Vrummmm...")

    # Semelhante ao toString() de classes Java
    # def __str__(self) -> str:
    #     return f"Bicicleta: {self.cor}, {self.modelo}, {self.ano}, {self.valor}"
    
    # Semelhante ao toString() de classes Java
    def __str__(self) -> str:
        return f"{self.__class__.__name__}: {', '.join([f'{chave} = {valor}' for chave, valor in self.__dict__.items()])}"

# Instância de bicicleta
b1 = Bicicleta("Vermelha", "Caloi", 2022, 600)
b1.buzinar()
b1.correr()
b1.parar()
print(b1.cor, b1.modelo, b1.ano, b1.valor)

b2 = Bicicleta("Verde", "Monark", 2000, 189)
b2.buzinar() # == Bicicleta.buzinar(b2)
print(b2)