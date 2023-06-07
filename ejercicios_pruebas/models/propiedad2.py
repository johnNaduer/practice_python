#!/usr/bin/python3

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from .administrador2 import administrador
from .base_model2 import basemodel, Base
from sqlalchemy.orm import declarative_base

class propiedad(basemodel, Base):
    __tablename__ = 'propiedad2'
    id = Column(Integer, primary_key=True, nullable=False)
    id_administrador = Column(Integer, ForeignKey('administrador2.id'), nullable=False)
    nombre = Column(String(100), nullable=False)
    direccion = Column(String(200), nullable=False)
    numero_telefono = Column(String(20), nullable=False)
    descripcion = Column(String(200), nullable=False)

    administrador = relationship("administrador", backref="propiedades")
