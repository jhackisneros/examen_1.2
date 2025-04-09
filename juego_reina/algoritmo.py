import csv
import os

def resolver_n_reinas(N):
    """
    Resuelve el problema de las N reinas y devuelve una lista de soluciones.
    Cada solución es una lista de enteros, donde el entero en la posición i representa
    la columna en la que se ubica la reina en la fila i.
    """
    soluciones = []
    tablero = [-1] * N  # tablero[i] = columna de la reina en la fila i

    def es_valido(fila, columna):
        # Verifica que colocar una reina en (fila, columna) no cause conflicto con reinas anteriores
        for i in range(fila):
            # Comprueba la columna y ambas diagonales
            if tablero[i] == columna or abs(tablero[i] - columna) == abs(i - fila):
                return False
        return True

    def backtrack(fila):
        # Si se ha alcanzado el final del tablero, se agrega la solución actual
        if fila == N:
            soluciones.append(tablero[:])
            return
        for columna in range(N):
            if es_valido(fila, columna):
                tablero[fila] = columna
                backtrack(fila + 1)
                tablero[fila] = -1  # retrocede

    backtrack(0)
    return soluciones

