#!/usr/bin/python3

from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String
Base = declarative_base()

class nombre:
    __tablename__ = 'information'
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)

    def __init__(self, name):
        self.name = name
        dato = self.__class__.__name__
        estorage.new(self)
        print(dato)

class filestorage:
    __objects = {}
    def new(self, obj):
        key = "{}".format(obj.__class__.__name__)
        self.__objects[key]=obj.name
        print(self.__objects)

class usuario(nombre, Base):
    __tablename__ = 'information2'
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)

class estado(nombre, Base):
    __tablename__ = 'information3'
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)
