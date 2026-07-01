import sys
import tkinter as tk
from pathlib import Path
from tkinter import ttk

if __name__ == "__main__":
    sys.path.append(str(Path(__file__).resolve().parents[2]))

from exemplos.compartilhado.janela_base import criar_area_explicacao, criar_janela_exemplo, executar_exemplo_individual


class TelaTreeviewTabela:
    def __init__(self, janela_pai):
        self.janela = criar_janela_exemplo(janela_pai, "13 - Treeview")
        self.resultado = tk.StringVar(value="Selecione uma linha da tabela.")
        self.criar_componentes()

    def criar_componentes(self):
        criar_area_explicacao(
            self.janela,
            "Treeview",
            "Treeview pode representar tabelas com colunas, linhas e seleção de registros.",
        )

        conteudo = ttk.Frame(self.janela, padding=16)
        conteudo.pack(fill="both", expand=True)

        self.tabela = ttk.Treeview(conteudo, columns=("nome", "curso", "nota"), show="headings", height=8)
        self.tabela.heading("nome", text="Nome")
        self.tabela.heading("curso", text="Curso")
        self.tabela.heading("nota", text="Nota")

        self.tabela.column("nome", width=180)
        self.tabela.column("curso", width=220)
        self.tabela.column("nota", width=80, anchor="center")
        self.tabela.pack(fill="both", expand=True)
        self.tabela.bind("<<TreeviewSelect>>", self.mostrar_linha)

        for aluno in [
            ("Ana", "Informática", "9.0"),
            ("Bruno", "Informática", "7.5"),
            ("Carla", "Redes", "8.7"),
            ("Diego", "Web Design", "6.8"),
        ]:
            self.tabela.insert("", tk.END, values=aluno)

        ttk.Label(conteudo, textvariable=self.resultado).pack(anchor="w", pady=10)

    def mostrar_linha(self, evento):
        selecionado = self.tabela.selection()
        if selecionado:
            nome, curso, nota = self.tabela.item(selecionado[0], "values")
            self.resultado.set(f"{nome} faz {curso} e obteve nota {nota}.")


if __name__ == "__main__":
    executar_exemplo_individual(TelaTreeviewTabela, "13 - Treeview")
