#!/usr/bin/python3

from create_model import place, Base
from os import getenv
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session
from sqlalchemy.orm import sessionmaker

class DBStorage:
    __engine = None
    __session = None

    def __init__(self):
        user = getenv('HBNB_MYSQL_USER')
        password = getenv('HBNB_MYSQL_PWD')
        host = getenv('HBNB_MYSQL_HOST')
        database = getenv('HBNB_MYSQL_DB')
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.format(user, password, host, database), 
                                      pool_pre_ping=True)

    def new(self, obj):
        self.__session.add(obj)

    def save(self):
        self.__session.commit()

    def reload(self):
        """recarga data de la base de datos"""
        Base.metadata.create_all(self.__engine)
        sess_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(sess_factory)
        self.__session = Session

dato1 = DBStorage()
dato1.reload()
datos = {"id":12,"name":"huancayo"}
datos2 = place(**datos)
dato1.new(datos2)
dato1.save()
