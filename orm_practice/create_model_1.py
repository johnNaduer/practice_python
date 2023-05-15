#!/usr/bin/python3
from sqlalchemy import Column, Integer, String

from sqlalchemy.orm import declarative_base

Base = declarative_base()

class datos(Base):
    __tablename__ = 'information'
    id = Column(Integer, primary_key = True, autoincrement = True, nullable = False)
    name = Column(String(128), nullable = False)

class datos2:
    __tablename__ = 'information2'
    id = Column(Integer, primary_key = True, autoincrement = True, nullable = False)
    name = Column(String(128), nullable = False)
