# Projeto Tkinter - Componentes

Este projeto apresenta exemplos práticos de interfaces gráficas com Tkinter. O objetivo é mostrar, de forma guiada, os principais componentes disponíveis na biblioteca padrão do Python.

O código foi organizado com Programação Orientada a Objetos: cada tela é representada por uma classe, com responsabilidades simples e métodos pequenos.

## Requisitos

Use Python instalado no Windows. Para verificar:

```bat
python --version
```

O Tkinter já acompanha a instalação padrão do Python em Windows. Não é necessário instalar bibliotecas externas.

## Como executar

Abra o Prompt de Comando, entre na pasta do projeto e execute:

```bat
cd tkinter_componentes
python main.py
```

A tela inicial apresenta todos os exemplos disponíveis e permite abrir cada tela.

## Exemplos disponíveis

1. Janela básica: `Tk`, título, tamanho e redimensionamento.
2. Labels e botões: `Label`, `Button` e eventos de clique.
3. Entrada de texto: `Entry`, `StringVar` e validação simples.
4. Organização com frames: `Frame` e `LabelFrame`.
5. Radio e check: `Radiobutton`, `Checkbutton` e variáveis de controle.
6. Combobox e Spinbox: listas de opções e valores numéricos.
7. Listbox: lista simples com adicionar, remover e selecionar.
8. Área de texto: `Text` para conteúdo com várias linhas.
9. Scale e Progressbar: controle deslizante e barra de progresso.
10. Menu: barra de menu com comandos.
11. Messagebox: caixas de informação, erro e confirmação.
12. Diálogos: seleção de arquivo, pasta e cor.
13. Treeview: tabela com colunas e seleção de linha.
14. Canvas: desenho de formas e interação por clique.
15. Notebook: organização da interface em abas.
16. Gerenciadores de layout: comparação entre `pack`, `grid` e `place`.

## Organização das pastas

Cada exemplo fica em sua própria subpasta dentro de `exemplos`. Isso facilita estudar um tema por vez:

```text
tkinter_componentes/
  main.py
  README.md
  exemplos/
    tela_inicial/
    01_janela_basica/
    02_labels_botoes/
    ...
    compartilhado/
```

A pasta `compartilhado` contém funções reutilizadas por várias telas, como criação de janelas e configuração visual.

## Execução individual

Alguns exemplos também podem ser executados individualmente. A partir da pasta `tkinter_componentes`, use:

```bat
python exemplos\01_janela_basica\janela_basica.py
```

Troque o caminho pelo exemplo que deseja estudar.

## Sugestão de estudo

Comece executando `python main.py`. Depois, abra os arquivos dos exemplos na ordem numérica e compare o código com o comportamento de cada tela.
