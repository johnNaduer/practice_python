#!/usr/bin/python3

from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base
from sqlalchemy import create_engine

Base = declarative_base()

class datos2(Base):
    __tablename__ = 'information3'
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)

engine = create_engine('mysql://johnnaduer:polares123@localhost/hbtn_0e_6_usa')
Base.metadata.create_all(bind=engine)
