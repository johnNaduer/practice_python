respecto este codigo:
class Rectangle:
    def __init__(self, w, h):
        self.width = w
        self.height = h

    def print(self):
        for i in range(self.height):
            print('X' * self.width)

class Square(Rectangle):
    def __init__(self, size):
        super().__init__(size, size)

class Square(Rectangle):
    def __init__(self, size):
        super().__init__(size, size)
        self.color = 'white'  # atributo adicional para el color del cuadrado
    
    def calculate_area(self):
        return self.width * self.width

class Square(Rectangle):
    def __init__(self, size):
        super().__init__(size, size)
        self.color = 'white'  # atributo adicional para el color del cuadrado
    
    def calculate_area(self):
        return self.width * self.height

class Square(Rectangle):
    def __init__(self, size):
        super().__init__(size, size)
        self.color = 'white'  # atributo adicional para el color del cuadrado
        self.width = 10
        self.height = 20

class Square(Rectangle):
    def __init__(self, size):
        super().__init__(size, size)
        self.color = 'white'  # atributo adicional para el color del cuadrado
        self.width = 10
        self.height = 20

