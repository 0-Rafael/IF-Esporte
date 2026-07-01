import sys
import tkinter as tk
from pathlib import Path
from tkinter import ttk

if __name__ == "__main__":
    sys.path.append(str(Path(__file__).resolve().parents[2]))

from exemplos.compartilhado.janela_base import criar_area_explicacao, criar_janela_exemplo, executar_exemplo_individual


class TelaFrameOrganizacao:
    def __init__(self, janela_pai):
        self.janela = criar_janela_exemplo(janela_pai, "04 - Organização com frames")
        self.resumo = tk.StringVar(value="Use frames para separar responsabilidades visuais.")
        self.criar_componentes()

    def criar_componentes(self):
        criar_area_explicacao(
            self.janela,
            "Frame e LabelFrame",
            "Frames agrupam widgets relacionados. Isso deixa a interface mais organizada e fácil de manter.",
        )

        conteudo = ttk.Frame(self.janela, padding=16)
        conteudo.pack(fill="both", expand=True)

        dados = ttk.LabelFrame(conteudo, text="Dados do aluno", padding=12)
        dados.pack(fill="x", pady=(0, 12))

        ttk.Label(dados, text="Nome: Ana").grid(row=0, column=0, sticky="w", padx=8, pady=4)
        ttk.Label(dados, text="Curso: Informática").grid(row=0, column=1, sticky="w", padx=8, pady=4)
        ttk.Label(dados, text="Turma: 2º ano").grid(row=1, column=0, sticky="w", padx=8, pady=4)

        acoes = ttk.LabelFrame(conteudo, text="Ações", padding=12)
        acoes.pack(fill="x")

        ttk.Button(acoes, text="Matricular", command=lambda: self.resumo.set("Aluno matriculado.")).pack(side="left", padx=(0, 8))
        ttk.Button(acoes, text="Cancelar matrícula", command=lambda: self.resumo.set("Matrícula cancelada.")).pack(side="left")

        ttk.Label(conteudo, textvariable=self.resumo, style="Subtitulo.TLabel").pack(anchor="w", pady=16)


if __name__ == "__main__":
    executar_exemplo_individual(TelaFrameOrganizacao, "04 - Organização com frames")
