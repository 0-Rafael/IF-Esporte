import ttkbootstrap as tk
from tkinter import messagebox
from ttkbootstrap.constants import *
from components.database.dados import Modalidades

class JanelaCadastro:
    def __init__(self, janela):
        self.janela = janela
        self.janela.title("Portal de Inscrições")
        self.janela.geometry("420x580") 
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
        self.frame_botoes.pack(fill=BOTH, expand=True, padx=40, pady=(0, 20))
        
        self.criar_botoes()
        self.criar_footer()

    def criar_botoes(self):
        for botao in self.frame_botoes.winfo_children():
            botao.destroy()
        
        modalidades = self.modalidades.ver_modalidades()
        for mod in modalidades:
            vagas = modalidades[mod].get("QuantidadeVagas", 0)
            btn_mod = tk.Button(
                self.frame_botoes,
                text=f"{mod}\n{str(vagas)} Vagas restantes",
                bootstyle="info-outline",
                cursor="hand2",
                command=lambda m=mod: self.abrir_janela_confirmacao(m)
            )
            btn_mod.pack(pady=5, fill=X)

    def criar_footer(self):
        self.frame_footer = tk.Frame(self.janela)
        self.frame_footer.pack(side=BOTTOM, fill=X, pady=15, padx=20)

        btn_nova_mod = tk.Button(
            self.frame_footer, text="Nova Modalidade", bootstyle="success", 
            cursor="hand2", command=self.abrir_nova_modalidade
        )
        btn_nova_mod.pack(side=LEFT, expand=True, fill=X, padx=5)

        btn_lista = tk.Button(
            self.frame_footer, text="Lista/Alunos", bootstyle="info", 
            cursor="hand2", command=self.abrir_lista_alunos
        )
        btn_lista.pack(side=LEFT, expand=True, fill=X, padx=5)

        btn_calendario = tk.Button(
            self.frame_footer, text="Calendário", bootstyle="warning", 
            cursor="hand2", command=self.abrir_calendario
        )
        btn_calendario.pack(side=LEFT, expand=True, fill=X, padx=5)

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

        tk.Label(
            self.janela_cadastro, 
            text=f"Inscrição: {modalidade_escolhida}", 
            font=("Helvetica", 12, "bold"), 
            bootstyle="info"
        ).pack(pady=20)

        tk.Label(self.janela_cadastro, text="Nome do Aluno", font=("Helvetica", 9, "bold")).pack(anchor="w", padx=35)
        self.entry_nome = tk.Entry(self.janela_cadastro, bootstyle="info")
        self.entry_nome.pack(fill=X, padx=35, pady=(2, 12))

        tk.Label(self.janela_cadastro, text="Número de Matrícula", font=("Helvetica", 9, "bold")).pack(anchor="w", padx=35)
        self.entry_matricula = tk.Entry(self.janela_cadastro, bootstyle="info")
        self.entry_matricula.pack(fill=X, padx=35, pady=(2, 20))

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
        elif nome != str or len(matricula) != 14:
            messagebox.showerror("Atenção", "Nome ou matricula inválidos .", parent=self.janela_cadastro)
            return


        mensagem = f"Inscrição realizada!\n\nAluno: {nome}\nModalidade: {modalidade}\nMatrícula: {matricula}"
        messagebox.showinfo("Sucesso!", mensagem)
        self.modalidades.adiionar_aluno(nome, matricula, modalidade)
        self.janela_cadastro.destroy()
        self.criar_botoes() 
    def abrir_nova_modalidade(self):
        janela_nova = tk.Toplevel(self.janela)
        janela_nova.title("Cadastrar Nova Modalidade")
        janela_nova.geometry("360x380")
        janela_nova.grab_set()

        tk.Label(janela_nova, text="Nova Modalidade", font=("Helvetica", 12, "bold"), bootstyle="success").pack(pady=20)

        tk.Label(janela_nova, text="Nome da Modalidade", font=("Helvetica", 9, "bold")).pack(anchor="w", padx=35)
        entrada_modalidade = tk.Entry(janela_nova, bootstyle="success")
        entrada_modalidade.pack(fill=X, padx=35, pady=(2, 12))

        tk.Label(janela_nova, text="Quantidade de Vagas", font=("Helvetica", 9, "bold")).pack(anchor="w", padx=35)
        entrada_vagas = tk.Entry(janela_nova, bootstyle="success")
        entrada_vagas.pack(fill=X, padx=35, pady=(2, 20))

        tk.Label(janela_nova, text="Professor Responsavel", font=("Helvetica", 9, "bold")).pack(anchor="w", padx=35)
        entrada_professor = tk.Entry(janela_nova, bootstyle="success")
        entrada_professor.pack(fill=X, padx=35, pady=(2, 20))

        def salvar_nova_modalidade():
            nome_mod = entrada_modalidade.get().strip()
            vagas_str = entrada_vagas.get().strip()
            
            if not nome_mod or not vagas_str.isdigit() or not entrada_professor:
                messagebox.showerror("Erro", "Preencha o nome e um número válido de vagas.", parent=janela_nova)
                return
                
            messagebox.showinfo("Sucesso", f"Modalidade {nome_mod} cadastrada!", parent=janela_nova)
            self.criar_botoes() 
            janela_nova.destroy()

        tk.Button(janela_nova, text="Salvar Modalidade", command=salvar_nova_modalidade, bootstyle="success").pack(fill=X, padx=35, pady=(0, 10))
        tk.Button(janela_nova, text="Voltar", command=janela_nova.destroy, bootstyle="secondary-outline").pack(fill=X, padx=35)

    def abrir_lista_alunos(self):
        janela_lista = tk.Toplevel(self.janela)
        janela_lista.title("Lista de Modalidades e Alunos")
        janela_lista.geometry("450x400")
        janela_lista.grab_set()

        tk.Label(janela_lista, text="Alunos Matriculados", font=("Helvetica", 12, "bold"), bootstyle="info").pack(pady=15)

        txt_area = tk.Text(janela_lista, wrap=WORD, height=15)
        txt_area.pack(fill=BOTH, expand=True, padx=20, pady=5)
        
        dados = self.modalidades.ver_modalidades()
        texto_exibicao = ""
        for mod, info in dados.items():
            texto_exibicao += f"--- {mod.upper()} ---\n"
            alunos = info.get("Alunos", [])
            if not alunos:
                texto_exibicao += "Nenhum aluno matriculado.\n"
            else:
                for aluno in alunos:
                    texto_exibicao += f"- {aluno}\n"
            texto_exibicao += "\n"
            
        txt_area.insert(END, texto_exibicao)
        txt_area.config(state=DISABLED) 

        tk.Button(janela_lista, text="Voltar", command=janela_lista.destroy, bootstyle="secondary").pack(pady=15, padx=20, fill=X)

    def abrir_calendario(self):
        janela_cal = tk.Toplevel(self.janela)
        janela_cal.title("Calendário Esportivo")
        janela_cal.geometry("400x350")
        janela_cal.grab_set()

        tk.Label(janela_cal, text="Calendário de Eventos", font=("Helvetica", 12, "bold"), bootstyle="warning").pack(pady=15)

        txt_area = tk.Text(janela_cal, wrap=WORD, height=12)
        txt_area.pack(fill=BOTH, expand=True, padx=20, pady=5)


        texto_exibicao = "Calendario modalidades"
        
        txt_area.insert(END, texto_exibicao)
        txt_area.config(state=DISABLED)

        tk.Button(janela_cal, text="Voltar", command=janela_cal.destroy, bootstyle="secondary").pack(pady=15, padx=20, fill=X)