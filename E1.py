"""
Given an array of integers [a0, a1, ..., an] (1<=ai<=100) determine which is the most popular number.

Most popular number appears more times that the others into given array.

If two numbers are equal of popularity algorith must return the minor of them.

Ej: [1, 3, 5, 6, 3, 6, 7, 8, 9, 6] => 6 (six is the most popular number)

"""

def popular(l: list) -> int:
    """
    This function get the most popular number on a list of integer numbers.
    :param l: list of integer.
    :return: python integer with the most popular number in the list.
    """
    values = list(set(l))  # Get list orderned ascendent without repeteat values
    count = []
    for val in values:  # Run over all integer values
        num_repeat = l.count(val)  # Get repeat number of values on list.
        count.append(num_repeat)  # Add repeat number to list
    maximun = max(count)  # Get the first maximum numbers repeats
    idx = count.index(maximun)  # Set index of number most popular.
    """
    Note: How the list is on ascendent order the first maximum number is the
    most small
    """
    return values[idx]  # Return number

if __name__ == "__main__":
    listas = [[5, 5, 5, 4, 4, 3, 3, 3],
              [1, 3, 5, 6, 3, 6, 7, 8, 9, 6]
              ]
    for lista in listas:
        print("{} is the most popular.".format(popular(lista)))
