from juego_De_caballo.tablero import TableroVisual
from juego_De_caballo.hanoi import TorreDeHanoi
import random

def juego_de_caballo():
    print("¡Bienvenido al problema del caballo!")
    inicio_x = random.randint(0, 7)
    inicio_y = random.randint(0, 7)
    print(f"Posición inicial del caballo: ({inicio_x}, {inicio_y})")

    tablero_visual = TableroVisual()
    tablero_visual.ejecutar(inicio_x, inicio_y)

def resolver_torre_de_hanoi():
    print("\n¡Bienvenido al problema de la Torre de Hanoi!")
    num_discos = int(input("Ingrese el número de discos: "))
    hanoi = TorreDeHanoi(num_discos)
    print("\nEstado inicial de los palos:")
    hanoi.mostrar_palos()
    hanoi.resolver()
    hanoi.imprimir_movimientos()

if __name__ == "__main__":
    print("Seleccione el problema que desea resolver:")
    print("1. Problema del Caballo")
    print("2. Torre de Hanoi")
    opcion = input("Ingrese el número de la opción: ")

    if opcion == "1":
        juego_de_caballo()
    elif opcion == "2":
        resolver_torre_de_hanoi()
    else:
        print("Opción no válida.")