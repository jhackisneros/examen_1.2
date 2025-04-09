from juego_De_caballo.caballo import ProblemaCaballo

class TableroVisual:
    def __init__(self, N=8):
        self.N = N
        self.problema_caballo = ProblemaCaballo(N)

    def convertir_a_notacion_ajedrez(self, x, y):
        """Convierte coordenadas (x, y) a notación de ajedrez (e.g., g4)."""
        columnas = "abcdefgh"
        return f"{columnas[y]}{self.N - x}"

    def mostrar_tablero(self, tablero):
        """Muestra el tablero con el recorrido del caballo en formato ASCII."""
        print("Recorrido del caballo en el tablero:")
        print("   " + " ".join("abcdefgh"))  # Encabezado de columnas
        for i, fila in enumerate(tablero):
            print(f"{self.N - i} | " + " ".join(f"{celda:2}" if celda != -1 else " ." for celda in fila))
        print("   " + " ".join("abcdefgh"))  # Pie de columnas

    def guardar_recorrido(self, recorrido):
        """Guarda el recorrido en notación de ajedrez y como vector."""
        movimientos_ajedrez = []
        vector_recorrido = []

        for x, y in recorrido:
            movimientos_ajedrez.append(self.convertir_a_notacion_ajedrez(x, y))
            vector_recorrido.append((x, y))

        # Guardar en archivos
        with open("movimientos_ajedrez.txt", "w") as f:
            f.write(" -> ".join(movimientos_ajedrez))

        with open("vector_recorrido.txt", "w") as f:
            f.write(str(vector_recorrido))

        print("\nRecorrido guardado en:")
        print("- movimientos_ajedrez.txt (notación de ajedrez)")
        print("- vector_recorrido.txt (vector de posiciones)")

    def ejecutar(self, inicio_x=0, inicio_y=0):
        """Ejecuta el problema del caballo y muestra el tablero."""
        solucion = self.problema_caballo.resolver(inicio_x, inicio_y)
        if solucion:
            self.mostrar_tablero(self.problema_caballo.tablero)
            self.guardar_recorrido(self.problema_caballo.recorrido)
        else:
            print("No se encontró una solución para el recorrido del caballo.")