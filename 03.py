"""
Escribir una clase en python llamada circulo que contenga un radio, con un método que devuelva el área y otro que devuelva el perímetro del circulo.
"""
from math import pi

class Figura:
	
	figura = "Ninguno"

	def descripcion(self):
		return "Soy un {}".format(self.figura)

	def area(self):
		print("El area de una figura")
		
	def perimetro(self):
		print("El perimetro de una figura")

	def __str__(self):
		msg = self.descripcion() + "\n"
		msg += "El área es: {}\n".format(self.area())
		msg += "El perimetro es: {}\n".format(self.perimetro())
		msg += "---------------------------------------------"
		return msg
		
	
class Circulo(Figura):
	def __init__(self, radio):
		self.radio = radio
		self.figura = "Circulo"

	def area(self):
		return pi * (self.radio**2)
		
	def perimetro(self):
		return 2*pi*self.radio
		
	def __str__(self):
		return super(Circulo, self).__str__()
		

class Cuadrado(Figura):
	def __init__(self, lado):
		self.lado = lado
		self.figura = "Cuadrado"

	def area(self):
		return self.lado**2
		
	def perimetro(self):
		return self.lado * 4
		
	def __str__(self):
		return super(Cuadrado, self).__str__() 

radio = int(input("Digite el radio del circulo: "))
circulo = Circulo(radio)
print(circulo)

lado = int(input("Digite el lado del cuadrado: "))
cuadrado = Cuadrado(lado)
print(cuadrado)