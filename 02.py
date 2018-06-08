"""
Write a program that calculates and prints the value according to the given
formula:
Q = Square root of [(2 * C * D)/H]
Following are the fixed values of C and H:
C is 50. H is 30.
D is the variable whose values should be input to your program in a
comma-separated sequence.
Example
Let us assume the following comma separated input sequence is
given to the program:
100,150,180
The output of the program should be:
18,22,24
 
Hints:
If the output received is in decimal form, it should be rounded
off to its nearest value (for example, if the output received is 26.0,
it should be printed as 26)
In case of input data being supplied to the question, it should be assumed
to be a console input.
"""
<<<<<<< HEAD

import math

def calcular():
    C = 50
    H = 30
    entradas = []
    for k in range(3):
        entradas.append(input("Introducir valores para calcular: "))
    print("\nEl resultado es:")
    for i in entradas:
        r = math.sqrt((2 * C * int(i)) / H)
        print(int(r), ",", end="")

calcular()


# ****************************************************************


import math
def calcular():
    C = 50
    H = 30
    entradas = [100 ,150 ,180]
    print("\nEl resultado es:")
    for i in entradas:
        r = math.sqrt((2 * C * i) / H)
        print(int(r), ",", end="")

calcular()


# #****************************************************
=======
from math import sqrt
def calcular():
    cadena =input("ingrese 3 valores separados por ',' : ")
    C=50
    H=30
    numero=[]
    numero=cadena.split(",")
    for iten in numero:
        print (round(sqrt((2 * C * int(iten)/H))), end="," )


calcular()
>>>>>>> 1575cf54374648d680f528485743f2b0c4523a66
