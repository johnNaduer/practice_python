#!/usr/bin/python3

from sqlalchemy import Column, Integer, String

from sqlalchemy.orm import declarative_base

Base = declarative_base()

class place3(Base):
    __tablename__ = 'places3'
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(60), nullable=False)
    diponibilidad = Column(String(60), nullable=False)
