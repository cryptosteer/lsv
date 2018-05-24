"""
Imprimir en una linea separados por coma todos los elementos que sean divisibles por 7 y no sean multipolos de 5 entre 20000 y 32000 (Incluyendo estos elementos).
Trabajar con listas.
to dos:
1. obtener rangos | listo
2. divisibles por 7 | listo
3. quitar los multiplos de 5 de la lista | listo
4. imprimirlo en una sola linea de codigo |
"""

# Obteniendo rangos
rango = range(20001, 32001)
lists = []
listfive = []
# Rangos divisibles for 7 
for target_list in rango:
    if target_list % 7 == 0:
        
        lists.append(target_list)

# quitar los multiplos de 5
for i in lists:
    if i % 5 != 0:
       listfive.append(i)

for i in listfive:
    print(i, end=", ")

