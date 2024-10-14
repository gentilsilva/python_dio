import functools
from typing import Callable

def meu_decorador(funcao: Callable[[], None]) -> Callable[[], None]:
    @functools.wraps(funcao)
    def envelope(*args, **kwargs):
        print("Faz algo antes de executar")
        resultado: str = funcao(*args, **kwargs)
        print("Faz algo depois de executar")
        return resultado

    return envelope

@meu_decorador
def ola_mundo(nome: str, valor: int) -> None:
    print(f"Olá, mundo - {nome}")
    return nome.upper()

resultado: str = ola_mundo("João", 1000)
print(resultado)

# Introspecção
# Capacidade de um objeto saber sobre seus próprios atributos em tempo de execução
print(ola_mundo.__name__)