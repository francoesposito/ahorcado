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

def calcular_puntuacion_parcial(errores,aciertos):
    puntuacion = errores + aciertos * 3
    return puntuacion

llave = seleccionar_categoria()

palabra = seleccionar_palabra(llave, palabras)

print(f"Categoría: {categorias[llave]} \npalabra elegida: {palabra}")