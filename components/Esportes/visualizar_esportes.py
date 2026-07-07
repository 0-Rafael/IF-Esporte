import ttkbootstrap as tk
from tkinter import messagebox
from ttkbootstrap.constants import *
from components.database.dados import Modalidades
class JanelaCadastro:
    def __init__(self, janela):
        self.janela = janela
        self.janela.title("Portal de Inscrições")
        self.janela.geometry("420x500")
        self.modalidades = Modalidades("components/database/modalidades.json") 
        
        self.banner = tk.Label(
            janela, 
            text="PORTAL ESPORTIVO", 
            foreground="#aaaaaa",
            font=("Helvetica", 14, "bold"), 
            background="#539839",
            anchor="center"
        )
        self.banner.pack(fill=X, ipady=15, pady=(0, 15))

        self.label_instrucao = tk.Label(
            janela, 
            text="Selecione a modalidade desejada:", 
            font=("Helvetica", 11, "bold"),
            bootstyle="secondary"
        )
        self.label_instrucao.pack(pady=10)
        
        self.frame_botoes = tk.Frame(janela)
        self.frame_botoes.pack(fill=BOTH, expand=True, padx=40)
        
        self.criar_botoes()

    def criar_botoes(self):
        for botao in self.frame_botoes.winfo_children():
            botao.destroy()
        
        modalidades = self.modalidades.ver_modalidades()
        for mod in modalidades:
            vagas = modalidades[mod]["QuantidadeVagas"]
            btn_mod = tk.Button(
                self.frame_botoes,
                text=f"{mod}\n{str(vagas)} Vagas restantes",
                bootstyle="info-outline",
                cursor="hand2",
                command=lambda m=mod: self.abrir_janela_confirmacao(m)
            )
            btn_mod.pack(pady=5, fill=X)

    def abrir_janela_confirmacao(self, modalidade_escolhida):
        opcoes = self.modalidades.ver_modalidades()
        vagas = opcoes[modalidade_escolhida].get("QuantidadeVagas", 0) 
        if vagas <= 0:
            messagebox.showinfo("Atenção", "Todas as vagas foram preenchidas", parent=self.janela)
            return
        self.janela_cadastro = tk.Toplevel(self.janela)
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
        self.modalidades.adiionar_aluno(nome, matricula, modalidade)
        self.janela_cadastro.destroy()
        self.criar_botoes()

