from palabras import palabras, categorias
import random


def seleccionar_categoria() -> str:
    
    llave = random.randint(1,4)
    llave = str(llave)
    
    return llave


def seleccionar_palabra(llave,diccionario):
    
    indice = random.randint(0,9)
    palabra = diccionario[llave][indice]
    
    return palabra

llave = seleccionar_categoria()

palabra = seleccionar_palabra(llave, palabras)

print(f"Categoría: {categorias[llave]} \npalabra elegida: {palabra}")
    