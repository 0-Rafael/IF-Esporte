import sys
import tkinter as tk
from pathlib import Path
from tkinter import colorchooser, filedialog, ttk

if __name__ == "__main__":
    sys.path.append(str(Path(__file__).resolve().parents[2]))

from exemplos.compartilhado.janela_base import criar_area_explicacao, criar_janela_exemplo, executar_exemplo_individual


class TelaDialogos:
    def __init__(self, janela_pai):
        self.janela = criar_janela_exemplo(janela_pai, "12 - Diálogos")
        self.resultado = tk.StringVar(value="Escolha uma ação.")
        self.criar_componentes()

    def criar_componentes(self):
        criar_area_explicacao(
            self.janela,
            "Filedialog e colorchooser",
            "Diálogos permitem usar janelas do sistema para escolher arquivos, pastas e cores.",
        )

        conteudo = ttk.Frame(self.janela, padding=16)
        conteudo.pack(fill="both", expand=True)

        ttk.Button(conteudo, text="Escolher arquivo", command=self.escolher_arquivo).pack(anchor="w", pady=4)
        ttk.Button(conteudo, text="Escolher pasta", command=self.escolher_pasta).pack(anchor="w", pady=4)
        ttk.Button(conteudo, text="Escolher cor", command=self.escolher_cor).pack(anchor="w", pady=4)
        ttk.Label(conteudo, textvariable=self.resultado, wraplength=680).pack(anchor="w", pady=16)

    def escolher_arquivo(self):
        caminho = filedialog.askopenfilename(title="Escolha um arquivo")
        self.resultado.set(caminho if caminho else "Nenhum arquivo escolhido.")

    def escolher_pasta(self):
        caminho = filedialog.askdirectory(title="Escolha uma pasta")
        self.resultado.set(caminho if caminho else "Nenhuma pasta escolhida.")

    def escolher_cor(self):
        cor_rgb, cor_hex = colorchooser.askcolor(title="Escolha uma cor")
        self.resultado.set(f"Cor escolhida: {cor_hex}" if cor_hex else "Nenhuma cor escolhida.")


if __name__ == "__main__":
    executar_exemplo_individual(TelaDialogos, "12 - Diálogos")
