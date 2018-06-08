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

def is_palindromo(frase: str) -> bool:
    normal = [letter.lower() for letter in list(frase) if letter != ' ' and letter != ',']
    reverse = normal.copy()
    reverse.reverse()
    a = [1 if (A == B) else 0 for A, B in zip(normal, reverse)]
    if all(a):
        return "Es palindromo"
    elif a.count(0) == 2:
        return "Es casi palindromo"
    else:
        return "No es palindromo"
    # Complete

if __name__ == "__main__":
    frases = ["Yo dono rosas, oro no doy", "Isaac ni ronca asi", "Hola"]
    for frase in frases:
        print("="*30)
        print("{} ---> {}".format(frase, is_palindromo(frase)))
