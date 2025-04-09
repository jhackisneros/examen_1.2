import csv
import os

def guardar_soluciones(n, soluciones):
    """
    Guarda las soluciones en un archivo CSV dentro de la carpeta 'juego_reina', evitando duplicados para un número específico de reinas.

    :param n: Número de reinas.
    :param soluciones: Lista de soluciones para el problema de las n-reinas.
    """
    # Construir la ruta del archivo CSV dentro de la carpeta 'juego_reina'
    carpeta = os.path.dirname(__file__)  # Ruta de la carpeta actual
    archivo_csv = os.path.join(carpeta, 'soluciones.csv')

    # Leer las soluciones existentes del archivo CSV
    soluciones_existentes = set()
    if os.path.exists(archivo_csv):
        with open(archivo_csv, mode='r', newline='', encoding='utf-8') as archivo:
            lector = csv.reader(archivo)
            for fila in lector:
                if fila and int(fila[0]) == n:  # Verificar que sea del mismo tamaño de tablero
                    soluciones_existentes.add(fila[1])

    # Filtrar las soluciones nuevas que no estén ya en el archivo
    nuevas_soluciones = [sol for sol in soluciones if str(sol) not in soluciones_existentes]

    # Guardar las nuevas soluciones en el archivo CSV
    if nuevas_soluciones:
        with open(archivo_csv, mode='a', newline='', encoding='utf-8') as archivo:
            escritor = csv.writer(archivo)
            for solucion in nuevas_soluciones:
                escritor.writerow([n, solucion])

        print(f"Se guardaron {len(nuevas_soluciones)} nuevas soluciones para n = {n}.")
    else:
        print(f"No hay soluciones nuevas para guardar para n = {n}.")

