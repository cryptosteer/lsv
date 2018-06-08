"""
Dada una cadena de caracteres determine si dicha cadena:

    1. Es palindromo
    2. Es casi-palindromo
    3. No es palindromo

Casi-palindromo con aquellas cadenas que por un caracter pueden ser palindromo:

    Ej: 
        "Yo dono rosas, oro no doy" ---> Palindromo
        "Isaac ni ronca así" ---> Casi-palindromo
"""

def pali(cadena):
        #se captura la cadena y se invierte
        palindromo= (cadena[::-1])
        #se compara las dos cadenas y se deternima si son iguales
        if cadena == palindromo:
        #si es palindromo se imprimira este bloque
                print("La palabra " + cadena + " es polindromo")
        else:
        #si no cumple la condicion se imprimira este bloque
                print("La palabra " + cadena + " no es polindromo")


cadena = str(input('Dame una palabra: '))
op1=pali(cadena)
print(op1)