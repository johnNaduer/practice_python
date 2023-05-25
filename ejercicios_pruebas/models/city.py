#!/usr/bin/python3

from sqlalchemy import Column, String, Integer, ForeignKey
from .base_model import basemodel, Base

class city(basemodel ,Base):
    __tablename__ = 'cities'
    name = Column(String(128), nullable=False)
    state_id = Column(String(60), ForeignKey('states.id'), nullable=False)

    """ A class representing a city 
    state_id = 
    name = """
