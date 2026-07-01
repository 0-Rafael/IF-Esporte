import sys
import tkinter as tk
from pathlib import Path
from tkinter import ttk

if __name__ == "__main__":
    sys.path.append(str(Path(__file__).resolve().parents[2]))

from exemplos.compartilhado.janela_base import criar_area_explicacao, criar_janela_exemplo, executar_exemplo_individual


class TelaLayoutGerenciadores:
    def __init__(self, janela_pai):
        self.janela = criar_janela_exemplo(janela_pai, "16 - Gerenciadores de layout", largura=840, altura=560)
        self.criar_componentes()

    def criar_componentes(self):
        criar_area_explicacao(
            self.janela,
            "pack, grid e place",
            "Tkinter possui gerenciadores de layout. Use apenas um gerenciador por container para evitar confusão.",
        )

        conteudo = ttk.Frame(self.janela, padding=16)
        conteudo.pack(fill="both", expand=True)

        self.criar_exemplo_pack(conteudo)
        self.criar_exemplo_grid(conteudo)
        self.criar_exemplo_place(conteudo)

    def criar_exemplo_pack(self, container):
        grupo = ttk.LabelFrame(container, text="pack: empilha ou posiciona por lado", padding=10)
        grupo.pack(fill="x", pady=6)

        ttk.Button(grupo, text="Esquerda").pack(side="left", padx=4)
        ttk.Button(grupo, text="Também esquerda").pack(side="left", padx=4)
        ttk.Button(grupo, text="Direita").pack(side="right", padx=4)

    def criar_exemplo_grid(self, container):
        grupo = ttk.LabelFrame(container, text="grid: organiza em linhas e colunas", padding=10)
        grupo.pack(fill="x", pady=6)

        for linha in range(2):
            for coluna in range(3):
                ttk.Label(grupo, text=f"L{linha + 1}, C{coluna + 1}", relief="solid", padding=8).grid(
                    row=linha,
                    column=coluna,
                    padx=4,
                    pady=4,
                    sticky="ew",
                )

        for coluna in range(3):
            grupo.columnconfigure(coluna, weight=1)

    def criar_exemplo_place(self, container):
        grupo = ttk.LabelFrame(container, text="place: usa coordenadas", padding=10)
        grupo.pack(fill="both", expand=True, pady=6)

        area = tk.Frame(grupo, background="white", height=110)
        area.pack(fill="both", expand=True)

        tk.Label(area, text="x=20, y=20", background="#dbeafe").place(x=20, y=20)
        tk.Label(area, text="x=180, y=55", background="#dcfce7").place(x=180, y=55)


if __name__ == "__main__":
    executar_exemplo_individual(TelaLayoutGerenciadores, "16 - Gerenciadores de layout")
