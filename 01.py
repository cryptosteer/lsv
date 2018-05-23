"""
Imprimir en una linea separados por coma todos los elementos que sean divisibles por 7 y no sean multipolos de 5 entre 20000 y 32000
(Incluyendo estos elementos).Trabajar con listas.
"""
from pprint import pprint

pprint(
    [number for number in range(20000, 32001) if number % 7 == 0 and not number % 5 == 0],
    indent=3,
    compact=True
)
