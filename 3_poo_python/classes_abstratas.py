from abc import ABC, abstractmethod
# Classes abstratas implementam o conceito de contrato (Semelhante a interfaces)

class ControleRemoto(ABC):
    @abstractmethod
    def ligar(self) -> None:
        pass

    @abstractmethod
    def desligar(self) -> None:
        pass

    @property
    @abstractmethod
    def marca(self) -> str:
        pass

class ControleTV(ControleRemoto):
    def ligar(self) -> None:
        print("Ligando a TV...")
        print("Ligado!")

    def desligar(self) -> None:
        print("Desligando a TV...")
        print("Desligado!")

    @property
    def marca(self) -> str:
        return "Philco"

class ControleArCondicionado(ControleRemoto):
    def ligar(self) -> None:
        print("Ligando o Ar condicionado...")
        print("Ligado!")
    
    def desligar(self) -> None:
        print("Desligando o Ar condicionado...")
        print("Desligado!")
    
    @property
    def marca(self) -> str:
        return "LG"


controleTv = ControleTV()
controleTv.ligar()
controleTv.desligar()
print(controleTv.marca)

controleArCond = ControleArCondicionado()
controleArCond.ligar()
controleArCond.desligar()
print(controleArCond.marca)