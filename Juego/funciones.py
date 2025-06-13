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
    palabra_oculta_lista = list(palabra_oculta)
    
    for letra in palabra:
        if letra_ingresada == palabra[i]:
            palabra_oculta_lista[i] = letra_ingresada
        i += 1
    palabra_oculta = "".join(palabra_oculta_lista)
    
        
    return palabra_oculta

def buscar_letra(palabra, letra_ingresada):
    encontrado = False
    for i in range(len(palabra)):
        if letra_ingresada == palabra[i]:
            encontrado = True
            break
    return encontrado

def sumar_errores(palabra, letra_ingresada, errores):
    palabra = list(palabra)
    i = 0 
    for letra in palabra:
        encontrado = buscar_letra(palabra, letra_ingresada)
        if encontrado == False:
            errores += 1
            break
    i += 1
    return errores

def sumar_aciertos(palabra, letra_ingresada, aciertos, palabra_oculta):
    palabra = list(palabra)
    palabra_oculta = palabra_oculta
    i = 0 
    for letra in palabra:
        encontrado = buscar_letra(palabra, letra_ingresada)
        encontrado_palabra_oculta = buscar_letra(palabra_oculta, letra_ingresada)
        if encontrado == True and encontrado_palabra_oculta == False:
            aciertos += 1
            break
    i += 1
    return aciertos

def verificar_estado_juego(palabra:str, palabra_oculta:str, errores:str) -> bool:
    
    termino = False
    
    if (palabra == palabra_oculta) or errores > 7:
        termino = True
        
    return termino
    
def calcular_puntuacion_parcial(errores,aciertos):
    puntuacion = errores + aciertos * 3
    return puntuacion

def calcular_puntuacion_final(puntaje_parcial,puntaje_final):
    puntaje_final += puntaje_parcial
    
def mostrar_palabra_oculta(palabra):
    palabra_oculta = ""
    for letra in palabra:
        palabra_oculta += "_"
    return palabra_oculta


# llave = seleccionar_categoria()

# palabra = seleccionar_palabra(llave, palabras)

# print(f"Categoría: {categorias[llave]} \npalabra elegida: {palabra}")