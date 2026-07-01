import importlib
import tkinter as tk
from tkinter import ttk


def carregar_classe(caminho_modulo, nome_classe):
    modulo = importlib.import_module(caminho_modulo)
    return getattr(modulo, nome_classe)


class TelaInicial:
    def __init__(self, janela):
        self.janela = janela
        self.exemplos = [
            ("01", "Janela básica", "Tk, título, tamanho e propriedades da janela.", "exemplos.01_janela_basica.janela_basica", "TelaJanelaBasica"),
            ("02", "Labels e botões", "Label, Button e eventos de clique.", "exemplos.02_labels_botoes.labels_botoes", "TelaLabelsBotoes"),
            ("03", "Entrada de texto", "Entry, StringVar e validação simples.", "exemplos.03_entry_texto.entry_texto", "TelaEntryTexto"),
            ("04", "Organização com frames", "Frame e LabelFrame para agrupar componentes.", "exemplos.04_frame_organizacao.frame_organizacao", "TelaFrameOrganizacao"),
            ("05", "Radio e check", "Radiobutton, Checkbutton e variáveis de controle.", "exemplos.05_radio_check.radio_check", "TelaRadioCheck"),
            ("06", "Combobox e Spinbox", "Escolha de opções e valores numéricos.", "exemplos.06_combobox_spinbox.combobox_spinbox", "TelaComboboxSpinbox"),
            ("07", "Listbox", "Lista com adicionar, remover e selecionar itens.", "exemplos.07_listbox.listbox", "TelaListbox"),
            ("08", "Área de texto", "Text para edição de conteúdo multilinha.", "exemplos.08_text_area.text_area", "TelaTextArea"),
            ("09", "Scale e Progressbar", "Controle deslizante e barra de progresso.", "exemplos.09_scale_progressbar.scale_progressbar", "TelaScaleProgressbar"),
            ("10", "Menu", "Barra de menu e comandos.", "exemplos.10_menu.menu", "TelaMenu"),
            ("11", "Messagebox", "Mensagens de informação, erro e confirmação.", "exemplos.11_messagebox.messagebox_exemplo", "TelaMessagebox"),
            ("12", "Diálogos", "Filedialog e colorchooser.", "exemplos.12_filedialog_colorchooser.dialogos", "TelaDialogos"),
            ("13", "Treeview", "Tabela com colunas e seleção de linha.", "exemplos.13_treeview_tabela.treeview_tabela", "TelaTreeviewTabela"),
            ("14", "Canvas", "Desenho de formas e interação por clique.", "exemplos.14_canvas_desenho.canvas_desenho", "TelaCanvasDesenho"),
            ("15", "Notebook", "Organização da interface em abas.", "exemplos.15_notebook_abas.notebook_abas", "TelaNotebookAbas"),
            ("16", "Gerenciadores de layout", "Comparação entre pack, grid e place.", "exemplos.16_layout_grid_pack_place.layout_gerenciadores", "TelaLayoutGerenciadores"),
        ]
        self.criar_componentes()

    def criar_componentes(self):
        conteudo = ttk.Frame(self.janela, padding=18)
        conteudo.pack(fill="both", expand=True)

        ttk.Label(conteudo, text="Projeto Tkinter - Componentes", style="Titulo.TLabel").pack(anchor="w")
        ttk.Label(
            conteudo,
            text=(
                "Este projeto reúne exemplos práticos para estudar os principais componentes "
                "do Tkinter. Cada tela mostra um recurso com código pequeno e organizado em classes."
            ),
            wraplength=900,
            justify="left",
        ).pack(anchor="w", pady=(8, 16))

        painel = ttk.Frame(conteudo)
        painel.pack(fill="both", expand=True)

        canvas = self.criar_canvas_com_rolagem(painel)
        lista = ttk.Frame(canvas)
        canvas.create_window((0, 0), window=lista, anchor="nw")
        lista.bind("<Configure>", lambda evento: canvas.configure(scrollregion=canvas.bbox("all")))

        for codigo, titulo, descricao, caminho_modulo, nome_classe in self.exemplos:
            self.criar_linha_exemplo(lista, codigo, titulo, descricao, caminho_modulo, nome_classe)

    def criar_canvas_com_rolagem(self, container):
        quadro = ttk.Frame(container)
        quadro.pack(fill="both", expand=True)

        canvas = tk.Canvas(quadro, highlightthickness=0, background="#f4f7fb")
        barra = ttk.Scrollbar(quadro, orient="vertical", command=canvas.yview)
        canvas.configure(yscrollcommand=barra.set)

        canvas.pack(side="left", fill="both", expand=True)
        barra.pack(side="right", fill="y")
        return canvas

    def criar_linha_exemplo(self, container, codigo, titulo, descricao, caminho_modulo, nome_classe):
        linha = ttk.Frame(container, padding=10, style="Area.TFrame")
        linha.pack(fill="x", pady=5)

        texto = ttk.Frame(linha, style="Area.TFrame")
        texto.pack(side="left", fill="x", expand=True)

        ttk.Label(texto, text=f"{codigo}. {titulo}", style="Area.TLabel").pack(anchor="w")
        ttk.Label(texto, text=descricao, style="Area.TLabel", wraplength=650).pack(anchor="w", pady=(3, 0))

        ttk.Button(
            linha,
            text="Abrir",
            style="Destaque.TButton",
            command=lambda: carregar_classe(caminho_modulo, nome_classe)(self.janela),
        ).pack(side="right", padx=(12, 0))
