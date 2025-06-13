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
    

def ingresar_nombre_usuario(mensaje: str, mensaje_error: str, minimo_len: int, maximo_len: int) -> str:
    nombre_valido = ""
    while True:
        nombre = input(mensaje)
        if minimo_len <= len(nombre) <= maximo_len:
            nombre_valido = nombre
            break
        else: 
            print(mensaje_error)
    
    return nombre_valido

nombre = ingresar_nombre_usuario("Ingresar su nombre: ", "Nombre no valido, reingrese su nombre: ", 3, 15)
print(f"Hola, {nombre}!")


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
    
def calcular_puntuacion_parcial(errores,aciertos):
    puntuacion = errores + aciertos * 3
    return puntuacion

def calcular_puntuacion_final(puntaje_parcial,puntaje_final):
    puntaje_final += puntaje_parcial

llave = seleccionar_categoria()

palabra = seleccionar_palabra(llave, palabras)

print(f"Categoría: {categorias[llave]} \npalabra elegida: {palabra}")