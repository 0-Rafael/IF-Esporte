import sys
import tkinter as tk
from pathlib import Path
from tkinter import ttk

if __name__ == "__main__":
    sys.path.append(str(Path(__file__).resolve().parents[2]))

from exemplos.compartilhado.janela_base import criar_area_explicacao, criar_janela_exemplo, executar_exemplo_individual


class TelaRadioCheck:
    def __init__(self, janela_pai):
        self.janela = criar_janela_exemplo(janela_pai, "05 - Radio e check")
        self.turno = tk.StringVar(value="matutino")
        self.receber_email = tk.BooleanVar(value=True)
        self.participar_monitoria = tk.BooleanVar(value=False)
        self.resultado = tk.StringVar()
        self.criar_componentes()
        self.atualizar_resultado()

    def criar_componentes(self):
        criar_area_explicacao(
            self.janela,
            "Radiobutton e Checkbutton",
            "Radiobutton escolhe uma opção entre várias. Checkbutton permite marcar opções independentes.",
        )

        conteudo = ttk.Frame(self.janela, padding=16)
        conteudo.pack(fill="both", expand=True)

        grupo_turno = ttk.LabelFrame(conteudo, text="Turno preferido", padding=12)
        grupo_turno.pack(fill="x", pady=(0, 12))

        for texto, valor in [("Matutino", "matutino"), ("Vespertino", "vespertino"), ("Noturno", "noturno")]:
            ttk.Radiobutton(grupo_turno, text=texto, value=valor, variable=self.turno, command=self.atualizar_resultado).pack(anchor="w")

        grupo_opcoes = ttk.LabelFrame(conteudo, text="Opções adicionais", padding=12)
        grupo_opcoes.pack(fill="x")

        ttk.Checkbutton(grupo_opcoes, text="Receber avisos por e-mail", variable=self.receber_email, command=self.atualizar_resultado).pack(anchor="w")
        ttk.Checkbutton(grupo_opcoes, text="Tenho interesse em monitoria", variable=self.participar_monitoria, command=self.atualizar_resultado).pack(anchor="w")

        ttk.Label(conteudo, textvariable=self.resultado, wraplength=700).pack(anchor="w", pady=16)

    def atualizar_resultado(self):
        email = "sim" if self.receber_email.get() else "não"
        monitoria = "sim" if self.participar_monitoria.get() else "não"
        self.resultado.set(f"Turno: {self.turno.get()} | Receber e-mail: {email} | Monitoria: {monitoria}")


if __name__ == "__main__":
    executar_exemplo_individual(TelaRadioCheck, "05 - Radio e check")
