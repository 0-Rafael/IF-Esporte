import tkinter as tk
import ttkbootstrap as ttk
from ttkbootstrap.constants import *

class SeletorDiasModalidade:
    def __init__(self, root):
        self.root = root
        self.root.title("Cadastro de Modalidade")
        self.root.geometry("500x300")
        
        # Dicionário para armazenar os dias da semana e suas respectivas variáveis (Booleanas)
        self.dias_semana = {
            "Segunda": tk.BooleanVar(value=False),
            "Terça": tk.BooleanVar(value=False),
            "Quarta": tk.BooleanVar(value=False),
            "Quinta": tk.BooleanVar(value=False),
            "Sexta": tk.BooleanVar(value=False),
        }

        # Frame Principal
        frame = ttk.Frame(root, padding=20)
        frame.pack(fill="both", expand=True)

        # Título / Instrução
        ttk.Label(
            frame, 
            text="Selecione os dias da semana para a modalidade:", 
            font=("Helvetica", 12, "bold")
        ).pack(anchor="w", pady=(0, 15))

        # Frame horizontal para organizar os botões dos dias
        frame_dias = ttk.Frame(frame)
        frame_dias.pack(fill="x", pady=10)

        # Criando os Checkbuttons estilizados como botões (Toolbutton)
        for dia, var in self.dias_semana.items():
            # O estilo 'outline-toolbutton' faz parecer um botão comum que fica "pressionado" quando ativo
            chk = ttk.Checkbutton(
                frame_dias, 
                text=dia[:3], # Mostra apenas as 3 primeiras letras (Seg, Ter, Qua...)
                variable=var, 
                style="outline-toolbutton", 
                bootstyle="primary"
            )
            chk.pack(side="left", expand=True, fill="x", padx=2)

        # Botão para salvar/confirmar
        btn_confirmar = ttk.Button(
            frame, 
            text="Salvar Dias da Modalidade", 
            command=self.obtener_dias_selecionados, 
            bootstyle="success"
        )
        btn_confirmar.pack(pady=25)

        # Label para mostrar o resultado do clique
        self.lbl_resultado = ttk.Label(frame, text="", font=("Helvetica", 10, "italic"))
        self.lbl_resultado.pack(pady=5)

    def obtener_dias_selecionados(self):
        # Filtra o dicionário pegando apenas os dias onde o valor do BooleanVar é True
        selecionados = [dia for dia, var in self.dias_semana.items() if var.get()]
        
        if selecionados:
            texto_resultado = f"Dias selecionados: {', '.join(selecionados)}"
            self.lbl_resultado.config(text=texto_resultado, bootstyle="success")
        else:
            self.lbl_resultado.config(text="Nenhum dia selecionado!", bootstyle="danger")
            
