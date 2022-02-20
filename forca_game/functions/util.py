def grava_arquivo(ADD: str, nome_arquivo: str) -> None:
  arquivo = open(nome_arquivo, 'a')
  arquivo.write(f'{ADD}\n')
  arquivo.close()

def ler_arquivo(nome_arquivo: str) -> list:
  arquivo = open(nome_arquivo, 'r')
  palavras = []
  
  for linha in arquivo.readlines():
    linha = linha.replace('\n', '')
    palavra = []
    for posicao in range(len(linha)): 
      letra = linha[posicao]
      palavra.append(letra)
    palavras.append(palavra)
      
  arquivo.close()
  return palavras
