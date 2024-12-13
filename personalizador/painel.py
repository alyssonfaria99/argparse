"""""
Lida com funcionalidades de painel utilizando a biblioteca rich.
"""

from rich.panel import Panel
from rich.console import Console

console = Console()

def painel_simples(texto, isArquivo=False):
    """
    Exibe o texto em um painel simples.
    """
    if isArquivo:
        with open(texto, 'r') as arquivo:
            texto = arquivo.read()
    console.print(Panel(texto, title="Painel Simples"))

def painel_com_borda(texto, isArquivo=False):
    """
    Exibe o texto em um painel com borda estilizada.
    """
    if isArquivo:
        with open(texto, 'r') as arquivo:
            texto = arquivo.read()
    console.print(Panel(texto, title="Painel Estilizado", border_style="bright_yellow"))

painel_simples('layout.py',False)
painel_com_borda('layout.py',False)
