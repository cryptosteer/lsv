"""
Escribir una clase en python llamada circulo que contenga un radio, con un método que devuelva el área y otro que devuelva el perímetro del circulo.
"""
from math import pi

class Figura:

    def descripcion(self):
        return "soy una figura"




class Circulo (Figura):

    def __init__(self, radio):
        self.radio=radio


    def area(self):
        area_circulo = pi*self.radio**2
        return print("El area del circulo es: {}".format(area_circulo))

    def perimetro (self):
        return print("El perimetro del circulo es: ",2*pi*self.radio)

    def descripcion(self):
        return "soy un circulo"




class Cuadrado(Figura):


    def __init__(self, lado):
        self.lado=lado


    def area (self):
        perimetro=self.lado**2
        return perimetro

    def descripcion(self):
        return "soy un Cuadrado"


miCirculo = Circulo(11)
print(miCirculo.descripcion())

miCuadrado = Cuadrado(12)
print(miCuadrado.area())