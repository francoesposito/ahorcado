from palabras import palabras
from funciones import *
import sys
import time

def jugar_ahorcado() -> None:
    seguir = "si"
    primera = True
    leaderboard = []
    nombre = ingresar_nombre_usuario("Ingrese nombre de usuario: ","Error,usuario invalido,reingrese usuario: ",3,10)
    while seguir == "si":
        categoria = seleccionar_categoria()
        palabra = seleccionar_palabra(categoria, palabras)
        palabra_oculta = mostrar_palabra_oculta(palabra)
        termino = False
        errores = 0
        aciertos = 0
        if primera == False:
            seguir = input("¿Seguir jugando? si/no:  ")
            if seguir != "si":
                print(puntuacion_final)
                print(leaderboard)
        while termino != True and seguir == "si":
            inicio = time.time()
            puntuacion_final = 0
            print(f"Categoría: {categoria}\nPalabra: {palabra_oculta}")
            letra = input("Ingrese una letra: ") 
            aciertos = sumar_aciertos(palabra, letra, aciertos, palabra_oculta)
            palabra_oculta = actualizar_palabra_oculta(palabra, palabra_oculta, letra)
            errores = sumar_errores(palabra, letra, errores)
            print(f"Errores: {errores}, aciertos: {aciertos}")
            termino = verificar_estado_juego(palabra, palabra_oculta, errores)
            primera = False
            puntuacion_final += calcular_puntuacion_final(errores,aciertos)
            final = time.time()
            duracion = final - inicio
            print(puntuacion_final)
        guardar_puntuacion(leaderboard,nombre,categoria,palabra,puntuacion_final,duracion)











if __name__ == "__main__":
    sys.exit(jugar_ahorcado())