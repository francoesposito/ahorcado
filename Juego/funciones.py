from palabras import palabras 
import random


def seleccionar_categoria() -> str:
    
    llave = random.randint(1,4)
    llave = str(llave)
    
    return llave

    
    
def seleccionar_palabra(llave):
    
    