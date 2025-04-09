from juego_De_caballo.caballo import caballo

class TableroVisual:
    def __init__(self, N=8):
        self.N = N
        self.problema_caballo = caballo(N)

    def mostrar_tablero(self, tablero):
        """Muestra el tablero con el recorrido del caballo."""
        print("Recorrido del caballo:")
        for fila in tablero:
            print(" ".join(f"{celda:2}" for celda in fila))

    def ejecutar(self, inicio_x=0, inicio_y=0):
        """Ejecuta el problema del caballo y muestra el tablero."""
        solucion = self.problema_caballo.resolver(inicio_x, inicio_y)
        if solucion:
            self.mostrar_tablero(self.problema_caballo.tablero)
        else:
            print("No se encontró una solución para el recorrido del caballo.")

# Ejemplo de uso
if __name__ == "__main__":
    import random
    inicio_x = random.randint(0, 7)
    inicio_y = random.randint(0, 7)
    print(f"Posición inicial del caballo: ({inicio_x}, {inicio_y})")
    tablero_visual = TableroVisual()
    tablero_visual.ejecutar(inicio_x, inicio_y)