#!/usr/bin/python3

from sqlalchemy import Column, Integer, String

""" importamos declarative_base para preparar el molde """
from sqlalchemy.ext.declarative import declarative_base


"""creo el molde para crear una tabla"""
Base = declarative_base()

class state(Base):
    __tablename__ = 'state'
    """ nullable quiere decir que no debe tenr campos vacios"""
    id = Column(Integer, primary_key = True, autoincrement = True, nullable = False)
    name = Column(String(128), nullable = False)


class new_name(Base):
    __tablename__ = 'table_names'
    name1 = Column(String(60), primary_key = True, nullable = False)
    name2 = Column(String(60), nullable = False)
