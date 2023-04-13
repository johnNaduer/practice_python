#!/usr/bin/python3

import uuid

class MyClass:
    __objects = {}
    instances = 0

    def __init__(self, name):
        self.id = str(uuid.uuid4())
        self.name = name
        MyClass.__objects[self.id] = self
        MyClass.instances += 1
        self.all()

    def all(self):
        print(MyClass.__objects)

    def count(self, cls=None):
        if cls:
            return len([obj for obj in MyClass.__objects.values() if isinstance(obj, cls)])
        else:
            return MyClass.instances

    def __str__(self):
        return "{} ({})".format(self.name, self.id)

# Ejemplo de uso
obj1 = MyClass("Objeto 1")
obj2 = MyClass("Objeto 2")
obj3 = MyClass("Objeto 3")
print("Número total de objetos:", obj1.count())
print("Número de objetos de la clase MyClass:", obj1.count(cls=MyClass))

