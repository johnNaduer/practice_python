#!/usr/bin/python3

import models

from sqlalchemy import create_engine
from os import environ
from sqlalchemy.orm import scoped_session
from sqlalchemy.orm import sessionmaker

from .base_model import Base, basemodel 
from .user import user
from .amenity import amenity
from .city import city
from .place import place
from .state import state
from .review import review

class DBStorage:
    __engine = None
    __session = None

    def __init__(self):
        user = environ.get('HBNB_MYSQL_USER')
        password = environ.get('HBNB_MYSQL_PWD')
        host = environ.get('HBNB_MYSQL_HOST')
        database = environ.get('HBNB_MYSQL_DB')
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.format(user, password, host, database), 
                                      pool_pre_ping=True)

        if environ.get('HBNB') == 'test':
            self.__engine.drop_all()

    def new(self, obj):
        """ add objects in the db """
        self.__session.add(obj)
        self.save()

    def save(self):
        """ save session """
        self.__session.commit()


    def reload(self):
        """ reload data in the databases """
        Base.metadata.create_all(self.__engine)
        sess_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(sess_factory)
        self.__session = Session
