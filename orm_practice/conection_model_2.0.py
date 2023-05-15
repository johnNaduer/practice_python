#!/usr/bin/python3

from create_model_2 import nombre, usuario, estado, Base
from sqlalchemy import create_engine
from os import getenv

db_user = getenv('HBNB_MYSQL_USER')
db_password = getenv('HBNB_MYSQL_PWD')
db_host = getenv('HBNB_MYSQL_HOST')
db_name = getenv('HBNB_MYSQL_DB')

if __name__ == '__main__':
    engine = create_engine(f"mysql+mysqldb://{db_user}:{db_password}@{db_host}/{db_name}")
    Base.metadata.create_all(engine)
