import json
class Modalidades:
    def __init__(self,caminho:str):
        self.caminho = caminho
    def ver_modalidades(self):
        with open(self.caminho, "r", encoding="utf-8") as arquivo:
            dados = json.load(arquivo)
        return dados
    def adicionar_modalidades(self, modalidade: dict):
        pass
t1 = Modalidades("components/database/modalidades.json")
print(t1.ver_modalidades())
