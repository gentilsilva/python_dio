# Modificadores de acesso
# Em python não existe palavras reservadas para modificar acesso a variáveis
# Existe convenção entre os programadores e para isso utiliza-se um caracter específico.
# 
# Definição
# Público: Pode ser acessado fora da classe.
# Privado: Só pode ser acessado pela classe.

class Conta:
    def __init__(self, nro_agencia: int, saldo: float = 0):
        self.nro_agencia = nro_agencia
        self._saldo = saldo

    def depositar(self, saldo):
        # ...
        self._saldo += saldo

    def sacar(self, saldo):
        # ...
        self._saldo -= saldo

    def mostrar_saldo(self):
        # ...
        return self._saldo

conta = Conta("0001", 100)
conta.depositar(100)
print(conta.nro_agencia)
print(conta.mostrar_saldo())