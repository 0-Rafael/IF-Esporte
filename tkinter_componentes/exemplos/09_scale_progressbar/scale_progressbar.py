import sys
import tkinter as tk
from pathlib import Path
from tkinter import ttk

if __name__ == "__main__":
    sys.path.append(str(Path(__file__).resolve().parents[2]))

from exemplos.compartilhado.janela_base import criar_area_explicacao, criar_janela_exemplo, executar_exemplo_individual


class TelaScaleProgressbar:
    def __init__(self, janela_pai):
        self.janela = criar_janela_exemplo(janela_pai, "09 - Scale e Progressbar")
        self.valor = tk.IntVar(value=40)
        self.texto_valor = tk.StringVar(value="Progresso: 40%")
        self.criar_componentes()

    def criar_componentes(self):
        criar_area_explicacao(
            self.janela,
            "Scale e Progressbar",
            "Scale permite escolher um valor em uma faixa. Progressbar representa visualmente esse valor.",
        )

        conteudo = ttk.Frame(self.janela, padding=16)
        conteudo.pack(fill="x")

        escala = ttk.Scale(conteudo, from_=0, to=100, variable=self.valor, command=self.atualizar_progresso)
        escala.pack(fill="x", pady=10)

        self.barra = ttk.Progressbar(conteudo, maximum=100, variable=self.valor)
        self.barra.pack(fill="x", pady=10)

        ttk.Label(conteudo, textvariable=self.texto_valor, style="Subtitulo.TLabel").pack(anchor="w")

    def atualizar_progresso(self, valor_recebido):
        valor = int(float(valor_recebido))
        self.valor.set(valor)
        self.texto_valor.set(f"Progresso: {valor}%")


if __name__ == "__main__":
    executar_exemplo_individual(TelaScaleProgressbar, "09 - Scale e Progressbar")
