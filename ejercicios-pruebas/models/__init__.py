#!/usr/bin/python3

from models.engine.db_storage2 import DBStorage 

estorage = DBStorage()
estorage.reload()


"""
initializar models packetes


from os import environ

storage_t = environ.get('HBNB_TYPE_STORAGE')

if storage_t == 'db':
    from .db_storage import DBStorage
    estorage = DBStorage() 
else:
    from .file_storage import filestorage
    estorage = filestorage()

estorage.reload()

"""
