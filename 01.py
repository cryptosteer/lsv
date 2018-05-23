"""
Imprimir en una linea separados por coma todos los elementos que sean divisibles por 7 y no sean multiplos de 5 entre 20000 y 32000 (Incluyendo estos elementos).
Trabajar con listas.
<<<<<<< HEAD
"""

lista = []
for i in range(20000, 32001):
	if i%7==0 and i%5!=0:
		lista.append(i)

print("Elementos divisibles por 7 y no multiplos de 5 entre 20000 y 32000")
for i in lista:
	print(i, end=",") 

