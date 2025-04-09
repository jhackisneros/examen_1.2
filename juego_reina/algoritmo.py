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

def guardar_soluciones_csv(soluciones, nombre_archivo):
    """
    Guarda la lista de soluciones en un archivo CSV.
    Cada fila del CSV representa una solución, donde cada columna indica
    la posición (columna) en la que se colocó la reina en la fila correspondiente.
    """
    # Determina la ruta para guardar el CSV en la misma carpeta que este módulo
    ruta_archivo = os.path.join(os.path.dirname(__file__), nombre_archivo)
    with open(ruta_archivo, mode='w', newline='', encoding='utf-8') as archivo:
        writer = csv.writer(archivo)
        # Escribe una cabecera opcional (puedes modificarla o eliminarla)
        if soluciones:
            N = len(soluciones[0])
            cabecera = [f"Fila{i}" for i in range(N)]
            writer.writerow(cabecera)
        # Escribe cada solución en una línea del CSV
        for sol in soluciones:
            writer.writerow(sol)