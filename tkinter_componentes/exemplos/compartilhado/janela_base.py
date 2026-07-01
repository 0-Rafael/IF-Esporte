import tkinter as tk
from tkinter import ttk


def centralizar_janela(janela, largura=760, altura=520):
    janela.update_idletasks()
    largura_tela = janela.winfo_screenwidth()
    altura_tela = janela.winfo_screenheight()
    x = (largura_tela - largura) // 2
    y = (altura_tela - altura) // 2
    janela.geometry(f"{largura}x{altura}+{x}+{y}")


def criar_janela_exemplo(janela_pai, titulo, largura=760, altura=520):
    janela = tk.Toplevel(janela_pai)
    janela.title(titulo)
    janela.transient(janela_pai)
    janela.minsize(560, 380)
    centralizar_janela(janela, largura, altura)
    return janela


def criar_area_explicacao(container, titulo, descricao):
    area = ttk.Frame(container)
    area.pack(fill="x", padx=16, pady=(16, 8))

    ttk.Label(area, text=titulo, style="Titulo.TLabel").pack(anchor="w")
    ttk.Label(area, text=descricao, wraplength=700, justify="left").pack(
        anchor="w", pady=(6, 0)
    )

    return area


def executar_exemplo_individual(classe_tela, titulo):
    from exemplos.compartilhado.estilos import configurar_estilos

    janela = tk.Tk()
    janela.title(titulo)
    configurar_estilos()
    classe_tela(janela)
    janela.mainloop()
