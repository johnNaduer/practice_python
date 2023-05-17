#!/usr/bin/python3

from models.state2 import state, Base
from os import getenv
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session
from sqlalchemy.orm import sessionmaker


class DBStorage:
    __engine = None
    __session = None
    user = 'johnnaduer'
    password = 'polares123'
    host = 'localhost'
    database = 'jh_db'
    def __init__(self):
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.format(self.user, self.password, self.host, self.database),
                                      pool_pre_ping=True)

    def all(self,cls=None):
        """ consultar todos los datos de la tabla """
        return self.__session.query(cls).all()

    def new(self, obj):
        self.__session.add(obj)
        self.save()

    def save(self):
        self.__session.commit()

    def reload(self):
        """recarga data de la base de datos"""
        Base.metadata.create_all(self.__engine)
        sess_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(sess_factory)
        self.__session = Session

"""
estorage = DBStorage()
estorage.reload()
"""
