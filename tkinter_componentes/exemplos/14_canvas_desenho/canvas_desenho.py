import sys
import tkinter as tk
from pathlib import Path
from tkinter import ttk

if __name__ == "__main__":
    sys.path.append(str(Path(__file__).resolve().parents[2]))

from exemplos.compartilhado.janela_base import criar_area_explicacao, criar_janela_exemplo, executar_exemplo_individual


class TelaCanvasDesenho:
    def __init__(self, janela_pai):
        self.janela = criar_janela_exemplo(janela_pai, "14 - Canvas")
        self.cor_atual = tk.StringVar(value="#2563eb")
        self.criar_componentes()

    def criar_componentes(self):
        criar_area_explicacao(
            self.janela,
            "Canvas",
            "Canvas permite desenhar formas, linhas e responder a cliques do usuário.",
        )

        conteudo = ttk.Frame(self.janela, padding=16)
        conteudo.pack(fill="both", expand=True)

        barra = ttk.Frame(conteudo)
        barra.pack(fill="x", pady=(0, 8))
        ttk.Button(barra, text="Azul", command=lambda: self.cor_atual.set("#2563eb")).pack(side="left", padx=(0, 8))
        ttk.Button(barra, text="Verde", command=lambda: self.cor_atual.set("#16a34a")).pack(side="left", padx=8)
        ttk.Button(barra, text="Limpar", command=self.limpar_canvas).pack(side="left", padx=8)

        self.canvas = tk.Canvas(conteudo, background="white", height=300)
        self.canvas.pack(fill="both", expand=True)
        self.canvas.bind("<Button-1>", self.desenhar_circulo)

        self.canvas.create_rectangle(30, 30, 180, 110, fill="#dbeafe", outline="#2563eb")
        self.canvas.create_text(105, 70, text="Clique para desenhar", fill="#1f2937")

    def desenhar_circulo(self, evento):
        raio = 12
        self.canvas.create_oval(
            evento.x - raio,
            evento.y - raio,
            evento.x + raio,
            evento.y + raio,
            fill=self.cor_atual.get(),
            outline="",
        )

    def limpar_canvas(self):
        self.canvas.delete("all")


if __name__ == "__main__":
    executar_exemplo_individual(TelaCanvasDesenho, "14 - Canvas")
