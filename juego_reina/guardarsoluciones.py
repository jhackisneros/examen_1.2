import csv
import os

def guardar_soluciones(n, soluciones, archivo_csv):
    """
    Guarda las soluciones en un archivo CSV, evitando duplicados para un número específico de reinas.

    :param n: Número de reinas.
    :param soluciones: Lista de soluciones para el problema de las n-reinas.
    :param archivo_csv: Ruta del archivo CSV donde se guardarán las soluciones.
    """
    # Verificar si el archivo CSV ya existe
    if os.path.exists(archivo_csv):
        with open(archivo_csv, mode='r', newline='', encoding='utf-8') as archivo:
            lector = csv.reader(archivo)
            # Leer los números de reinas ya guardados
            n_guardados = {int(fila[0]) for fila in lector if fila}
    else:
        n_guardados = set()

    # Si ya existen soluciones para este número de reinas, no guardar de nuevo
    if n in n_guardados:
        print(f"Las soluciones para n = {n} ya están guardadas.")
        return

    # Guardar las nuevas soluciones en el archivo CSV
    with open(archivo_csv, mode='a', newline='', encoding='utf-8') as archivo:
        escritor = csv.writer(archivo)
        for solucion in soluciones:
            escritor.writerow([n, solucion])

    print(f"Soluciones para n = {n} guardadas correctamente.")

