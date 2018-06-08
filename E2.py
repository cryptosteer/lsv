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
a = 'Yo dono rosas, oro no doy'
b = 'Isaac ni ronca así'
def is_palindromo(x):

    a = x[::-1]
    a = a.lower()
    a = a.strip()

    if x==a:
        print(x," (es palindromo)")
    else:
        print(x," (no es palindromo)")


is_palindromo(a)