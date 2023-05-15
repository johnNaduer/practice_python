#!/usr/bin/python3

from sys import argv
from create_model_1 import datos, Base, datos2
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(argv[1], argv[2], argv[3]), 
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)
