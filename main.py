import os

from src.Ejercicio1.script import obtener_puntaje as ejercicio1
from src.Ejercicio2.script import capturar as ejercicio2


def menu():
    print("Bienvenido a las respuestas del examen de algoritmos de Jesús Fernando Almanza Loredo")
    res = input('''
*********************************
* A) Respuesta del ejercicio 1  *
* B) Respuesta del ejercicio 2  *
******** Elije una opción *******
$> ''')
    if res.upper() == 'A':
        os.system("clear")
        resultado = ejercicio1()
        print(f'''
********************
* Alice : {resultado[0]}        *
* Bob   : {resultado[1]}        *
********************

Resultado sin procesar: {resultado}''')
        salida()

    elif res.upper() == "B":
        resultado = ejercicio2()
        print(f'''
Resultado final: {resultado}
''')
        salida()
    else:
        os.system("clear")
        print("Opción inválida!")
        menu()


def salida():
    respuesta = input('Deseas salir? (S/N)\n$> ').upper()
    if respuesta == "S":
        print("Hasta luego...")
        exit(0)
    elif respuesta == 'N':
        os.system('clear')
        menu()
    else:
        os.system('clear')
        print("Opción inválida")
        salida()


if __name__ == '__main__':
    menu()
