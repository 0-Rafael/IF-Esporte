from components.Esportes.visualizar_esportes import JanelaCadastro
def main():
    import tkinter as tk

    janela = tk.Tk()
    janela.title("Projeto Tkinter - Componentes")
    janela.geometry("980x680")
    janela.minsize(820, 560)
    cadastro = JanelaCadastro(janela)

    janela.mainloop()


if __name__ == "__main__":
    main()
