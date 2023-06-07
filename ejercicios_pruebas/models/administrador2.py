#!/usr/bin/python3

from sqlalchemy import Column, Integer, String
from .base_model2 import Base, basemodel
from sqlalchemy.orm import declarative_base

class administrador(basemodel, Base):
    __tablename__ = 'administrador2'
    id = Column(Integer, primary_key=True, nullable=False)
    name_aministrador = Column(String(60), nullable=False)
    apellidos_administrador = Column(String(60), nullable=False)
    email_administrador = Column(String(60), nullable=False)
    numero_telefono_administrador = Column(Integer, nullable=False)
    usuario_administrador = Column(String(120), nullable=False)
    contraseña_administrador = Column(String(120), nullable=False)
