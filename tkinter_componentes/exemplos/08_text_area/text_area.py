import sys
import tkinter as tk
from pathlib import Path
from tkinter import ttk

if __name__ == "__main__":
    sys.path.append(str(Path(__file__).resolve().parents[2]))

from exemplos.compartilhado.janela_base import criar_area_explicacao, criar_janela_exemplo, executar_exemplo_individual


class TelaTextArea:
    def __init__(self, janela_pai):
        self.janela = criar_janela_exemplo(janela_pai, "08 - Área de texto")
        self.resultado = tk.StringVar(value="Digite uma observação e clique em Ler texto.")
        self.criar_componentes()

    def criar_componentes(self):
        criar_area_explicacao(
            self.janela,
            "Text",
            "O componente Text recebe textos longos, com várias linhas, como observações ou descrições.",
        )

        conteudo = ttk.Frame(self.janela, padding=16)
        conteudo.pack(fill="both", expand=True)

        self.texto = tk.Text(conteudo, height=10, wrap="word")
        self.texto.pack(fill="both", expand=True)
        self.texto.insert("1.0", "Escreva aqui uma observação sobre a aula de hoje.")

        botoes = ttk.Frame(conteudo)
        botoes.pack(anchor="w", pady=10)
        ttk.Button(botoes, text="Ler texto", command=self.ler_texto).pack(side="left", padx=(0, 8))
        ttk.Button(botoes, text="Limpar", command=self.limpar).pack(side="left")

        ttk.Label(conteudo, textvariable=self.resultado).pack(anchor="w")

    def ler_texto(self):
        conteudo = self.texto.get("1.0", tk.END).strip()
        quantidade = len(conteudo)
        self.resultado.set(f"O texto possui {quantidade} caractere(s).")

    def limpar(self):
        self.texto.delete("1.0", tk.END)
        self.resultado.set("Texto limpo.")


if __name__ == "__main__":
    executar_exemplo_individual(TelaTextArea, "08 - Área de texto")
