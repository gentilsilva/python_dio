from typing import Callable
# Em python é possível passar função como argumento para outra função
# E essas funções também podem ser retornadas
# Quando isso é feito chamamos as funções de função de primeira classe

# Inner functions: São as funções definidas dentro de outras funções

# Exemplo funções por parâmetro
def mensagem(nome: str) -> str:
    print("Executando função mensagem")
    return f"Oi {nome}"

def mensagem_longa(nome: str )-> str:
    print("Executando função mensagem longa")
    return f"Olá, tudo bem com você {nome}?"

def executar(funcao: Callable[[str], str], nome: str) -> str:
    print("Executando funcao executar")
    return funcao(nome)

print(executar(mensagem_longa, "João"))


# Exemplo Inner Functions
def printipal() -> None:
    print('Executando a função principal')

    def funcao_interna() -> None:
        print("Executando a função interna.")

    def funcao_interna_dois() -> None:
        print("Executando a função interna dois")

    funcao_interna()
    funcao_interna_dois()

printipal()


# Retorno de funções
def calculadora(operacao: str) -> Callable[[int, int], float]:
    def somar(a, b) -> float:
        return a + b
    
    def subtrair(a, b) -> float:
        return a - b
    
    def multiplicar(a, b) -> float:
        return a * b

    def dividir(a, b) -> float:
        return a / b
    
    match operacao:
        case "+":
            return somar
        case "-":
            return subtrair
        case "*":
            return multiplicar
        case "/":
            return dividir
        
print(calculadora("+")(2, 2))
print(calculadora("-")(2, 2))
print(calculadora("*")(2, 2))
print(calculadora("/")(2, 2))


# Decorador
def meu_decorador(funcao: Callable[[], None]) -> Callable[[], None]:
    def envelope():
        print("Faz algo antes de executar.")
        funcao()
        print("Faz algo depois de executar.")

    return envelope
    
def ola_mundo():
    print("Olá, Mundo!")

ola_mundo = meu_decorador(ola_mundo)
ola_mundo()


# Decorador com Açucar sintático
def meu_decorador_dois(funcao) -> Callable[[], None]:
    def envelope():
        print("Faz algo antes de executar.")
        funcao()
        print("Faz algo depois de executar.")
    return envelope

@meu_decorador_dois
def ola_mundo_dois():
    print("Olá, Mundo!")

ola_mundo_dois()
