import math

class RaizCuadrada:
    def __init__(self, numero):
        self.numero = numero

    def calcular_raiz_cuadrada(self):
        if self.numero < 0:
            print("El número debe ser positivo.")
        else:
            raiz = math.sqrt(self.numero)
            print("La raíz cuadrada de", self.numero, "es:", raiz)


# Ejemplo de uso
numero1 = float(input("Ingrese un número: "))
raiz_cuadrada1 = RaizCuadrada(numero1)
raiz_cuadrada1.calcular_raiz_cuadrada()
