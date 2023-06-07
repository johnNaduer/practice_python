#!/usr/bin/python3

from create_model import place3, Base
from os import getenv
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session
from sqlalchemy.orm import sessionmaker

class DBStorage:
    __engine = None
    __session = None

    def __init__(self):
        user = "johnnaduer" #getenv('HBNB_MYSQL_USER')
        password = "polares123" #getenv('HBNB_MYSQL_PWD')
        host = "localhost" #getenv('HBNB_MYSQL_HOST')
        database = "jh_db_2"#getenv('HBNB_MYSQL_DB')
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.format(user, password, host, database), 
                                      pool_pre_ping=True)

    def all(self, cls=None):
        """ consultar todos los datos de la tabla """
        return self.__session.query(cls).all()


    def get(self, cls, id):
        """Buscar un objeto por su ID"""
        return self.__session.query(cls).get(id)

    def new(self, obj):
        self.__session.add(obj)

    def save(self):
        self.__session.commit()

    def delete(self, obj=None):
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """recarga data de la base de datos"""
        Base.metadata.create_all(self.__engine)
        sess_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(sess_factory)
        self.__session = Session


estorage = DBStorage()
estorage.reload()

"""
datos = {"id":118,"name":"peru", "diponibilidad":"disponible"}
datos2 = place3(**datos)
estorage.new(datos2)
estorage.save()


obj = dato1.all(place)[1]
dato1.delete(obj)
dato1.save()


all_data = estorage.all(place3)
print(all_data)


for objetos in all_data:
    if objetos.id == 115:
        dato1.delete(objetos)
        dato1.save()
        break

for obj3 in all_data:
    print("{} - {} ".format(obj3.id, obj3.name, obj3.diponibilidad))

for ob4 in all_data:
    print("{}".format(ob4.__dict__))




all_data = dato1.all() 
 print(all_data) 

for obj in all_data:
    print(obj)
for obj2 in all_data:
    print(obj2.__dict__)

"""
