# São blocos de código identificados por um nomee pode receber
# uma lista de parâmetros, que podem ou não ter valores padrões.
# Pode ou não ter retorno.
# Programar baseado em funções é o mesmo que programar de forma estruturada.

def exibir_mensagem():
    print("Olá mundo!")

def exibir_mensagem_2(nome):
    print(f"Seja bem vindo {nome}")

def exibir_mensagem_3(nome = "Anônimo"):
    print(f"Seja bem vindo {nome}")

exibir_mensagem()
exibir_mensagem_2(nome="Charlie")
exibir_mensagem_3()
exibir_mensagem_3(nome="Chappie")

def calcular_total(numeros):
    return sum(numeros)

def retorna_antecessor_e_sucessor(numero):
    antecessor = numero - 1
    sucessor = numero + 1
    return antecessor, sucessor

def func_3():
    print("Olá mundo!")

print(calcular_total([10, 20, 34]))
print(retorna_antecessor_e_sucessor(10))

def salvar_carro(marca, modelo, ano, placa):
    print(f"Carro inserido com suceso! {marca}/{modelo}/{ano}/{placa}")

salvar_carro("Palio", "Fiat", 1999, "ABC-1234") # Argumentos posicionados
salvar_carro(marca="Fiat", modelo="Palio", ano=1999, placa="ABC-1234") # Argumentos nomeados
salvar_carro(**{"marca": "Fiat", "modelo": "Palio", "ano": 1999, "placa": "ABC-1234"}) # Passando um dicionário que por baixo dos panos é convertido para argumento nomeado

# *args e **kwargs
# Estrutura do tipo *args -> Tupla
# Estrutura do tipo **kwargs -> Dicionário

def exibir_poema(data_extenso, *args, **kwargs): # Posso trocar para qualquer outro nome o args e o kwargs, o que importa é o * e **
    texto = "\n".join(args)
    metadados = "\n".join([f"{chave.title()}: {valor}" for chave, valor in kwargs.items()])
    mensagem = f"{data_extenso}\n\n{texto}\n\n{metadados}"
    print(mensagem)

exibir_poema("Zen of Python", "Beautiful is better tha ugly.", autor="Tim Peters", ano=1999)

# Parâmetros especiais
# / -> Indica que parâmetros antes dele só podem ser passados por posição
# * -> Indica que parâmetros após ele só podem ser passados por nome
def f(pos1, pos2, /, pos_or_key_word, *, key_word, key_word_2):
    pass

f("posicao_um", "posicao_2", pos_or_key_word="posicao_3", key_word="posicao_4", key_word_2="posicao_5") # Válido
f("posicao_um", "posicao_2", "posicao_3", key_word="posicao_4", key_word_2="posicao_5") # Válido
# f(pos1="posicao_um", pos2="posicao_2", pos_or_key_word="posicao_3", key_word="posicao_4", key_word_2="posicao_5") # Inválido
# f("posicao_um", "posicao_2", pos_or_key_word="posicao_3", "posicao_4", "posicao_5") # Inválido

def somar(a, b):
    return a + b

def subtrair(a, b):
    return a - b

def exibir_resultado(a, b, funcao):
    resultado = funcao(a, b)
    print(f"O resultado da opereração é {resultado}")

exibir_resultado(10, 10, somar)
exibir_resultado(10, 5, subtrair)

op = somar
print(op(1, 23))

# Escopos - local e global
# Variávels com a palavra reservada global, pertence ao escopo global

salario = 2000
def salario_bonus(bonus):
    global salario
    salario += bonus
    return salario

bonus = salario_bonus(100)
print(bonus)