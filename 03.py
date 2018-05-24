"""
Escribir una clase en python llamada circulo que contenga un radio, con un método que devuelva el área y otro que devuelva el perímetro del circulo.
"""
import math


class Figura:
    def descripcion(self):
        print("Soy una figura")


class Circulo(Figura):
    def __init__(self,radio):
        self.radio=radio

    def area(self):
        return math.pi*(self.radio**2)

    def perimetro(self):
        return 2*math.pi*self.radio

    def descripcion(self):
        print("Soy un circulo")


class Cuadrado(Figura):
    def __init__(self,lado):
        self.lado=lado

    def area(self):
        return self.lado*self.lado

    def perimetro(self):
        return self.lado*4

    def descripcion(self):
        print("Soy un cuadrado")

# c=Circulo(int(input("Ingrese el radio deseado: ")))
circulo=Circulo(8)
print("El area del circulo es: ", circulo.area())
print("El perimetro del circulo es: ", circulo.perimetro())
circulo.descripcion()
cuadrado=Cuadrado(2)
print("El area del cuadrado es: ", cuadrado.area())
print("El perimetro del cuadrado es: ", cuadrado.perimetro())
cuadrado.descripcion()