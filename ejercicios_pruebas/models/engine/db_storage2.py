#!/usr/bin/python3

from models.base_model2 import basemodel, Base
from models.state2 import state
from models.administrador2 import administrador
from models.propiedad2 import propiedad
from models.espacio2 import espacio
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

    def get_espacios_by_propiedad_id(self, propiedad_id):
        return self.__session.query(espacio).filter(espacio.id_propiedad == propiedad_id).all()

    def get_propiedad_by_nombre(self, nombre):
        """Buscar una propiedad por su nombre"""
        return self.__session.query(propiedad).filter_by(nombre=nombre).first()

    def all(self,cls=None):
        """ consultar todos los datos de la tabla """
        return self.__session.query(cls).all()

    def delete(self, obj=None):
        if obj is not None:
            self.__session.delete(obj)

    def get(self, cls, id):
        """Buscar un objeto por su ID"""
        return self.__session.query(cls).get(id)

    def new(self, obj):
        """ add new object in the table """
        self.__session.add(obj)
        self.save()

    def save(self):
        """ save session """
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
