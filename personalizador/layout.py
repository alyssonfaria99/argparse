"""
Lida com funcionalidades de layout utilizando a biblioteca rich.
"""
from rich.layout import Layout
from rich.console import Console

console = Console()

def print1(texto, isArquivo=False):
    """""
    Separa o texto em header, body e footer
    """

    if isArquivo:
        with open(texto, 'r') as arquivo:
            texto = arquivo.read()
    layout = Layout(name="root")
    layout.split(
        Layout(name="header", size=3),
        Layout(name="body", ratio=1),
        Layout(name="footer", size=3)
    )
    layout["header"].update("[bold cyan]Header[/bold cyan]")
    layout["body"].update(f"[green]{texto}[/green]")
    layout["footer"].update("[bold magenta]Footer[/bold magenta]")
    console.print(layout)

def print2(texto, isArquivo=False):
    """
    Exibe o texto centralizado.
    """
    if isArquivo:
        with open(texto, 'r') as arquivo:
            texto = arquivo.read()
        console.print(f"[bold cyan]{texto.center(50)}[/bold cyan]")
    else:
        print(texto)
print1('layout.py', False)
print2('layout.py', False)

