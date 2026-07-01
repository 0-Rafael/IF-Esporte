import sys
import tkinter as tk
from pathlib import Path
from tkinter import ttk

if __name__ == "__main__":
    sys.path.append(str(Path(__file__).resolve().parents[2]))

from exemplos.compartilhado.janela_base import criar_area_explicacao, criar_janela_exemplo, executar_exemplo_individual


class TelaEntryTexto:
    def __init__(self, janela_pai):
        self.janela = criar_janela_exemplo(janela_pai, "03 - Entrada de texto")
        self.nome = tk.StringVar()
        self.idade = tk.StringVar()
        self.resultado = tk.StringVar(value="Preencha os campos e clique em Cadastrar.")
        self.criar_componentes()

    def criar_componentes(self):
        criar_area_explicacao(
            self.janela,
            "Entry",
            "O componente Entry recebe textos curtos, como nome, e-mail, senha ou idade.",
        )

        formulario = ttk.Frame(self.janela, padding=16)
        formulario.pack(fill="x")

        ttk.Label(formulario, text="Nome:").grid(row=0, column=0, sticky="w", pady=6)
        ttk.Entry(formulario, textvariable=self.nome, width=35).grid(row=0, column=1, sticky="ew", pady=6)

        ttk.Label(formulario, text="Idade:").grid(row=1, column=0, sticky="w", pady=6)
        ttk.Entry(formulario, textvariable=self.idade, width=10).grid(row=1, column=1, sticky="w", pady=6)

        botoes = ttk.Frame(formulario)
        botoes.grid(row=2, column=1, sticky="w", pady=10)
        ttk.Button(botoes, text="Cadastrar", command=self.cadastrar).pack(side="left", padx=(0, 8))
        ttk.Button(botoes, text="Limpar", command=self.limpar).pack(side="left")

        ttk.Label(formulario, textvariable=self.resultado).grid(row=3, column=0, columnspan=2, sticky="w", pady=8)
        formulario.columnconfigure(1, weight=1)

    def cadastrar(self):
        nome = self.nome.get().strip()
        idade = self.idade.get().strip()

        if not nome:
            self.resultado.set("Informe o nome.")
            return

        if not idade.isdigit():
            self.resultado.set("A idade deve conter apenas números.")
            return

        self.resultado.set(f"{nome} foi cadastrado(a) com {idade} ano(s).")

    def limpar(self):
        self.nome.set("")
        self.idade.set("")
        self.resultado.set("Campos limpos.")


if __name__ == "__main__":
    executar_exemplo_individual(TelaEntryTexto, "03 - Entrada de texto")
