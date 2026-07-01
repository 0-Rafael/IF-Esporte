import sys
import tkinter as tk
from pathlib import Path
from tkinter import ttk

if __name__ == "__main__":
    sys.path.append(str(Path(__file__).resolve().parents[2]))

from exemplos.compartilhado.janela_base import criar_area_explicacao, criar_janela_exemplo, executar_exemplo_individual


class TelaNotebookAbas:
    def __init__(self, janela_pai):
        self.janela = criar_janela_exemplo(janela_pai, "15 - Notebook")
        self.criar_componentes()

    def criar_componentes(self):
        criar_area_explicacao(
            self.janela,
            "Notebook",
            "Notebook organiza a interface em abas, separando conteúdos sem abrir várias janelas.",
        )

        conteudo = ttk.Frame(self.janela, padding=16)
        conteudo.pack(fill="both", expand=True)

        abas = ttk.Notebook(conteudo)
        abas.pack(fill="both", expand=True)

        aba_dados = ttk.Frame(abas, padding=14)
        aba_notas = ttk.Frame(abas, padding=14)
        aba_observacoes = ttk.Frame(abas, padding=14)

        abas.add(aba_dados, text="Dados")
        abas.add(aba_notas, text="Notas")
        abas.add(aba_observacoes, text="Observações")

        ttk.Label(aba_dados, text="Nome: Marina").pack(anchor="w", pady=4)
        ttk.Label(aba_dados, text="Matrícula: 2026001").pack(anchor="w", pady=4)

        ttk.Label(aba_notas, text="POO: 9.2").pack(anchor="w", pady=4)
        ttk.Label(aba_notas, text="Banco de Dados: 8.6").pack(anchor="w", pady=4)

        texto = tk.Text(aba_observacoes, height=8, wrap="word")
        texto.pack(fill="both", expand=True)
        texto.insert("1.0", "A aluna participa bem das atividades práticas.")


if __name__ == "__main__":
    executar_exemplo_individual(TelaNotebookAbas, "15 - Notebook")
