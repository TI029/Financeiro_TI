### estrutura dos arquivos
# main.py - inicializa a interface
def main():
    from interface import iniciar_interface
    from database import criar_tabela

    criar_tabela()
    iniciar_interface()

if __name__ == "__main__":
    main()