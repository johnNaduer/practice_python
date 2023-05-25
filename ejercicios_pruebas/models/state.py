#!/usr/bin/python3

from .base_model import basemodel, Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
from .city import city

from os import environ

""" no funcioanra solo el if ya uqe necesita un export = a db """
if environ.get('HBNB_TYPE_STORAGE') == 'db':
    class state(basemodel, Base):
        __tablename__ = 'states'
        name = Column(String(128), nullable=False)
        """ DBStorage: el atributo de clase Ciudades debe representar una relación con la clase 
        Ciudad. Si se elimina el objeto State, todos los objetos City vinculados deben
        eliminarse automáticamente. Además, la referencia de un objeto City a 
        su State debe llamarse state"""
        cities = relationship('city', cascade='all, delete', backref='state')

else:
    class state(basemodel):
        pass
