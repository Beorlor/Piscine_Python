#!/usr/bin/env python3
"""
Loading.py
Exercice 08: Imiter la barre de progression de tqdm avec ft_tqdm.
"""

import sys
# import time


def ft_tqdm(iterable):
    """
    ft_tqdm(iterable) -> générateur
    Imite le comportement de la fonction tqdm :
    - Affiche une barre de progression
    - Rend chaque élément de iterable
    """
    length = len(iterable)  # Il faut que iterable soit un objet "sized"
    # !!!! a utiliser pour avoir une version plus proche de lorginal
    # start_time = time.time()

    for i, elem in enumerate(iterable):
        # Calcul pourcentage
        percent = (i + 1) / length
        # On peut estimer la vitesse, le temps écoulé, etc.
        bar_length = 30  # longueur visuelle de la barre
        filled = int(bar_length * percent)
        bar_str = "=" * filled + ">" + "." * (bar_length - filled - 1)
        # Ex:  100%|[=========>....]| 33/333
        sys.stdout.write(
            f"\r{int(percent*100)}%|[{bar_str}]| {i+1}/{length}"
        )
        sys.stdout.flush()

        yield elem  # super important, permet davancer literateur

    # A la fin, on force la barre à 100%
    sys.stdout.write(
        f"\r100%|[{'='*(bar_length)}]| {length}/{length}\n"
    )
    sys.stdout.flush()


def main():
    """
    Si on lance Loading.py seul, on ne fait rien de spécial,
    car le vrai test se fait dans tester.py
    """
    pass


if __name__ == "__main__":
    main()
