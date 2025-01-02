#!/usr/bin/env python3
"""
filterstring.py
Exercice 06: Programme qui filtre les mots d'une chaîne selon leur longueur.
"""

import sys
from ft_filter import ft_filter

def main():
    """
    - Récupère 2 arguments: la chaîne S et l'entier N
    - Affiche la liste des mots de S dont la longueur est > N
    - Gère les AssertionError si les arguments sont mauvais
    """
    args = sys.argv[1:]

    try:
        if len(args) != 2:
            raise AssertionError("the arguments are bad")

        S = args[0]
        # Essayer de caster le deuxième argument en int
        try:
            N = int(args[1])
        except ValueError:
            raise AssertionError("the arguments are bad")

        # Vérification des types (S doit être une str, N un int)
        if not isinstance(S, str) or not isinstance(N, int):
            raise AssertionError("the arguments are bad")

        # Découpage de la chaîne S en mots
        words = S.split()

        # On veut les mots dont la longueur > N
        # On doit utiliser une list comprehension et un lambda
        # Voici une manière de le faire avec ft_filter :
        filtered_words = ft_filter(lambda w: len(w) > N, words)
        # Comme ft_filter renvoie un générateur, on peut le convertir en liste
        filtered_words_list = [w for w in filtered_words]

        print(filtered_words_list)

    except AssertionError as e:
        print(f"AssertionError: {e}")


if __name__ == "__main__":
    main()
