#!/usr/bin/python3

from sqlalchemy import Column, Integer, String

from sqlalchemy.orm import declarative_base

Base = declarative_base()

class place(Base):
    __tablename__ = 'places2'
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(60), nullable=False)
