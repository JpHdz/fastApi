from config.database import Base;
from sqlalchemy import Column, Integer, String, Float;

class Computadora(Base):
    
    __tablename__ = "computadoras"

    id = Column(Integer, primary_key = True)
    marca = Column(String)
    modelo = Column(String)
    color = Column(String)
    ram = Column(Integer)
    almacenamiento = Column(Integer)
