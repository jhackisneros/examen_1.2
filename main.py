from juego_De_caballo.tablero import TableroVisual
from juego_reina.algoritmo import resolver_n_reinas
from juego_reina.guardarsoluciones import guardar_soluciones
from juego_torre_De_hanoi.hanoi import TorreDeHanoi  # Importa la clase TorreDeHanoi
import random

def juego_de_caballo():
    print("¡Bienvenido al problema del caballo!")
    inicio_x = random.randint(0, 7)
    inicio_y = random.randint(0, 7)
    print(f"Posición inicial del caballo: ({inicio_x}, {inicio_y})")

    tablero_visual = TableroVisual()
    tablero_visual.ejecutar(inicio_x, inicio_y)

def juego_de_reinas():
    print("¡Bienvenido al problema de las n-reinas!")
    N = int(input("Introduce el tamaño del tablero (N): "))
    soluciones = resolver_n_reinas(N)
    print(f"Se encontraron {len(soluciones)} soluciones")

    # Guardar las soluciones en el archivo CSV
    archivo_csv = "soluciones_reinas.csv"
    guardar_soluciones(N, soluciones, archivo_csv)

def problema_de_hanoi():
    print("¡Bienvenido al problema de la Torre de Hanoi!")
    num_discos = int(input("Ingrese el número de discos: "))
    hanoi = TorreDeHanoi(num_discos)
    print("\nEstado inicial de los palos:")
    hanoi.mostrar_palos()
    hanoi.resolver()
    hanoi.imprimir_movimientos()

if __name__ == "__main__":
    while True:
        print("\nSeleccione el juego/problema que desea resolver:")
        print("1. Problema del caballo")
        print("2. Problema de las n-reinas")
        print("3. Problema de la Torre de Hanoi")
        print("4. Salir")
        opcion = input("Ingrese el número de su elección: ")

        if opcion.isdigit():
            if opcion == "1":
                juego_de_caballo()
            elif opcion == "2":
                juego_de_reinas()
            elif opcion == "3":
                problema_de_hanoi()
            elif opcion == "4":
                print("¡Gracias por jugar!")
                break
            else:
                print("Opción no válida. Por favor, intente de nuevo.")
        else:
            print("Por favor, ingrese un número válido.")