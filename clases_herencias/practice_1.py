class Rectangle:
    def __init__(self, w, h):
        self.width = w
        self.height = h
        print(self)

    def print(self):
        for i in range(self.height):
            print('X' * self.width)

class Square(Rectangle):
    name = "jhoin"
    def imprimir(self):
        print(self.__dict__)
    
    
dato1 = Rectangle(2, 3)
print(dato1)
dato1.print()
dato2 = Square(2, 2)
dato2.name = "jhnozito"
dato2.imprimir()

