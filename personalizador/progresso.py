"""
Lida com funcionalidades de barras de progresso utilizando a biblioteca rich.
"""
from rich.progress import Progress
from time import sleep

def barra_progresso_simples(texto, isArquivo=False):
    """
    Exibe uma barra de progresso com base no comprimento do texto.
    """
    if isArquivo:
        with open(texto, 'r') as arquivo:
            texto = arquivo.read()
    with Progress() as progress:
        tarefa = progress.add_task("Carregando...", total=len(texto))
        for _ in texto:
            sleep(0.02)
            progress.advance(tarefa)

def barra_progresso_arquivo(texto, isArquivo=False):
    """
    Simula progresso ao carregar um arquivo.
    """
    if isArquivo:
        with open(texto, 'r') as arquivo:
            texto = arquivo.read()
    with Progress() as progress:
        tarefa = progress.add_task("Processando arquivo...", total=100)
        for i in range(100):
            sleep(0.02)
            progress.advance(tarefa)

barra_progresso_arquivo('layout.py',False)