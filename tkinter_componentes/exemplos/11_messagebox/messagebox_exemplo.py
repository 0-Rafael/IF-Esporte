import sys
import tkinter as tk
from pathlib import Path
from tkinter import messagebox, ttk

if __name__ == "__main__":
    sys.path.append(str(Path(__file__).resolve().parents[2]))

from exemplos.compartilhado.janela_base import criar_area_explicacao, criar_janela_exemplo, executar_exemplo_individual


class TelaMessagebox:
    def __init__(self, janela_pai):
        self.janela = criar_janela_exemplo(janela_pai, "11 - Messagebox")
        self.status = tk.StringVar(value="Clique em uma opção para abrir uma caixa de mensagem.")
        self.criar_componentes()

    def criar_componentes(self):
        criar_area_explicacao(
            self.janela,
            "Messagebox",
            "Messagebox mostra mensagens rápidas, erros e perguntas de confirmação.",
        )

        conteudo = ttk.Frame(self.janela, padding=16)
        conteudo.pack(fill="both", expand=True)

        ttk.Button(conteudo, text="Mostrar informação", command=self.mostrar_informacao).pack(anchor="w", pady=4)
        ttk.Button(conteudo, text="Mostrar erro", command=self.mostrar_erro).pack(anchor="w", pady=4)
        ttk.Button(conteudo, text="Confirmar ação", command=self.confirmar_acao).pack(anchor="w", pady=4)
        ttk.Label(conteudo, textvariable=self.status).pack(anchor="w", pady=16)

    def mostrar_informacao(self):
        messagebox.showinfo("Informação", "Cadastro realizado com sucesso.")
        self.status.set("Uma mensagem de informação foi exibida.")

    def mostrar_erro(self):
        messagebox.showerror("Erro", "Não foi possível concluir a operação.")
        self.status.set("Uma mensagem de erro foi exibida.")

    def confirmar_acao(self):
        confirmou = messagebox.askyesno("Confirmação", "Deseja continuar?")
        self.status.set("Usuário confirmou." if confirmou else "Usuário cancelou.")


if __name__ == "__main__":
    executar_exemplo_individual(TelaMessagebox, "11 - Messagebox")
