import tkinter as tk
from tkinter import messagebox

class AplicativoCadastro:
    def __init__(self, root):
        self.root = root
        self.root.title("Sistema de Inscrição em Modalidades")
        self.root.geometry("400x450") 
        
        self.label_titulo = tk.Label(
            root, text="Modalidades Disponíveis", font=("Arial", 16, "bold"), pady=10
        )
        self.label_titulo.pack()

        self.label_instrucao = tk.Label(
            root, text="Clique em uma modalidade para se inscrever:", font=("Arial", 11)
        )
        self.label_instrucao.pack(pady=5)

        modalidades = ["Futebol", "Natação", "Vôlei", "Basquete", "", "Judô"]
        
        for mod in modalidades:
            btn_mod = tk.Button(
                root,
                text=mod,
                font=("Arial", 12),
                bg="#E0E0E0",      
                fg="black",         
                activebackground="#BDBDBD", 
                command=lambda m=mod: self.abrir_janela_confirmacao(m)
            )
            btn_mod.pack(pady=4, fill=tk.X, padx=40)

    def abrir_janela_confirmacao(self, modalidade_escolhida):
        self.janela_cadastro = tk.Toplevel(self.root)
        self.janela_cadastro.title("Confirmar Cadastro")
        self.janela_cadastro.geometry("350x280")
        
        self.janela_cadastro.grab_set()

        tk.Label(
            self.janela_cadastro, 
            text=f"Inscrição em: {modalidade_escolhida}", 
            font=("Arial", 12, "bold"), 
            fg="#0056b3"
        ).pack(pady=15)

        tk.Label(self.janela_cadastro, text="Nome do Aluno:", font=("Arial", 10)).pack(anchor="w", padx=30)
        self.entry_nome = tk.Entry(self.janela_cadastro, font=("Arial", 11))
        self.entry_nome.pack(fill=tk.X, padx=30, pady=5)

        tk.Label(self.janela_cadastro, text="Matrícula:", font=("Arial", 10)).pack(anchor="w", padx=30)
        self.entry_matricula = tk.Entry(self.janela_cadastro, font=("Arial", 11))
        self.entry_matricula.pack(fill=tk.X, padx=30, pady=5)

        self.btn_salvar = tk.Button(
            self.janela_cadastro, 
            text="Confirmar Matrícula", 
            font=("Arial", 11, "bold"), 
            bg="#007BFF", 
            fg="white",
            command=lambda: self.salvar_dados(modalidade_escolhida)
        )
        self.btn_salvar.pack(pady=20)

    def salvar_dados(self, modalidade):
        nome = self.entry_nome.get().strip()
        matricula = self.entry_matricula.get().strip()

        if not nome or not matricula:
            messagebox.showerror("Erro", "Todos os campos devem ser preenchidos!", parent=self.janela_cadastro)
            return

        mensagem_sucesso = f"Parabéns {nome}!\nSua inscrição em '{modalidade}' (Matrícula: {matricula}) foi confirmada."
        messagebox.showinfo("Sucesso!", mensagem_sucesso)

        self.janela_cadastro.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = AplicativoCadastro(root)
    root.mainloop()