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

def is_palindromo(frase: str) -> str:
    """
    Funcion que retorna el estado de palindromidad de una frase.
    :param frase: string python (str) con la frase a verificar.
    :return: mensaje de estado de la frase.
    """
    # Convirtiendo frase a lista excluyendo espacios y comas, y su contenido
    # en minusculas, resultando una lista con los caracteres de la frase.
    normal = [letter.lower() for letter in list(frase) if letter != ' ' and letter != ',']
    reverse = normal.copy()  # Creando una copia de la list de caracteres
    reverse.reverse()  # Reversiando su contenido (caracteres en orden inverso)
    #  Verificando si los caracteres en orden normal (A) se parecen a los
    # de orden inverso (B), si es asi se establece 1 de lo contrario 0
    a = [1 if (A == B) else 0 for A, B in zip(normal, reverse)]
    if all(a):  # Verificando si todos los caracteres dan resultados positivos
        return "Es palindromo"
    elif a.count(0) == 2:
         # Si solo 1 caracter no compagina se dan 2 estados negativos.
        return "Es casi palindromo"
    else:
        # Si no se cumplen ningunas de las anteriores no es palindromo
        return "No es palindromo"


if __name__ == "__main__":
    frases = ["Yo dono rosas, oro no doy", "Isaac ni ronca asi", "Hola"]
    for frase in frases:
        print("="*30)
        print("{} ---> {}".format(frase, is_palindromo(frase)))
