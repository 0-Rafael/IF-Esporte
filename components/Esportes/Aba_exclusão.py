import ttkbootstrap as tk
import tkinter as ttk
from tkinter import messagebox
from components.database.dados import Modalidades

class Exclusao:
    def __init__(self,janela_pai):
        self.janela = janela_pai
    
    def remover_aluno(self, list_box: ttk.Listbox, instancia_modalidades: Modalidades, esporte: str, callback=None, callback_atualizacao_principal=None):
        try:
            selecionado = list_box.curselection()
            if not selecionado:
                messagebox.showwarning("Atenção", "Selecione um aluno para remover.", parent=self.janela)
                return
            
            texto = list_box.get(selecionado[0])
            partes = [x.strip() for x in texto.split("--") if x.strip()]
            
            if len(partes) < 2:
                messagebox.showerror("Erro", "Formato inválido do aluno.", parent=self.janela)
                return
            
            nome = partes[0].replace("- ", "").strip().capitalize()
            matricula = partes[1].strip()
            
            instancia_modalidades.remover_aluno(nome, matricula, esporte)
            messagebox.showinfo("Sucesso", f"Aluno {nome} removido!", parent=self.janela)
            
            if callback:
                callback()
            
            if callback_atualizacao_principal:
                callback_atualizacao_principal()
            
        except IndexError:
            messagebox.showwarning("Atenção", "Selecione um aluno para remover.", parent=self.janela)
    def remover_modalidade(self, list_box: ttk.Listbox, instancia_modalidades: Modalidades, esporte: str, callback=None, callback_atualizacao_principal=None):
        if not esporte:
            messagebox.showwarning("Atenção", "Selecione uma modalidade para remover.", parent=self.janela)
            return

        if esporte in instancia_modalidades.ver_modalidades():
            instancia_modalidades.remover_modalidade(esporte)
            messagebox.showinfo("Sucesso", f"Modalidade {esporte} removida", parent=self.janela)
        else:
            messagebox.showerror("Erro", "Modalidade não encontrada.", parent=self.janela)
            return
        if callback:
            callback()

        if callback_atualizacao_principal:
            callback_atualizacao_principal()