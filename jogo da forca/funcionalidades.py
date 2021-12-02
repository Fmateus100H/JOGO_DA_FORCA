from game import start
from util import grava_arquivo, ler_arquivo

def menu(opcao: str, nome_arquivo: str):
  if opcao == 'ADD':
    ADD = input('NOVA PALAVRA: ')
    grava_arquivo(ADD, nome_arquivo)
    print('Palavra adicionada!\n')
  else:
    lista_palavras = ler_arquivo(nome_arquivo)
    start(lista_palavras)
