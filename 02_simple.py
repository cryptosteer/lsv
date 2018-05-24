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
from math import sqrt
from pprint import pprint

def Q(D: int) -> float:
    return sqrt((2 * 50 * D)/30)


def show_results(D: list) -> None:
    print("-"*10)
    print("Soluciones")
    print("="*10)
    for key,value in D:
        print("Numero {0} = {1}".format(key, value))
    print("="*10)


def main():
    while True:
        D = input("Ingrese lista de valores de x <ej. 18,22,24>: ")
        D = D.split(',')
        try:
            D = [tuple( ( value, Q(int(value)) ) ) for value in D ]
            show_results(D)
            break
        except ValueError:
            print("Ingrese la informacion en el formato correcto")

if __name__ == "__main__":
    main()
