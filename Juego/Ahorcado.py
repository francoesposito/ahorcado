from palabras import palabras
from funciones import *
import sys

def jugar_ahorcado() -> None:
    seguir = "si"
    primera = True
    while seguir == "si":
        categoria = seleccionar_categoria()
        palabra = seleccionar_palabra(categoria, palabras)
        palabra_oculta = mostrar_palabra_oculta(palabra)
        termino = False
        errores = 0
        aciertos = 0
        if primera == False:
            seguir = input("¿Seguir jugando? si/no:  ")
        while termino != True and seguir == "si":
            print(palabra)
            print(f"Categoría: {categoria}\nPalabra: {palabra_oculta}")
            letra = input("Ingrese una letra: ") 
            aciertos = sumar_aciertos(palabra, letra, aciertos, palabra_oculta)
            palabra_oculta = actualizar_palabra_oculta(palabra, palabra_oculta, letra)
            errores = sumar_errores(palabra, letra, errores)
            print(f"Errores: {errores}, aciertos: {aciertos}")
            termino = verificar_estado_juego(palabra, palabra_oculta, errores)
            primera = False

        











if __name__ == "__main__":
    sys.exit(jugar_ahorcado())