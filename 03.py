"""
Escribir una clase en python llamada circulo que contenga un radio, con un método que devuelva el área y otro que devuelva el perímetro del circulo.
"""
import math
class Circulo:
    def __init__(self,radio):
        self.radio=radio
    def area(self):
        return math.pi*(self.radio**2)
    def perimetro(self):
        return 2*math.pi*self.radio
c=Circulo(int(input("Ingrese el radio deseado: ")))
print("El area del circulo es: ", c.area())
print("El perimetro del circulo es: ", c.perimetro())