from design import forca
import random


def start(lista_palavras: list) -> None:
  erros = 0
  
  quantia_palavras = len(lista_palavras)
  N = random.randint(0, quantia_palavras - 1)
  palavra = lista_palavras[N]
  
  letras_chutadas = []
  while True:
    #talvez pôr opção de chutar palavra
    limpar()
    mostrar_letras(letras_chutadas)
    forca(erros)
    ganhou = mostrar(palavra, letras_chutadas)
    ganhar_perder(erros, ganhou)
    if erros == 6 or ganhou == 1:
      break
    L = input('Chute uma letra: ')
    letras_chutadas.append(L)
    erros = verificar(erros, L, palavra)
    
def verificar(erros: int, L: str, palavra) -> int:
  x = 0
  for i in palavra:
    if L == i:
      x = 1
      break
  if x == 0:
    erros += 1
  return erros

def mostrar_letras(letras_chutadas: list):
  print('\nletras chutadas')
  tamanho = len(letras_chutadas)

  if tamanho > 0:
    for i in range(tamanho-1):
      print(letras_chutadas[i], end=', ')

    print(letras_chutadas[tamanho - 1])
    print('\n')
      


def mostrar(palavra: str, letras_chutadas: list) -> int:

  ganhou = 1
  for letra in palavra:
      x = 0
      if letra == ' ':
        print(' ', end=' ')
      
      for letra_chutada in letras_chutadas:
        if letra_chutada == letra:
          print(letra, end=' ')
          x = 1
          break
          
      if x == 0 and letra != ' ':
        print('_', end=' ')
        ganhou = 0
        
  print('\n')
  return ganhou

def ganhar_perder(erros: int, ganhou: int):
  if erros == 6:
    mostrar = '''

|---------------|GAME OVER|---------------|

Você perdeu :(
Pressione ENTER para retornar ao menu principal.

'''
    print(mostrar)
    Z = input()
    limpar()

  elif ganhou == 1:
    mostrar = '''
|---------------|CONGRATULATIONS|---------------|

Você ganhou :)
Pressione ENTER para retornar ao menu principal.

'''
    print(mostrar)
    Z = input()
    limpar()
    

def limpar() -> None:
  print('\n' * 50)
    
