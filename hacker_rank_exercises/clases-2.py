#!/usr/bin/python3

class nombre:
    def __init__(self):
        self.name = ""
        self.apellido = ""

    def obtener_dato(self):
        name = self.name
        apellido = self.apellido

    def imprimir(self):
        print("{} - {}".format(name, apellido))


dato1 = nombre()
dato1.name = "mirella"
dato1.apellido = "cubas"
dato1.imprimir()
