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
    def imprimir(self, c, uno, dos):
        self.height = uno
        self.width = dos
        for i in range(self.height):
            print(c * self.width)
    

dato2 = Square(2, 2)
dato2.name = "jhnozito"
dato2.imprimir('c', 2 , 3)
