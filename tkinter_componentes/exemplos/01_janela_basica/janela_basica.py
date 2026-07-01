import sys
import tkinter as tk
from pathlib import Path
from tkinter import ttk

if __name__ == "__main__":
    sys.path.append(str(Path(__file__).resolve().parents[2]))

from exemplos.compartilhado.janela_base import criar_area_explicacao, criar_janela_exemplo, executar_exemplo_individual


class TelaJanelaBasica:
    def __init__(self, janela_pai):
        self.janela = criar_janela_exemplo(janela_pai, "01 - Janela básica")
        self.criar_componentes()

    def criar_componentes(self):
        criar_area_explicacao(
            self.janela,
            "Janela básica",
            "A janela é o primeiro objeto visual de uma aplicação Tkinter. Ela possui título, tamanho e estado.",
        )

        conteudo = ttk.Frame(self.janela, padding=16)
        conteudo.pack(fill="both", expand=True)

        ttk.Label(conteudo, text="Experimente alterar o tamanho da janela pelos botões abaixo.").pack(anchor="w")

        botoes = ttk.Frame(conteudo)
        botoes.pack(anchor="w", pady=14)

        ttk.Button(botoes, text="Pequena", command=lambda: self.janela.geometry("520x360")).pack(side="left", padx=(0, 8))
        ttk.Button(botoes, text="Média", command=lambda: self.janela.geometry("760x520")).pack(side="left", padx=8)
        ttk.Button(botoes, text="Grande", command=lambda: self.janela.geometry("960x620")).pack(side="left", padx=8)

        self.variavel_redimensionavel = tk.BooleanVar(value=True)
        ttk.Checkbutton(
            conteudo,
            text="Permitir redimensionar a janela",
            variable=self.variavel_redimensionavel,
            command=self.alternar_redimensionamento,
        ).pack(anchor="w", pady=12)

    def alternar_redimensionamento(self):
        permitir = self.variavel_redimensionavel.get()
        self.janela.resizable(permitir, permitir)


if __name__ == "__main__":
    executar_exemplo_individual(TelaJanelaBasica, "01 - Janela básica")
