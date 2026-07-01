import sys
import tkinter as tk
from pathlib import Path
from tkinter import ttk

if __name__ == "__main__":
    sys.path.append(str(Path(__file__).resolve().parents[2]))

from exemplos.compartilhado.janela_base import criar_area_explicacao, criar_janela_exemplo, executar_exemplo_individual


class TelaComboboxSpinbox:
    def __init__(self, janela_pai):
        self.janela = criar_janela_exemplo(janela_pai, "06 - Combobox e Spinbox")
        self.disciplina = tk.StringVar(value="Programação Orientada a Objetos")
        self.quantidade = tk.IntVar(value=1)
        self.resultado = tk.StringVar(value="Escolha a disciplina e a quantidade de aulas.")
        self.criar_componentes()

    def criar_componentes(self):
        criar_area_explicacao(
            self.janela,
            "Combobox e Spinbox",
            "Combobox oferece uma lista de escolhas. Spinbox permite escolher números em uma faixa definida.",
        )

        conteudo = ttk.Frame(self.janela, padding=16)
        conteudo.pack(fill="x")

        ttk.Label(conteudo, text="Disciplina:").grid(row=0, column=0, sticky="w", pady=6)
        combo = ttk.Combobox(
            conteudo,
            textvariable=self.disciplina,
            values=["Programação Orientada a Objetos", "Banco de Dados", "Redes", "Web Design"],
            state="readonly",
            width=35,
        )
        combo.grid(row=0, column=1, sticky="ew", pady=6)

        ttk.Label(conteudo, text="Quantidade de aulas:").grid(row=1, column=0, sticky="w", pady=6)
        tk.Spinbox(conteudo, from_=1, to=6, textvariable=self.quantidade, width=8).grid(row=1, column=1, sticky="w", pady=6)

        ttk.Button(conteudo, text="Montar resumo", command=self.montar_resumo).grid(row=2, column=1, sticky="w", pady=10)
        ttk.Label(conteudo, textvariable=self.resultado, wraplength=650).grid(row=3, column=0, columnspan=2, sticky="w")
        conteudo.columnconfigure(1, weight=1)

    def montar_resumo(self):
        self.resultado.set(f"{self.disciplina.get()} terá {self.quantidade.get()} aula(s) nesta semana.")


if __name__ == "__main__":
    executar_exemplo_individual(TelaComboboxSpinbox, "06 - Combobox e Spinbox")
