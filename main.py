from juego_De_caballo.tablero import TableroVisual
from juego_reina.algoritmo import resolver_n_reinas
from juego_reina.guardarsoluciones import guardar_soluciones
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

def juego_adicional():
    print("¡Bienvenido al problema adicional!")
    # Aquí puedes implementar la lógica para el tercer problema
    print("Este es un espacio reservado para el tercer juego/problema.")

if __name__ == "__main__":
    while True:
        print("\nSeleccione el juego/problema que desea resolver:")
        print("1. Problema del caballo")
        print("2. Problema de las n-reinas")
        print("3. Problema adicional")
        print("4. Salir")
        opcion = input("Ingrese el número de su elección: ")

        if opcion == "1":
            juego_de_caballo()
        elif opcion == "2":
            juego_de_reinas()
        elif opcion == "3":
            juego_adicional()
        elif opcion == "4":
            print("¡Gracias por jugar!")
            break
        else:
            print("Opción no válida. Por favor, intente de nuevo.")