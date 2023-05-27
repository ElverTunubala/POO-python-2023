class Estudiante:
    def __init__(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota

    def imprimir_datos(self):
        print("Nombre del estudiante:", self.nombre)
        print("Nota del estudiante:", self.nota)

    def mostrar_resultado(self):
        if self.nota >= 5:
            resultado = "Aprobado"
        else:
            resultado = "Reprobado"
        print("El estudiante", self.nombre, "ha", resultado, "con una nota de", self.nota)


# Ejemplo de uso
estudiante1 = Estudiante("Juan", 8)
estudiante1.imprimir_datos()
estudiante1.mostrar_resultado()
