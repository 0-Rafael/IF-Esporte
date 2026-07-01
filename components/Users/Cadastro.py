class Aluno:
    def __init__(self, nome, matricula):
        self.nome = nome
        self.matricula = matricula
        self.esportes = []
class Professor(Aluno):
    def __init__(self, nome, matricula):
        super().__init__(nome, matricula)