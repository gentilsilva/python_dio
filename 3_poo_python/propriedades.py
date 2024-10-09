# Com property() do python é utilizado para criar atributos gerenciados em uma classe.
# Esses atributos gerenciados são conhecidos como propriedades.

from datetime import date


class Foo:
    def __init__(self, x: int = None) -> None:
        self._x = x

    @property
    def x(self):
        return self._x or 0
    
    @x.setter
    def x(self, value: int) -> int:
        self._x += value

    @x.deleter
    def x(self):
        self._x = -1
    
# foo = Foo(10)
# print(foo.x)
# foo.x = 10
# print(foo.x)

# del foo.x
# print(foo.x)

class Pessoa:
    def __init__(self, nome: str, ano_nascimento: int) -> None:
        self._nome = nome
        self._ano_nascimento = ano_nascimento

    @property
    def nome(self):
        return self._nome
    
    @property
    def idade(self):
        _ano_atual = date.today().year
        return _ano_atual - self._ano_nascimento
    
pessoa = Pessoa("Teste", 1993)
print(f"Nome: {pessoa.nome} \tIdade: {pessoa.idade}")