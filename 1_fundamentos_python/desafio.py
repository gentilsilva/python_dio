def depositar(valor: float, saldo: float, controle_transacao: list[float], tipo_transacao: list[int]):
    if valor < 0:
        print("Não é depositar valores negativos")
        return saldo
    saldo += valor
    controle_transacao.append(valor)
    tipo_transacao.append(1)
    return saldo

def sacar(valor: float, saldo: float, controle_transacao: list[float], tipo_transacao: list[int]):
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

def extrato(saldo: float, controle_transacao: list[float], tipo_transacao: list[int]):
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

def main():
    limite_saque: int = 0
    saldo: float = 0
    valor: float = 0
    controle_transacao: list[float] = []
    tipo_transacao: list[int] = []

    while(True):
        Menu = """
            [D] Depositar
            [S] Sacar
            [E] Extrato
            [Q] Sair
            =>
        """ 

        opcao = input(Menu)

        if limite_saque >= 3 and opcao.upper() == "S":
            print("Limite de saque diário estourado.")
            continue

        if opcao.upper() == "D":
            valor = float(input("Digite o valor a ser depositado: "))
            saldo = depositar(valor, saldo, controle_transacao, tipo_transacao)
        elif opcao.upper() == "S" and limite_saque < 3:
            valor = float(input("Digite o valor a ser sacado: "))
            if valor > 0 or valor > saldo:
                limite_saque += 1
            saldo = sacar(valor, saldo, controle_transacao, tipo_transacao)
        elif opcao.upper() == "E":
            extrato(saldo, controle_transacao, tipo_transacao)
        elif opcao.upper() == "Q":
            print("Obridado, volte sempre")
            break
        else:
            print("Opção invalida. Selecione novamente a opção desejada.")

if __name__ == "__main__":
    main()
