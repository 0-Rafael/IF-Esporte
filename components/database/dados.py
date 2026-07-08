import json
class Modalidades:
    def __init__(self,caminho:str):
        self.caminho = caminho
    def ver_modalidades(self):
        try:
            with open(self.caminho, "r", encoding="utf-8") as arquivo:
                dados = json.load(arquivo)
            return dados
        except (json.JSONDecodeError, FileNotFoundError):
            return {}
    def adicionar_modalidades(self, modalidade: str, quantidade_vagas: int, professor: str):
        modalidade = modalidade.capitalize()
        professor = professor.capitalize()
        modalidades = self.ver_modalidades()
        if modalidade in modalidades:
            print("Modalidade já cadastrada")
            return
        
        modalidades[modalidade] = {
            "alunos": [],
            "QuantidadeVagas": quantidade_vagas,
            "ProfessorResponsavel": professor
        }
        with open(self.caminho, "w", encoding="utf-8") as arquivo:
            json.dump(modalidades, arquivo, indent=4)
    def adiionar_aluno(self, nome: str, matricula: str, esporte: str):
        try:
            esporte = esporte.capitalize()
            nome = nome.capitalize()
            dados = self.ver_modalidades()
            aluno = {"nome": nome, "matricula": matricula}
            dados[esporte]["alunos"].append(aluno)
            dados[esporte]["QuantidadeVagas"] = dados[esporte]["QuantidadeVagas"] - 1
            with open(self.caminho, "w", encoding="utf-8") as arquivo:
                json.dump(dados, arquivo, indent=4)
        except KeyError:
            print("Modalidade nao encontrada")
t1 = Modalidades("components/database/modalidades.json")
