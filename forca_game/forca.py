from functions.funcionalidades import menu

#PRINCIPAL

nome_arquivo = 'run\word\palavras.txt'

def menu_principal():
  while True:
    name = '''
|---------------| JOGO DA FORCA |---------------|
'''
    print(name)
    print('Pressione ENTER para iniciar')
    print('Digite ADD para adicionar uma nova palavra\n')
    opcao = input()
    menu(opcao, nome_arquivo)

menu_principal()
