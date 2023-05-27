# Abstracción:
from abc import ABC, abstractmethod

class Animal(ABC):
    def __init__(self, nombre):
        self.nombre = nombre

    @abstractmethod
    def hacer_sonido(self):
        pass


# Herencia: 
class Perro(Animal):
    def hacer_sonido(self):
        return "Woof!"

class Gato(Animal):
    def hacer_sonido(self):
        return "Meow!"

class Vaca(Animal):
    def hacer_sonido(self):
        return "Moo!"


# Polimorfismo:
def hacer_sonidos_animales(animales):
    for animal in animales:
        print(animal.nombre + " hace: " + animal.hacer_sonido())


# Encapsulamiento: 

class Persona:
    def __init__(self, nombre, edad):
        self._nombre = nombre
        self._edad = edad

    def get_nombre(self):
        return self._nombre

    def get_edad(self):
        return self._edad


# Ejemplo de uso

# Abstracción
perro = Perro("Firulais")
gato = Gato("Garfield")
vaca = Vaca("Margarita")

# Polimorfismo
animales = [perro, gato, vaca]
hacer_sonidos_animales(animales)

# Encapsulamiento
persona = Persona("Juan", 25)
print("Nombre de la persona:", persona.get_nombre())
print("Edad de la persona:", persona.get_edad())
