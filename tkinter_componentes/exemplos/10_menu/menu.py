import sys
import tkinter as tk
from pathlib import Path
from tkinter import ttk

if __name__ == "__main__":
    sys.path.append(str(Path(__file__).resolve().parents[2]))

from exemplos.compartilhado.janela_base import criar_area_explicacao, criar_janela_exemplo, executar_exemplo_individual


class TelaMenu:
    def __init__(self, janela_pai):
        self.janela = criar_janela_exemplo(janela_pai, "10 - Menu")
        self.status = tk.StringVar(value="Use o menu superior para executar ações.")
        self.criar_menu()
        self.criar_componentes()

    def criar_menu(self):
        barra_menu = tk.Menu(self.janela)

        menu_arquivo = tk.Menu(barra_menu, tearoff=False)
        menu_arquivo.add_command(label="Novo", command=lambda: self.status.set("Novo arquivo criado."))
        menu_arquivo.add_command(label="Salvar", command=lambda: self.status.set("Arquivo salvo."))
        menu_arquivo.add_separator()
        menu_arquivo.add_command(label="Fechar exemplo", command=self.janela.destroy)

        menu_ajuda = tk.Menu(barra_menu, tearoff=False)
        menu_ajuda.add_command(label="Sobre", command=lambda: self.status.set("Exemplo de menus no Tkinter."))

        barra_menu.add_cascade(label="Arquivo", menu=menu_arquivo)
        barra_menu.add_cascade(label="Ajuda", menu=menu_ajuda)
        self.janela.config(menu=barra_menu)

    def criar_componentes(self):
        criar_area_explicacao(
            self.janela,
            "Menu",
            "Menus organizam comandos em uma barra superior, como em aplicativos de desktop tradicionais.",
        )

        conteudo = ttk.Frame(self.janela, padding=16)
        conteudo.pack(fill="both", expand=True)
        ttk.Label(conteudo, textvariable=self.status, style="Subtitulo.TLabel").pack(anchor="w")


if __name__ == "__main__":
    executar_exemplo_individual(TelaMenu, "10 - Menu")
