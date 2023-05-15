#!/usr/bin/python3

from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base
Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    name = Column(String(128), primary_key=True, nullable=False)
    email = Column(String(128), nullable=False)
