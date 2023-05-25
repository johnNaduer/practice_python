#!/usr/bin/python3

from .base_model import basemodel, Base
from sqlalchemy import Column, String

class user(basemodel, Base):
    """ 
    __tablename__ = 'users'

    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    first_name = Column(String(128), nullable=True)
    last_name = Column(String(128), nullable=True)
    """

    email = ""
    password = ""
    first_name = ""
    last_name = ""

