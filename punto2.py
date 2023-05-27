class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def mostrar_datos(self):
        print("Nombre:", self.nombre)
        print("Edad:", self.edad)

    def es_mayor_de_edad(self):
        if self.edad >= 18:
            print(self.nombre, "es mayor de edad.")
        else:
            print(self.nombre, "no es mayor de edad.")


# Ejemplo de uso
persona1 = Persona("Juan", 25)
persona1.mostrar_datos()
persona1.es_mayor_de_edad()
