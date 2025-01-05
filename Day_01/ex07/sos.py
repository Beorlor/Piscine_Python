#!/usr/bin/env python3
"""
sos.py
Exercice 07: Convertir une chaîne de caractères (alphanum + espace) en code Morse.
"""

import sys

NESTED_MORSE = {
    "A": ".- ", "B": "-... ", "C": "-.-. ", "D": "-.. ", "E": ". ",
    "F": "..-. ", "G": "--. ", "H": ".... ", "I": ".. ", "J": ".--- ",
    "K": "-.- ", "L": ".-.. ", "M": "-- ", "N": "-. ", "O": "--- ",
    "P": ".--. ", "Q": "--.- ", "R": ".-. ", "S": "... ", "T": "- ",
    "U": "..- ", "V": "...- ", "W": ".-- ", "X": "-..- ", "Y": "-.-- ",
    "Z": "--.. ",
    "0": "----- ", "1": ".---- ", "2": "..--- ", "3": "...-- ", "4": "....- ",
    "5": "..... ", "6": "-.... ", "7": "--... ", "8": "---.. ", "9": "----. ",
    " ": "/ "
}


def string_to_morse(text: str) -> str:
    """
    Convertit la chaîne text en code Morse grâce au dictionnaire NESTED_MORSE.
    Renvoie la chaîne Morse résultante.
    """
    # On met en majuscules pour correspondre aux clés du dictionnaire
    text = text.upper()

    # Pour chaque caractère, on va chercher NESTED_MORSE[car].
    # S'il n'existe pas, on peut lever une erreur ou ignorer
    morse_output = []
    for char in text:
        if char not in NESTED_MORSE:
            raise ValueError(f"Character '{char}' is not allowed.")
        morse_output.append(NESTED_MORSE[char])
    # On joint tout sans espace supplémentaire, car chaque code a déjà un
    # espace à la fin (sauf si on veut le couper)
    return "".join(morse_output).rstrip()


def main():
    """
    Gère:
    - Récupération d'un unique argument
    - Conversion en Morse
    - AssertionError si argument invalide
    """
    args = sys.argv[1:]

    try:
        if len(args) != 1:
            raise AssertionError("the arguments are bad")

        input_str = args[0]
        # Vérification du type
        if not isinstance(input_str, str):
            raise AssertionError("the arguments are bad")

        # Conversion
        # Si un caractère n'est pas pris en charge, ValueError sera levé
        morse_str = string_to_morse(input_str)
        print(morse_str.strip())  # On retire un éventuel espace final

    except AssertionError as e:
        print(f"AssertionError: {e}")
    except ValueError as ve:
        # Ce cas arrive si un caractère illicite se trouve dans la chaîne
        print(f"AssertionError: the arguments are bad ({ve})")


if __name__ == "__main__":
    main()
