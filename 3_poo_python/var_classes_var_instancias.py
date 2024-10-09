class Estudante:
    # Atributo de classe
    escola: str = "DIO"

    def __init__(self, nome, matricula) -> None:
        self.nome = nome
        self.matricula = matricula

    def __str__(self) -> None:
        return f"{self.nome} - {self.matricula} - {self.escola}"
    
def mostrar_valores(*objetos) -> None:
    for objeto in objetos:
        print(objeto)

aluno_1 = Estudante("Guilherme", 1)
aluno_2 = Estudante("Giovanna", 2)
mostrar_valores(aluno_1, aluno_2)

Estudante.escola = "Python"

aluno_3 = Estudante("Chappie", 3)
mostrar_valores(aluno_1, aluno_2, aluno_3)