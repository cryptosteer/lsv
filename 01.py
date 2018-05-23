"""
Imprimir en una linea separados por coma todos los elementos que sean divisibles por 7 y
no sean multipolos de 5 entre 20000 y 32000 (Incluyendo estos elementos).
Trabajar con listas.
"""

values = []
for x in range(2000, 32000):

    if x % 7 == 0 and x % 5 != 0:
        values.append(x)

print(values)


a = [x for x in range(1, 32000) if x % 7 == 0 and x % 5 != 0]
print(a)