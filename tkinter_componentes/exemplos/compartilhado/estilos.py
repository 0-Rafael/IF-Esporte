from tkinter import ttk


COR_FUNDO = "#f4f7fb"
COR_TEXTO = "#1f2937"
COR_DESTAQUE = "#2563eb"
COR_AREA = "#ffffff"
FONTE_TITULO = ("Segoe UI", 18, "bold")
FONTE_SUBTITULO = ("Segoe UI", 12, "bold")
FONTE_TEXTO = ("Segoe UI", 10)


def configurar_estilos():
    estilo = ttk.Style()
    estilo.theme_use("clam")

    estilo.configure(".", font=FONTE_TEXTO)
    estilo.configure("TFrame", background=COR_FUNDO)
    estilo.configure("Area.TFrame", background=COR_AREA)
    estilo.configure("TLabel", background=COR_FUNDO, foreground=COR_TEXTO)
    estilo.configure("Area.TLabel", background=COR_AREA, foreground=COR_TEXTO)
    estilo.configure("Titulo.TLabel", font=FONTE_TITULO, background=COR_FUNDO)
    estilo.configure("Subtitulo.TLabel", font=FONTE_SUBTITULO, background=COR_FUNDO)
    estilo.configure("TButton", padding=(10, 6))
    estilo.configure("Destaque.TButton", foreground=COR_DESTAQUE)
    estilo.configure("TLabelframe", background=COR_FUNDO)
    estilo.configure("TLabelframe.Label", background=COR_FUNDO, foreground=COR_TEXTO)
