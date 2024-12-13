"""
Lida com funcionalidades de estilização de texto utilizando a biblioteca rich.
"""
from rich.text import Text
from rich.console import Console

console = Console()

def texto_estilizado(texto, isArquivo=False):
    """
    Aplica estilo ao texto e printa.
    """
    
    if isArquivo:
        with open(texto, 'r') as arquivo:
            texto = arquivo.read()
    texto_formatado = Text(texto)
    texto_formatado.stylize("bold red")
    console.print(texto_formatado)

def texto_destaque(texto, isArquivo=False):
    """
    Exibe texto sublinhado e destacado.
    """
    if isArquivo:
        with open(texto, 'r') as arquivo:
            texto = arquivo.read()
    texto_formatado = Text.from_markup(f"[underline bold green]{texto}[/underline bold green]")
    console.print(texto_formatado)

texto_estilizado('ok')
texto_destaque('ok')