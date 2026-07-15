import tkinter as tk
import ttkbootstrap as ttk
from ttkbootstrap.constants import *

class SeletorDiasModalidade:
    def __init__(self, root):
        
        self.dias_semana = {
            "Segunda": tk.BooleanVar(value=False),
            "Terça": tk.BooleanVar(value=False),
            "Quarta": tk.BooleanVar(value=False),
            "Quinta": tk.BooleanVar(value=False),
            "Sexta": tk.BooleanVar(value=False),
        }
        frame = ttk.Frame(root, padding=20)
        frame.pack(fill="x")

        ttk.Label(
            frame, 
            text="Selecione os dias da semana para a modalidade:", 
            font=("Helvetica", 12, "bold")
        ).pack(anchor="center", pady=(0, 2))
        frame_dias = ttk.Frame(frame)
        frame_dias.pack(fill="x", pady=5)

        for dia, var in self.dias_semana.items():
            chk = ttk.Checkbutton(
                frame_dias, 
                text=dia[:3],
                variable=var, 
                style="outline-toolbutton", 
                bootstyle="primary"
            )
            chk.pack(side="left", expand=True, fill="x", padx=2)

    def obtener_dias_selecionados(self):
        selecionados = [dia for dia, var in self.dias_semana.items() if var.get()]
        
        if selecionados:
            return selecionados
        else:
            return None
            