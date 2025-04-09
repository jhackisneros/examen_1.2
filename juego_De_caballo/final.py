from juego_De_caballo.caballo import ProblemaCaballo
import random

class CaballoConRecorrido(ProblemaCaballo):
    def __init__(self, N=8):
        super().__init__(N)
        self.recorrido = []  # Lista para guardar las posiciones visitadas

    def resolver_caballo(self, x, y, paso):
        """
        Sobrescribe el método para guardar el recorrido del caballo.
        """
        if paso == self.N * self.N:
            self.recorrido.append((x, y))  # Guardar la última posición
            return True  # Todas las casillas han sido visitadas

        for dx, dy in self.movimientos_caballo:
            nx, ny = x + dx, y + dy
            if self.es_valido(nx, ny):
                self.tablero[nx][ny] = paso  # Marcar la casilla como visitada
                self.recorrido.append((x, y))  # Guardar la posición actual
                if self.resolver_caballo(nx, ny, paso + 1):
                    return True
                self.tablero[nx][ny] = -1  # Desmarcar (backtracking)
                self.recorrido.pop()  # Eliminar la posición si no es válida

        return False

    def obtener_recorrido(self):
        """Devuelve el recorrido completo del caballo."""
        return self.recorrido


# Ejemplo de uso
if __name__ == "__main__":
    inicio_x = random.randint(0, 7)
    inicio_y = random.randint(0, 7)
    print(f"Posición inicial del caballo: ({inicio_x}, {inicio_y})")

    caballo = CaballoConRecorrido()
    solucion = caballo.resolver(inicio_x, inicio_y)

    if solucion:
        print("¡El caballo visitó todas las casillas!")
        print("Recorrido del caballo:")
        for paso, posicion in enumerate(caballo.obtener_recorrido()):
            print(f"Paso {paso + 1}: {posicion}")
        print("\nTablero final:")
        caballo.imprimir_tablero()
    else:
        print("No se encontró una solución para el recorrido del caballo.")