from exemplos.compartilhado.estilos import configurar_estilos
from exemplos.tela_inicial.tela_inicial import TelaInicial


def main():
    import tkinter as tk

    janela = tk.Tk()
    janela.title("Projeto Tkinter - Componentes")
    janela.geometry("980x680")
    janela.minsize(820, 560)

    configurar_estilos()
    TelaInicial(janela)

    janela.mainloop()


if __name__ == "__main__":
    main()
