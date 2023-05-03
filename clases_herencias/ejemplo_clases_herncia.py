#!/usr/bin/python3

dato5 = 10

class nombre:
    def __init__(self, name):
        self.name = name
        dato = self.__class__.__name__
        estorage.new(self)
        print(dato5)

class filestorage:
    __objects = {}
    def new(self, obj):
        key = "{}".format(obj.__class__.__name__)
        self.__objects[key]=obj.name
        print(self.__objects)

class usuario(nombre):
    pass

class estado(nombre):
    pass

classes = {'nombre':nombre, 'usuario':usuario, 'estado':estado}

estorage = filestorage()
dato = 'usuario'
if dato in classes:
    classes[dato]("kelly")
    

estado1 = estado("lima")
