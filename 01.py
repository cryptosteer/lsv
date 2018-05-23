"""
Imprimir en una linea separados por coma todos los elementos que sean divisibles por 7 y no sean multipolos de 5
entre 20000 y 32000 (Incluyendo estos elementos). Trabajar con listas.
"""
list = []
for num in range(20000,32001):
    if(num%7==0 and not(num%5==0)):
        list.append(num);

print(list)

list_comp = [num for num in range(20000,320001) if(num%7==0 and not(num%5==0))]
print("..................................")
print(list_comp)

