from juego_reina.guardarsoluciones import guardar_soluciones

def resolver_n_reinas(N):
    soluciones = []
    tablero = [-1] * N  # tablero[i] = columna de la reina en la fila i

    def es_valido(fila, columna):
        for i in range(fila):
            if tablero[i] == columna or \
               abs(tablero[i] - columna) == abs(i - fila):
                return False
        return True

    def backtrack(fila):
        if fila == N:
            soluciones.append(tablero[:])
            return
        for columna in range(N):
            if es_valido(fila, columna):
                tablero[fila] = columna
                backtrack(fila + 1)
                tablero[fila] = -1  # deshacer

    backtrack(0)
    return soluciones

# Ejemplo: mostrar soluciones para N=8
sols = resolver_n_reinas(int(input("Introduce el tamaño del tablero (N): ")))
print(f"Se encontraron {len(sols)} soluciones")
