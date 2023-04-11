class Persona:
    def __init__(self, nombre, edad):
        self._nombre = nombre
        self._edad = edad

    # Getter para el nombre
    @property
    def nombre(self):
        return self._nombre

    # Setter para el nombre
    @nombre.setter
    def nombre(self, nuevo_nombre):
        self._nombre = nuevo_nombre

    # Getter para la edad
    @property
    def edad(self):
        return self._edad

    # Setter para la edad
    @edad.setter
    def edad(self, nueva_edad):
        if nueva_edad < 0:
            raise ValueError("La edad no puede ser negativa")
        self._edad = nueva_edad

# Crear una instancia de la clase Persona
persona = Persona("Juan", 30)

# Imprimir el nombre y la edad
print("Nombre:", persona.nombre)
print("Edad:", persona.edad)

# Cambiar el nombre y la edad usando los setters
persona.nombre = "Ana"
persona.edad = 25

# Imprimir el nuevo nombre y edad
print("Nuevo nombre:", persona.nombre)
print("Nueva edad:", persona.edad)

