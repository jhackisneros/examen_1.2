from sqlalchemy import create_engine, Column, Integer, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class CaballoMovimiento(Base):
    tablename = 'caballo_movimientos'
    id = Column(Integer, primary_key=True)
    recorrido = Column(Text)

class ReinaSolucion(Base):
    tablename = 'reina_soluciones'
    id = Column(Integer, primary_key=True)
    solucion = Column(Text)

class HanoiPaso(Base):
    tablename = 'hanoi_pasos'
    id = Column(Integer, primary_key=True)
    pasos = Column(Text)

engine = create_engine('sqlite:///juegos.db')
Session = sessionmaker(bind=engine)
session = Session()

Base.metadata.create_all(engine)