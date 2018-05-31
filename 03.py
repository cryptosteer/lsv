"""
Escribir una clase en python llamada circulo que contenga un radio, con un método que devuelva el área
 y otro que devuelva el perímetro del circulo.
"""
import math


class Figura:

    def descripcion(self):
        return ("Soy una figura")


class Circulo(Figura):

    def __init__(self, radio):
        self.radio = radio

    def area(self):
        a =  math.pi * math.sqrt(self.radio)
        return a

    def perimetro(self):
        p = math.pi * self.radio * 2
        return p

    def descripcion(self):
        return ("Soy un Circulo")


class Cuadrado(Figura):

    def __init__(self, lado):
        self.lado = lado

    def area(self):
        a = math.sqrt(self.lado)
        return a

    def perimetro(self):
     p = 4 * self.lado
     return p

    def descripcion(self):
       # return ("Soy un Cuadrado")
        return (super().descripcion() + " Cuadratica")




class Saludo:

    def area(self):
        return 'Hola soy el area de cualquier figura'

    def perimetro(self):
     return 'Hola soy el perimetro de cualquier figura'




def obtener_area_figura(figura):
   print("El area del " + figura.__class__.__name__ + " es: ", figura.area())
   print("El perimetro del " + figura.__class__.__name__ + " es: ", figura.perimetro())

#def obtener_area_figura(figura):
 #  print("El area del es: ", figura.area())
  # print("El perimetro del es: ", figura.perimetro())



c=Circulo(10)
cu = Cuadrado(5)
sa = Saludo()

#polimorfismo
obtener_area_figura(c)
obtener_area_figura(cu)
obtener_area_figura(sa)


