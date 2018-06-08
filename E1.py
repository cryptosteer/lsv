"""
Given an array of integers [a0, a1, ..., an] (1<=ai<=100) determine which is the most popular number. 
Most popular number appears more times that the others into given array.
If two numbers are equal of popularity algorith must return the minor of them.
Ej: [1, 3, 5, 6, 3, 6, 7, 8, 9, 6] => 6 (six is the most popular number)
"""

lista = [1, 3, 5, 6, 3, 6, 7, 8, 9, 6]
pop=0

for i in lista:
    a=lista.count(i)
    if a > pop:
        pop = a
        b=i
print('el numero mas popular es: ',b)

