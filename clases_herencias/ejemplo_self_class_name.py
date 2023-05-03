#!/usr/bin/python3

class nombre:
    def __init__(self, name):
        self.name = name
        dato = self.__class__
        print(dato2)


class usuario(nombre):
    pass


usuario2 = usuario("kelly")
print(usuario2.__dict__)
print(usuario2.__class__.name)
