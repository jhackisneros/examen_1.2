from juego_De_caballo.tablero import TableroVisual
import random

def juego_de_caballo():
    print("¡Bienvenido al problema del caballo!")
    inicio_x = random.randint(0, 7)
    inicio_y = random.randint(0, 7)
    print(f"Posición inicial del caballo: ({inicio_x}, {inicio_y})")

    tablero_visual = TableroVisual()
    tablero_visual.ejecutar(inicio_x, inicio_y)
def resolver_torre_de_hanoi():
    """Resuelve el problema de la Torre de Hanoi."""
    piramide_egipcia = PuzzlePiramide(3)  # Cambia el número de piedras si es necesario
    solucion = piramide_egipcia.resolver()
    return solucion


if __name__ == "__main__":
    juego_de_caballo()
