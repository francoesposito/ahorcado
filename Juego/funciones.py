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


def actualizar_palabra_oculta(palabra:str, palabra_oculta:str, letra_ingresada:str) -> str:
    i = 0
    
    for letra in palabra:
        if letra_ingresada == palabra[i]:
            palabra_oculta[i] = palabra_oculta
        i += 1
        
    return palabra_oculta

def verificar_estado_juego(palabra:str, palabra_oculta:str, errores:str) -> bool:
    
    termino = False
    
    if (palabra == palabra_oculta) or errores == 7:
        termino = True
        
    return termino
    

llave = seleccionar_categoria()

palabra = seleccionar_palabra(llave, palabras)

print(f"Categoría: {categorias[llave]} \npalabra elegida: {palabra}")
    