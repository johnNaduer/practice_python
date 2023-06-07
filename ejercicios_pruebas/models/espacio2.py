#!/usr/bin/python3

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from .propiedad2 import propiedad
from .base_model2 import basemodel, Base
from sqlalchemy.orm import declarative_base

class espacio(basemodel, Base):
    __tablename__ = 'espacio2'
    id = Column(Integer, primary_key=True, nullable=False)
    id_propiedad = Column(Integer, ForeignKey('propiedad2.id'), nullable=False)
    numero = Column(Integer, nullable=False)
    descripcion = Column(String(200), nullable=False)
    precio = Column(String(20), nullable=False)
    disponibilidad = Column(String(20), nullable=False)

    propiedad = relationship("propiedad", backref="espacios")
