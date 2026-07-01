import sys
import tkinter as tk
from pathlib import Path
from tkinter import ttk

if __name__ == "__main__":
    sys.path.append(str(Path(__file__).resolve().parents[2]))

from exemplos.compartilhado.janela_base import criar_area_explicacao, criar_janela_exemplo, executar_exemplo_individual


class TelaListbox:
    def __init__(self, janela_pai):
        self.janela = criar_janela_exemplo(janela_pai, "07 - Listbox")
        self.nome_item = tk.StringVar()
        self.resultado = tk.StringVar(value="Selecione um item da lista.")
        self.criar_componentes()

    def criar_componentes(self):
        criar_area_explicacao(
            self.janela,
            "Listbox",
            "Listbox exibe uma lista simples de textos. O usuário pode selecionar um ou mais itens.",
        )

        conteudo = ttk.Frame(self.janela, padding=16)
        conteudo.pack(fill="both", expand=True)

        entrada = ttk.Frame(conteudo)
        entrada.pack(fill="x", pady=(0, 10))
        ttk.Entry(entrada, textvariable=self.nome_item, width=35).pack(side="left", fill="x", expand=True)
        ttk.Button(entrada, text="Adicionar", command=self.adicionar_item).pack(side="left", padx=8)
        ttk.Button(entrada, text="Remover selecionado", command=self.remover_item).pack(side="left")

        self.lista = tk.Listbox(conteudo, height=10)
        self.lista.pack(fill="both", expand=True)
        self.lista.bind("<<ListboxSelect>>", self.mostrar_item_selecionado)

        for item in ["Python", "Tkinter", "Classe", "Objeto"]:
            self.lista.insert(tk.END, item)

        ttk.Label(conteudo, textvariable=self.resultado).pack(anchor="w", pady=10)

    def adicionar_item(self):
        item = self.nome_item.get().strip()
        if item:
            self.lista.insert(tk.END, item)
            self.nome_item.set("")

    def remover_item(self):
        selecao = self.lista.curselection()
        if selecao:
            self.lista.delete(selecao[0])
            self.resultado.set("Item removido.")

    def mostrar_item_selecionado(self, evento):
        selecao = self.lista.curselection()
        if selecao:
            item = self.lista.get(selecao[0])
            self.resultado.set(f"Item selecionado: {item}")


if __name__ == "__main__":
    executar_exemplo_individual(TelaListbox, "07 - Listbox")
