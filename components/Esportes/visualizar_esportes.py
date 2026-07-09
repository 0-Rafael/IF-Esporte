import ttkbootstrap as tk
from tkinter import messagebox
from ttkbootstrap.constants import *
from components.database.dados import Modalidades
from components.Users.Cadastro import SeletorDiasModalidade

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
        
        self.container_lista = tk.Frame(janela)
        self.container_lista.pack(fill=BOTH, expand=True, padx=40, pady=(0, 20))

        self.canvas = tk.Canvas(self.container_lista, bd=0, highlightthickness=0)
        self.scrollbar = tk.Scrollbar(self.container_lista, orient="vertical", command=self.canvas.yview)
        self.canvas.configure(yscrollcommand=self.scrollbar.set)
        
        self.frame_botoes = tk.Frame(self.canvas)
        
        self.canvas_window = self.canvas.create_window((0, 0), window=self.frame_botoes, anchor="nw")
        
        self.frame_botoes.bind(
            "<Configure>",
            lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all"))
        )
        
        self.canvas.bind(
            "<Configure>",
            lambda e: self.canvas.itemconfig(self.canvas_window, width=e.width)
        )

        self.canvas.pack(side=LEFT, fill=BOTH, expand=True)
        self.scrollbar.pack(side=RIGHT, fill=Y)

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
        elif any(char.isdigit() for char in nome) or len(matricula) != 14:
            messagebox.showerror("Atenção", "Nome inválido ou matrícula deve ter 14 dígitos.", parent=self.janela_cadastro)
            return

        mensagem = f"Inscrição realizada!\n\nAluno: {nome}\nModalidade: {modalidade}\nMatrícula: {matricula}"
        messagebox.showinfo("Sucesso!", mensagem)
        self.modalidades.adiionar_aluno(nome, matricula, modalidade)
        self.janela_cadastro.destroy()
        self.criar_botoes() 

    def abrir_nova_modalidade(self):
        janela_nova = tk.Toplevel(self.janela)
        janela_nova.title("Cadastrar Nova Modalidade")
        janela_nova.geometry("560x500")
        janela_nova.grab_set()

        tk.Label(janela_nova, text="Nova Modalidade", font=("Helvetica", 12, "bold"), bootstyle="success").pack(pady=20)

        tk.Label(janela_nova, text="Nome da Modalidade", font=("Helvetica", 9, "bold")).pack(anchor="w", padx=35)
        entrada_modalidade = tk.Entry(janela_nova, bootstyle="success")
        entrada_modalidade.pack(fill=X, padx=35, pady=(2, 12))

        tk.Label(janela_nova, text="Quantidade de Vagas", font=("Helvetica", 9, "bold")).pack(anchor="w", padx=35)
        entrada_vagas = tk.Entry(janela_nova, bootstyle="success")
        entrada_vagas.pack(fill=X, padx=35, pady=(2, 20))

        tk.Label(janela_nova, text="Professor/monitor Responsável", font=("Helvetica", 9, "bold")).pack(anchor="w", padx=35)
        entrada_professor = tk.Entry(janela_nova, bootstyle="success")
        entrada_professor.pack(fill=X, padx=35, pady=(2, 20))

        calendario = SeletorDiasModalidade(janela_nova)


        def salvar_nova_modalidade():
            nome_mod = entrada_modalidade.get().strip()
            vagas_str = entrada_vagas.get().strip()
            profesor = entrada_professor.get().strip()
            datas = calendario.obtener_dias_selecionados()
            if not nome_mod or not vagas_str.isdigit() or not profesor or datas==None:
                messagebox.showerror("Erro", "Preencha todos os campos.", parent=janela_nova)
                return
                
            messagebox.showinfo("Sucesso", f"Modalidade {nome_mod} cadastrada!", parent=janela_nova)
            self.modalidades.adicionar_modalidades(nome_mod, int(vagas_str), profesor, datas)
            self.criar_botoes()
            janela_nova.destroy()

        tk.Button(janela_nova, text="Salvar Modalidade", command=salvar_nova_modalidade, bootstyle="success").pack(fill=X, padx=35, pady=(0, 10))
        tk.Button(janela_nova, text="Voltar", command=janela_nova.destroy, bootstyle="secondary-outline").pack(fill=X, padx=35)

    def abrir_lista_alunos(self):
        janela_lista = tk.Toplevel(self.janela)
        janela_lista.title("Lista de Modalidades e Alunos")
        janela_lista.geometry("550x500") 
        janela_lista.grab_set()

        tk.Label(janela_lista, text="Selecione uma Modalidade", font=("Helvetica", 12, "bold"), bootstyle="info").pack(pady=10)

        frame_botoes = tk.Frame(janela_lista)
        frame_botoes.pack(fill=X, padx=20, pady=5)

        scrollbar_botoes = tk.Scrollbar(frame_botoes)
        scrollbar_botoes.pack(side=RIGHT, fill=Y)

        container_botoes = tk.Text(
            frame_botoes, 
            height=4, 
            wrap=WORD, 
            yscrollcommand=scrollbar_botoes.set,
            bg=janela_lista.cget("bg"),
            cursor="arrow"
        )
        container_botoes.pack(side=LEFT, fill=X, expand=True)
        scrollbar_botoes.config(command=container_botoes.yview)

        txt_area = tk.Text(janela_lista, wrap=WORD, height=12)
        txt_area.pack(fill=BOTH, expand=True, padx=20, pady=10)
        txt_area.insert(END, "Clique em uma das modalidades acima para ver os alunos matriculados.")
        txt_area.config(state=DISABLED) 
        
        dados = self.modalidades.ver_modalidades()

        def exibir_alunos_da_modalidade(modalidade_selecionada):
            txt_area.config(state=NORMAL)
            txt_area.delete("1.0", END)
            
            alunos = dados[modalidade_selecionada]['alunos']
            texto_exibicao = f"--- {modalidade_selecionada.upper()} ---\n"
            
            if not alunos:
                texto_exibicao += "Nenhum aluno matriculado.\n"
            else:
                for aluno in alunos:
                    texto_exibicao += f"- {aluno['nome']} -- {aluno['matricula']}\n"
            
            txt_area.insert(END, texto_exibicao)
            txt_area.config(state=DISABLED)

        for mod in dados:
            btn = tk.Button(
                container_botoes, 
                text=mod.upper(), 
                bootstyle="outline-info",
                command=lambda m=mod: exibir_alunos_da_modalidade(m),
                cursor="hand2",
                padding=2
            )
            container_botoes.window_create(END, window=btn)
            container_botoes.insert(END, "  ")

        container_botoes.config(state=DISABLED)
        tk.Button(janela_lista, text="Voltar", command=janela_lista.destroy, bootstyle="secondary").pack(pady=15, padx=20, fill=X)

    def abrir_calendario(self):
        janela_cal = tk.Toplevel(self.janela)
        janela_cal.title("Calendário Esportivo")
        janela_cal.geometry("450x550") 
        janela_cal.grab_set()

        tk.Label(
            janela_cal, 
            text="Calendário de treinos da Semana", 
            font=("Helvetica", 14, "bold"), 
            bootstyle="warning"
        ).pack(pady=10)

        container = tk.Frame(janela_cal)
        container.pack(fill=BOTH, expand=True, padx=15, pady=5)

        canvas = tk.Canvas(container, borderwidth=0, highlightthickness=0)
        scrollbar = tk.Scrollbar(container, orient="vertical", command=canvas.yview)
        
        scrollable_frame = tk.Frame(canvas)
        scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )

        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw", width=400)
        canvas.configure(yscrollcommand=scrollbar.set)

        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

        dias_calendario = {}
        dias_semana = ["Segunda-feira", "Terça-feira", "Quarta-feira", "Quinta-feira", "Sexta-feira", "Sábado", "Domingo"]

        for dia in dias_semana:
            frame_dia = tk.LabelFrame(scrollable_frame, text=dia, bootstyle="info", padding=10)
            frame_dia.pack(fill=X, expand=True, pady=8, padx=5)
            
            dias_calendario[dia] = frame_dia
            
            lbl_vazio = tk.Label(frame_dia, text="Nenhum evento agendado", font=("Helvetica", 9, "italic"), foreground="gray")
            lbl_vazio.pack(anchor="w")
            frame_dia.lbl_vazio = lbl_vazio


        dados_modalidades = self.modalidades.ver_modalidades()

        for nome_modalidade, info in dados_modalidades.items():
            dias_treino = info.get("Dias", [])  
            horario = info.get("Horario", "Horário não definido")
            professor = info.get("professor", "Sem responsável")

            for dia in dias_treino:
                if dia in dias_calendario:
                    f_dia = dias_calendario[dia]
                    
                    if hasattr(f_dia, 'lbl_vazio') and f_dia.lbl_vazio.winfo_exists():
                        f_dia.lbl_vazio.destroy()
                    
                    card = tk.Frame(f_dia, bootstyle="light", padding=8)
                    card.pack(fill=X, pady=4)
                    
                    texto_card = f" {nome_modalidade.upper()} - {horario}\n Prof(a): {professor}"
                    tk.Label(card, text=texto_card, font=("Helvetica", 9, "bold"), justify=LEFT).pack(anchor="w")

        tk.Button(
            janela_cal, 
            text="Voltar", 
            command=janela_cal.destroy, 
            bootstyle="secondary"
        ).pack(pady=15, padx=15, fill=X)