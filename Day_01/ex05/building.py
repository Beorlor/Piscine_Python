#!/usr/bin/env python3
"""
building.py
Ex05: Programme qui compte différents types de caractères dans une chaîne.
"""

import sys
import string


def count_characters(text: str) -> dict:
    """
    Retourne un dictionnaire contenant le décompte des caractères:
    - total : la longueur totale de la chaîne
    - upper : nombre de lettres majuscules
    - lower : nombre de lettres minuscules
    - punctuation : nombre de signes de ponctuation
    - spaces : nombre d'espaces
    - digits : nombre de chiffres
    """
    counts = {
        "total": len(text),
        "upper": 0,
        "lower": 0,
        "punctuation": 0,
        "spaces": 0,
        "digits": 0
    }

    for char in text:
        if char.isupper():
            counts["upper"] += 1
        elif char.islower():
            counts["lower"] += 1
        elif char.isdigit():
            counts["digits"] += 1
        elif char.isspace():
            # compte aussi les retours à la ligne comme des espaces
            counts["spaces"] += 1
        elif char in string.punctuation:
            counts["punctuation"] += 1

    return counts


def main():
    """
    Point d'entrée principal qui gère:
    - la récupération du texte en paramètre ou en entrée
    - l'affichage des résultats
    - la gestion des erreurs (AssertionError) si plusieurs arguments
    """
    args = sys.argv[1:]

    try:
        if len(args) > 1:
            raise AssertionError("more than one argument is provided")
        if len(args) == 1:
            text_to_count = args[0]
        else:
            print("What is the text to count?")
            text_to_count = sys.stdin.readline()

        counts = count_characters(text_to_count)

        print(f"The text contains {counts['total']} characters:")
        print(f"{counts['upper']} upper letters")
        print(f"{counts['lower']} lower letters")
        print(f"{counts['punctuation']} punctuation marks")
        print(f"{counts['spaces']} spaces")
        print(f"{counts['digits']} digits")

    except AssertionError as e:
        print(f"AssertionError: {e}")


if __name__ == "__main__":
    main()
