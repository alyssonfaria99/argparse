import argparse
from personalizador import layout, painel, progresso, estilo

def main():
    parser = argparse.ArgumentParser(description="Processa texto ou arquivos com estilos personalizados.")
    parser.add_argument('texto', type=str, help="Texto ou caminho para arquivo a ser processado.")
    parser.add_argument('-a', '--arquivo', action='store_true', help="Indica que o texto fornecido é um arquivo.")
    parser.add_argument('-m', '--modulo', choices=['layout', 'painel', 'progresso', 'estilo'], help="Escolha o módulo para processar.")
    parser.add_argument(
        '-f', '--funcao',
        choices=[
            'print1', 'print2',
            'painel_com_borda', 'painel_sem_borda',
            'barra_progresso_texto', 'barra_progresso_arquivo',
            'texto_destaque', 'texto_colorido'
        ],
        help="Escolha a função a ser executada no módulo escolhido."
    )

    args = parser.parse_args()

    if args.modulo == 'layout':
        getattr(layout, args.funcao)(args.texto, args.arquivo)
    elif args.modulo == 'painel':
        getattr(painel, args.funcao)(args.texto, args.arquivo)
    elif args.modulo == 'progresso':
        getattr(progresso, args.funcao)(args.texto, args.arquivo)
    elif args.modulo == 'estilo':
        getattr(estilo, args.funcao)(args.texto, args.arquivo)

if __name__ == "__main__":
    main()
