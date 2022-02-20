def forca(erros: int) -> None:

  if erros == 0:
    forca = '''
________      
║      |
║
║
║
║
║
║
╨
'''

  elif erros == 1:
    forca = '''
________      
║      |
║      0   
║
║
║
║
║
╨
'''

  elif erros == 2:
    forca = '''
________      
║      |   
║      0   
║      |   
║      |   
║     
║
║
╨
'''
  elif erros == 3:
    forca = '''
________      
║      |   
║      0   
║     /|    
║      |    
║     
║
║
╨
'''

  elif erros == 4:
    forca = '''     
________      
║      |    
║      0    
║     /|\    
║      |    
║
║
║
╨
'''

  elif erros == 5:
    forca = '''
________      
║      |   
║      0    
║     /|\    
║      |    
║     /     
║
║
╨
'''
    
  elif erros == 6:
    forca = '''
 ________       
 ║      |  
 ║      0  
 ║     /|\  
 ║      |  
 ║     / \  
 ║
 ║
 ╨
'''
  print(forca)
     
