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
        self.recorrido = []  # Lista para guardar el recorrido del caballo

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
        self.tablero[x][y] = paso  # Marcar la casilla como visitada
        self.recorrido.append((x, y))  # Guardar la posición actual

        if paso == self.N * self.N - 1:
            return True  # Todas las casillas han sido visitadas

        for dx, dy in self.movimientos_caballo:
            nx, ny = x + dx, y + dy
            if self.es_valido(nx, ny):
                if self.resolver_caballo(nx, ny, paso + 1):
                    return True

        # Backtracking: desmarcar la casilla y eliminar la posición del recorrido
        self.tablero[x][y] = -1
        self.recorrido.pop()
        return False

    def resolver(self, inicio_x=0, inicio_y=0):
        """
        Resuelve el problema del caballo desde una posición inicial.
        :param inicio_x: Posición inicial en el eje X
        :param inicio_y: Posición inicial en el eje Y
        :return: Tablero con la solución o None si no hay solución
        """
        if self.resolver_caballo(inicio_x, inicio_y, 0):
            return self.tablero
        else:
            print("No se encontró solución.")
            return None