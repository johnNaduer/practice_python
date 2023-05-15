#!/usr/bin/python3


from model_and_conection_2 import nombre, usuario, estado, Base
from sqlalchemy import create_engine

if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://johnnaduer:polares123@localhost/jh_db')
    Base.metadata.create_all(bind=engine)
