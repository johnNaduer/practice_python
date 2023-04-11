#!/usr/bin/python3


class obtener_entrada:

    def __init__(self, **kwargs):
        self.hobby = ""
        self.kwargs = kwargs
    
    def __str__(self):
        return "{} - {} - {}".format(self.kwargs["nombre"], self.kwargs["apellido"], self.name)

dato = {"nombre":"john","apellido":"espino"}

nombre = obtener_entrada(**dato)
nombre.hobby = "futbol"
print(nombre)


"""
def getString(self):
def printString(self):
"""
