import sys
import tkinter as tk
from pathlib import Path
from tkinter import ttk

if __name__ == "__main__":
    sys.path.append(str(Path(__file__).resolve().parents[2]))

from exemplos.compartilhado.janela_base import criar_area_explicacao, criar_janela_exemplo, executar_exemplo_individual


class TelaLabelsBotoes:
    def __init__(self, janela_pai):
        self.janela = criar_janela_exemplo(janela_pai, "02 - Labels e botões")
        self.quantidade_cliques = 0
        self.mensagem = tk.StringVar(value="Clique no botão para alterar esta mensagem.")
        self.criar_componentes()

    def criar_componentes(self):
        criar_area_explicacao(
            self.janela,
            "Labels e botões",
            "Labels exibem texto. Botões executam funções quando o usuário clica neles.",
        )

        conteudo = ttk.Frame(self.janela, padding=16)
        conteudo.pack(fill="both", expand=True)

        ttk.Label(conteudo, textvariable=self.mensagem, style="Subtitulo.TLabel").pack(anchor="w", pady=(0, 12))

        ttk.Button(conteudo, text="Contar clique", command=self.contar_clique).pack(anchor="w")
        ttk.Button(conteudo, text="Reiniciar", command=self.reiniciar).pack(anchor="w", pady=8)

    def contar_clique(self):
        self.quantidade_cliques += 1
        self.mensagem.set(f"O botão foi clicado {self.quantidade_cliques} vez(es).")

    def reiniciar(self):
        self.quantidade_cliques = 0
        self.mensagem.set("Contador reiniciado.")


if __name__ == "__main__":
    executar_exemplo_individual(TelaLabelsBotoes, "02 - Labels e botões")
