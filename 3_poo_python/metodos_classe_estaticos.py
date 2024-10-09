from __future__ import annotations

# Métodos de classe estão ligados a classe e não ao objeto. Recebem um parâmetro que aponta para a classe e não para a instância do objeto, utiliza-se cls no lugar de self
# Métodos estáticos não recebem o primeiro argumento explícito. Ele também é um método vinculado a classe e não ao objeto. Este método não pode acessar ou modificar o estado da classe
# Geralmente usamos o método de classes em métodos de fabrica
# Geralmente usamos o método estaticos para criar funções utilitarias

from datetime import date



class Pessoa:
    def __init__(self, nome: str, idade: int) -> None:
        self.nome: str = nome
        self.idade: int = idade

    # Não está legal, "Método de fábrica", utilizar método de classe
    # def criar_de_data_nascimento(self, ano: int, mes: int, dia: int, nome: str) -> Pessoa:
    #     idade = date.today().year - ano
    #     return Pessoa(nome, idade)
        
    @classmethod
    def criar_de_data_nascimento(cls, ano: int, mes: int, dia:int, nome: str) -> Pessoa:
        idade = date.today().year - ano
        return cls(nome, idade)
    
    @classmethod
    def e_maior_idade(cls, idade: int) -> int:
        return idade >= 18

# p = Pessoa("Guilherme", 28)
# print(p.nome, p.idade)
    
# p2 = Pessoa().criar_de_data_nascimento(1993, 8, 9, "Test")
# print(p2.nome, p2.idade)

# Ao utilizar método de classe, pode se chamar o método sem criar multiplas instâncias
p = Pessoa.criar_de_data_nascimento(1993, 8, 9, "Test")
print(p.nome, p.idade)

print(Pessoa.e_maior_idade(18))
print(Pessoa.e_maior_idade(8))