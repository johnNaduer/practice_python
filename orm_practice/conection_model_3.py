#!/usr/bin/python3

from create_model_3 import User, Base
from sqlalchemy import create_engine

engine = create_engine('mysql+mysqldb://johnnaduer:polares123@localhost/jh_db')
Base.metadata.drop_all(engine)
