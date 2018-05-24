"""
Imprimir en una linea separados por coma todos los elementos que sean divisibles por 7 y no sean multipolos de 5 entre 20000 y 32000 (Incluyendo estos elementos).
Trabajar con listas.

"""
from pprint import pprint

data = []
for element in range(20000, 32001):
    if (element % 7 == 0) and ~(element % 5 == 0):
        data.append(element)
pprint(data)
