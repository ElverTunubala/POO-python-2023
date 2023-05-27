class Triangulo:
    def __init__(self, lado1, lado2, lado3):
        self.lado1 = lado1
        self.lado2 = lado2
        self.lado3 = lado3

    def imprimir_lado_mayor(self):
        lado_mayor = max(self.lado1, self.lado2, self.lado3)
        print("El lado con mayor tamaño es:", lado_mayor)

    def determinar_tipo(self):
        if self.lado1 == self.lado2 == self.lado3:
            tipo = "equilátero"
        elif self.lado1 == self.lado2 or self.lado1 == self.lado3 or self.lado2 == self.lado3:
            tipo = "isósceles"
        else:
            tipo = "escaleno"
        print("El triángulo es de tipo:", tipo)


# Ejemplo de uso
lado1 = float(input("Ingrese el valor del lado 1: "))
lado2 = float(input("Ingrese el valor del lado 2: "))
lado3 = float(input("Ingrese el valor del lado 3: "))

triangulo1 = Triangulo(lado1, lado2, lado3)
triangulo1.imprimir_lado_mayor()
triangulo1.determinar_tipo()
