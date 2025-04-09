import csv

def guardar_soluciones(nombre_archivo, soluciones):
    """
    Guarda las soluciones del problema de las n-reinas en un archivo CSV.

    :param nombre_archivo: Nombre del archivo CSV donde se guardarán las soluciones.
    :param soluciones: Diccionario con las soluciones. Ejemplo:
                       {
                           4: [[1, 3, 0, 2], [2, 0, 3, 1]],
                           5: [[0, 2, 4, 1, 3]]
                       }
    """
    with open(nombre_archivo, mode='w', newline='', encoding='utf-8') as archivo_csv:
        escritor = csv.writer(archivo_csv)
        # Escribir encabezados
        escritor.writerow(['n-reinas', 'soluciones distintas', 'todas las soluciones', 'una solución'])

        for n, lista_soluciones in soluciones.items():
            num_soluciones = len(lista_soluciones)
            todas_las_soluciones = '; '.join(map(str, lista_soluciones))
            una_solucion = lista_soluciones[0] if num_soluciones == 1 else ''
            escritor.writerow([n, num_soluciones, todas_las_soluciones, una_solucion])

# Ejemplo de uso
soluciones_ejemplo = {
    4: [[1, 3, 0, 2], [2, 0, 3, 1]],
    5: [[0, 2, 4, 1, 3]],
    6: [[1, 3, 5, 0, 2, 4]]
}

guardar_soluciones('soluciones_n_reinas.csv', soluciones_ejemplo)