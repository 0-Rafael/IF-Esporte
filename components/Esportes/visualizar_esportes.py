import ttkbootstrap as tk
from tkinter import messagebox
from ttkbootstrap.constants import *

class AplicativoCadastro:
    def __init__(self, root):
        self.root = root
        self.root.title("Portal de Inscrições")
        self.root.geometry("420x500") 
        
        # Header
        self.banner = tk.Label(
            root, 
            text="PORTAL ESPORTIVO", 
            foreground="#aaaaaa",
            font=("Helvetica", 14, "bold"), 
            background="#539839",
            anchor="center"
        )
        self.banner.pack(fill=X, ipady=15, pady=(0, 15))

        self.label_instrucao = tk.Label(
            root, 
            text="Selecione a modalidade desejada:", 
            font=("Helvetica", 11, "bold"),
            bootstyle="secondary"
        )
        self.label_instrucao.pack(pady=10)

        modalidades = ["Futebol", "Natação", "Vôlei", "Basquete", "Handebol"]
        
        self.frame_botoes = tk.Frame(root)
        self.frame_botoes.pack(fill=BOTH, expand=True, padx=40)
        btn_t = tk.Button()
        btn_t.pack(pady=2, fill="y")

        # mapeando os botoes
        for mod in modalidades:
            btn_mod = tk.Button(
                self.frame_botoes,
                text=mod,
                bootstyle="info-outline",
                cursor="hand2",
                command=lambda m=mod: self.abrir_janela_confirmacao(m)
            )
            btn_mod.pack(pady=5, fill=X)

    def abrir_janela_confirmacao(self, modalidade_escolhida):
        self.janela_cadastro = tk.Toplevel(self.root)
        self.janela_cadastro.title("Confirmar Matrícula")
        self.janela_cadastro.geometry("360x320")
        self.janela_cadastro.resizable(False, False)
        self.janela_cadastro.grab_set()

        # Corfirm tabel
        tk.Label(
            self.janela_cadastro, 
            text=f"Inscrição: {modalidade_escolhida}", 
            font=("Helvetica", 12, "bold"), 
            bootstyle="info"
        ).pack(pady=20)

        # Nome
        tk.Label(self.janela_cadastro, text="Nome do Aluno", font=("Helvetica", 9, "bold")).pack(anchor="w", padx=35)
        self.entry_nome = tk.Entry(self.janela_cadastro, bootstyle="info")
        self.entry_nome.pack(fill=X, padx=35, pady=(2, 12))

        # Div matricula
        tk.Label(self.janela_cadastro, text="Número de Matrícula", font=("Helvetica", 9, "bold")).pack(anchor="w", padx=35)
        self.entry_matricula = tk.Entry(self.janela_cadastro, bootstyle="info")
        self.entry_matricula.pack(fill=X, padx=35, pady=(2, 20))

        # salvar button
        self.btn_salvar = tk.Button(
            self.janela_cadastro, 
            text="Finalizar Inscrição", 
            command=lambda: self.salvar_dados(modalidade_escolhida),
            bootstyle="success",
            cursor="hand2"
        )
        self.btn_salvar.pack(fill=X, padx=35)

    def salvar_dados(self, modalidade):
        nome = self.entry_nome.get().strip()
        matricula = self.entry_matricula.get().strip()

        if not nome or not matricula:
            messagebox.showerror("Atenção", "Por favor, preencha todos os campos.", parent=self.janela_cadastro)
            return

        mensagem = f"Inscrição realizada!\n\nAluno: {nome}\nModalidade: {modalidade}\nMatrícula: {matricula}"
        messagebox.showinfo("Sucesso!", mensagem)

        self.janela_cadastro.destroy()

if __name__ == "__main__":
    # "darkly", "cosmo", "superhero", "morph", "journal"
    root = tk.Window(themename="journal")
    app = AplicativoCadastro(root)
    root.mainloop()