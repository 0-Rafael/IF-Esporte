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
    def adicionar_modalidades(self, modalidade: str, quantidade_vagas: int, professor: str, datas: list):
        modalidade = modalidade.capitalize()
        professor = professor.capitalize()
        modalidades = self.ver_modalidades()
        if modalidade in modalidades:
            print("Modalidade já cadastrada")
            return
        
        modalidades[modalidade] = {
            "alunos": [],
            "QuantidadeVagas": quantidade_vagas,
            "ProfessorResponsavel": professor,
            "Datas": datas
        }
        with open(self.caminho, "w", encoding="utf-8") as arquivo:
            json.dump(modalidades, arquivo, indent=4)
    def remover_modalidade(self, esporte):
        dados = self.ver_modalidades()

        esporte = esporte.capitalize()
        
        if esporte in dados:
            del dados[esporte]

            with open(self.caminho, "w", encoding="utf-8") as arquivo:
                json.dump(dados, arquivo, indent=4)

            return True

        return False
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
    def remover_aluno(self, nome, matricula, esporte):
        dados = self.ver_modalidades()
        esporte = esporte.capitalize()
        nome = nome.capitalize()
        
        if esporte in dados:
            for indice, aluno in enumerate(dados[esporte]["alunos"]):
                if aluno["matricula"] == matricula and aluno["nome"] == nome:
                    dados[esporte]["alunos"].pop(indice)
                    dados[esporte]["QuantidadeVagas"] += 1
                    with open(self.caminho, "w", encoding="utf-8") as arquivo:
                        json.dump(dados, arquivo, indent=4)
                    return True
        return False



    def verificar_quantidade_matricula(self, matricula: str):
        modalidades = self.ver_modalidades()
        quantidade = 0
        for key,value in modalidades.items():
            for alunos in value["alunos"]:
                if alunos["matricula"]==matricula:
                    quantidade+=1
        if quantidade>=2:
            return True
        return False
    def cadastro_mesma_modalidade(self, matricula: str, esporte: str):
        modalidades = self.ver_modalidades()
        for key,value in modalidades.items():
            if key==esporte:
                for alunos in value["alunos"]:
                    if alunos["matricula"]==matricula:
                        return True
        return False

