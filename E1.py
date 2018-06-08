"""
Given an array of integers [a0, a1, ..., an] (1<=ai<=100) determine which is the most popular number. 

Most popular number appears more times that the others into given array.

If two numbers are equal of popularity algorith must return the minor of them.

Ej: [1, 3, 5, 6, 3, 6, 7, 8, 9, 6] => 6 (six is the most popular number)

"""

from collections import Counter

def popular(l):
    # We use counter, the most common method and get the fit value on the tuple
    return Counter(l).most_common(1)[0][0]


lista = [1, 3, 5, 6, 3, 6, 7, 8, 9, 6]
print("{} is the most popular.".format(popular(lista)))
