import random
import math

class ProblemaCaballo:
    def __init__(self, N=8):
        self.N = N  # Dimensiones del tablero (N x N)
        self.movimientos_caballo = [
            (2, 1), (1, 2), (-1, 2), (-2, 1),
            (-2, -1), (-1, -2), (1, -2), (2, -1)
        ]
        self.tablero = [[-1 for _ in range(N)] for _ in range(N)]

    def es_valido(self, x, y):
        """Verifica si la posición está dentro del tablero y no ha sido visitada."""
        return 0 <= x < self.N and 0 <= y < self.N and self.tablero[x][y] == -1

    def resolver_caballo(self, x, y, paso):
        """
        Intenta resolver el problema del caballo usando backtracking.
        :param x: Posición actual en el eje X
        :param y: Posición actual en el eje Y
        :param paso: Número del paso actual
        :return: True si se encuentra una solución, False en caso contrario
        """
        if paso == self.N * self.N:
            return True  # Todas las casillas han sido visitadas

        for dx, dy in self.movimientos_caballo:
            nx, ny = x + dx, y + dy
            if self.es_valido(nx, ny):
                self.tablero[nx][ny] = paso  # Marcar la casilla como visitada
                if self.resolver_caballo(nx, ny, paso + 1):
                    return True
                self.tablero[nx][ny] = -1  # Desmarcar (backtracking)

        return False

    def resolver(self, inicio_x=0, inicio_y=0):
        """
        Resuelve el problema del caballo desde una posición inicial.
        :param inicio_x: Posición inicial en el eje X
        :param inicio_y: Posición inicial en el eje Y
        :return: Tablero con la solución o None si no hay solución
        """
        self.tablero[inicio_x][inicio_y] = 0  # Paso inicial
        if self.resolver_caballo(inicio_x, inicio_y, 1):
            return self.tablero
        else:
            print("No se encontró solución.")
            return None

    def imprimir_tablero(self):
        """Imprime el tablero."""