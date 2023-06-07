#!/usr/bin/python3

from sqlalchemy import Column, Integer, String
from .base_model2 import Base, basemodel
from sqlalchemy.orm import declarative_base


class state(basemodel, Base):
    __tablename__ = 'state2'
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(60), nullable=False)
