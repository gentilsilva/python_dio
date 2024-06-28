def depositar(valor: float, saldo: float, controle_transacao: list[float], tipo_transacao: list[int], /):
    if valor < 0:
        print("Não é depositar valores negativos")
        return saldo
    saldo += valor
    controle_transacao.append(valor)
    tipo_transacao.append(1)
    return saldo

def sacar(*, valor: float, saldo: float, controle_transacao: list[float], tipo_transacao: list[int]):
    if valor <= 0:
        print("Não é possível relizar saques de R$ 0 ou valores negativos.")
        return saldo
    elif saldo < valor:
        print("Saldo insuficiente.")
        return saldo
    saldo -= valor
    controle_transacao.append(valor)
    tipo_transacao.append(-1)
    return saldo

def extrato(saldo: float, /, tipo_transacao: list[int], *, controle_transacao: list[float]):
    print("=============== Extrato ===============")
    if len(controle_transacao) != 0:
        for i in range(len(controle_transacao)):
            if tipo_transacao[i] == 1:
                print(f"Deposito: R${controle_transacao[i]:.2f}")
            elif tipo_transacao[i] == -1:
                print(f"Saque: R${controle_transacao[i]:.2f}")
    else:
        print("Não foi realizadas movimentações")
    print("\n")
    print(f"O saldo atual é: R${saldo:.2f}")
    print("=======================================")

def criar_usuario(usuarios: list[dict]):
    controlador: bool = True
    while controlador is True:
        nome: str = input("Digite o nome: ")
        data_nascimento: str = (input("Digite a data de nascimento (dd/mm/YYYY): "))
        cpf: str = input("Digite o CPF (SOMENTE NÚMEROS): ")
        endereco: str = input("Digite o endereço (logradouro, nro - bairro - cidade/sigla estado): ")

        if len(usuarios) != 0:
            for item in usuarios:
                if item["cpf"] == cpf:
                    print("CPF Já cadastrado. Duplicidade de usuários é proibido.")
                    controlador = True
                    break
                else:
                    controlador = False
        else:
            controlador = False
    
    usuario = {"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco}
    usuarios.append(usuario)
    print(f"Usuário criado com sucesso\n {usuario}")

def criar_conta_corrente(contas_corrente: list[dict], conta: int, usuarios: list[dict]):
    conta_corrente = {}
    usuario_existe: bool = False
    agencia: str = "0001"
    cpf: str = input("Digite o cpf do usuário: ")

    for item in usuarios:
        if item["cpf"] == cpf:
            conta_corrente = {"agencia": agencia, "conta": conta, "usuario": item}
            contas_corrente.append(conta_corrente)
            conta += 1
            usuario_existe = True
            break

    if usuario_existe:
        print(f"Conta criada com sucesso.\n {conta_corrente}")
        return conta
    else:
        print("Usuário não existe")

def main():
    numero_conta: int = 1
    limite_saque: int = 0
    saldo: float = 0
    valor: float = 0
    controle_transacao: list[float] = []
    tipo_transacao: list[int] = []
    usuarios: list[dict] = []
    contas_correntes: list[dict] = []

    while(True):
        Menu = """
            [U] Criar usuário
            [C] Criar conta
            [D] Depositar
            [S] Sacar
            [E] Extrato
            [Q] Sair
            Escolha =>
        """ 

        opcao = input(Menu)

        if opcao.upper() == "U":
            criar_usuario(usuarios)
        elif opcao.upper() == "C":
            numero_conta = criar_conta_corrente(contas_correntes, numero_conta, usuarios)
        elif limite_saque >= 3 and opcao.upper() == "S":
            print("Limite de saque diário estourado.")
            continue
        elif opcao.upper() == "D":
            valor = float(input("Digite o valor a ser depositado: "))
            saldo = depositar(valor, saldo, controle_transacao, tipo_transacao)
        elif opcao.upper() == "S" and limite_saque < 3:
            valor = float(input("Digite o valor a ser sacado: "))
            if valor > 0 or valor > saldo:
                limite_saque += 1
            saldo = sacar(valor=valor, saldo=saldo, controle_transacao=controle_transacao, tipo_transacao=tipo_transacao)
        elif opcao.upper() == "E":
            extrato(saldo, tipo_transacao, controle_transacao=controle_transacao)
        elif opcao.upper() == "Q":
            print("Obridado, volte sempre")
            break
        else:
            print("Opção invalida. Selecione novamente a opção desejada.")

if __name__ == "__main__":
    main()
