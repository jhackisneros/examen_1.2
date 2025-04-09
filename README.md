# examen_1.2
https://github.com/jhackisneros/examen_1.2.git

# Examen 1.2 - Resolución de Problemas Clásicos con Python

Este proyecto implementa la resolución de tres problemas clásicos utilizando Python y SQLAlchemy para la persistencia de datos. Además, incluye una interfaz gráfica con Gradio para visualizar los resultados.

## Problemas Implementados

### 1. Problema del Caballo
El problema del caballo consiste en encontrar un recorrido en el que un caballo de ajedrez visite todas las casillas de un tablero sin repetir ninguna.  
- **Archivo principal:** `juego_De_caballo/caballo.py`
- **Visualización:** `juego_De_caballo/tablero.py`
- **Resultados guardados:** Recorridos en formato de notación de ajedrez y como vectores.

### 2. Problema de las N Reinas
El problema de las N reinas busca colocar N reinas en un tablero de ajedrez de tamaño NxN de manera que ninguna se ataque entre sí.  
- **Archivo principal:** `juego_reina/algoritmo.py`
- **Resultados guardados:** Soluciones como listas de posiciones.

### 3. Problema de la Torre de Hanoi
El problema de la Torre de Hanoi consiste en mover un conjunto de discos de un palo a otro siguiendo ciertas reglas.  
- **Archivo principal:** `juego_torre_De_hanoi/hanoi.py`
- **Resultados guardados:** Secuencia de movimientos realizados.

## Persistencia de Datos
Los resultados de los problemas se guardan en una base de datos SQLite utilizando SQLAlchemy.  
- **Base de datos:** `juegos.db`
- **Modelos definidos en:** `db.py`
  - `CaballoMovimiento`: Guarda los recorridos del caballo.
  - `ReinaSolucion`: Guarda las soluciones del problema de las N reinas.
  - `HanoiPaso`: Guarda los pasos del problema de la Torre de Hanoi.

## Interfaz Gráfica
Se utiliza Gradio para visualizar los resultados guardados en la base de datos.  
- **Archivo:** `gradio_interface.py`
- **Tabs disponibles:**
  - Recorridos del Caballo
  - Soluciones de las N Reinas
  - Pasos de la Torre de Hanoi

## Requisitos
Instalar las dependencias necesarias desde el archivo `requirements.txt`:
```plaintext
sqlalchemy>=1.4
gradio>=4.0
```

Instalación:
```bash
pip install -r requirements.txt
```

## Ejecución
### Resolución de Problemas
Ejecutar el archivo `main.py` para resolver los problemas y guardar los resultados:
```bash
python main.py
```

### Visualización de Resultados
Ejecutar el archivo `gradio_interface.py` para abrir la interfaz gráfica:
```bash
python gradio_interface.py
```

## Estructura del Proyecto
```
examen_1.2/
│
├── db.py                     # Configuración de la base de datos y modelos SQLAlchemy
├── gradio_interface.py       # Interfaz gráfica para visualizar resultados
├── main.py                   # Menú principal para resolver problemas
├── requirements.txt          # Dependencias del proyecto
├── README.md                 # Documentación del proyecto
│
├── juego_De_caballo/         # Implementación del problema del Caballo
│   ├── __init__.py
│   ├── caballo.py
│   ├── tablero.py
│   └── final.py
│
├── juego_reina/              # Implementación del problema de las N Reinas
│   ├── __init__.py
│   └── algoritmo.py
│
├── juego_torre_De_hanoi/     # Implementación del problema de la Torre de Hanoi
│   ├── __init__.py
│   ├── hanoi.py
│   └── torre_de_hanoi.py
│
├── soluciones_reinas.txt     # Soluciones del problema de las N Reinas
├── movimientos_ajedrez.txt   # Recorridos del Caballo en notación de ajedrez
├── vector_recorrido.txt      # Recorridos del Caballo como vectores
└── juegos.db                 # Base de datos SQLite
```

## Notas
- Asegúrese de que los archivos de resultados (`soluciones_reinas.txt`, `movimientos_ajedrez.txt`, `vector_recorrido.txt`) se generen correctamente al ejecutar los problemas.
- La base de datos `juegos.db` se crea automáticamente al ejecutar el proyecto por primera vez.
