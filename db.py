from sqlalchemy import create_engine, Column, Integer, String, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

# Tabla para el juego del caballo
class CaballoMovimiento(Base):
    __tablename__ = 'caballo_movimientos'
    id = Column(Integer, primary_key=True)
    recorrido = Column(Text)  # Puede almacenar la secuencia de movimientos

# Tabla para el juego de las reinas
class ReinaSolucion(Base):
    __tablename__ = 'reina_soluciones'
    id = Column(Integer, primary_key=True)
    solucion = Column(Text)  # Representación del tablero con reinas

# Tabla para el juego de la torre de hanoi
class HanoiPaso(Base):
    __tablename__ = 'hanoi_pasos'
    id = Column(Integer, primary_key=True)
    pasos = Column(Text)  # Pasos realizados en la solución

# Configuración de la base de datos
engine = create_engine('sqlite:///juegos.db')
Session = sessionmaker(bind=engine)
session = Session()

# Crear todas las tablas
Base.metadata.create_all(engine)