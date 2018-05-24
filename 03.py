"""
Escribir una clase en python llamada circulo que contenga un radio, con un método que devuelva el área y otro que devuelva el perímetro del circulo.
"""
from math import pi

class Circulo:
	def __init__(self, radio):
		self.radio = radio

	def area(self):
		area = pi * (self.radio**2)
		print("El área del circulo es: ", area)

	def perimetro(self):
		perimetro = 2*pi*self.radio
		print("El perimetro del circulo es: ", perimetro)

radio = int(input("Digite el radio del circulo: "))
c = Circulo(radio)
c.area()
c.perimetro()