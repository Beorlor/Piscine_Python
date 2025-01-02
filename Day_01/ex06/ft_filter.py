#!/usr/bin/env python3
"""
ft_filter.py
Recode de la fonction filter, sans utiliser la fonction intégrée filter.
"""

def ft_filter(function_or_none, iterable):
    """
    ft_filter(function_or_none, iterable) -> filter object (ou liste, selon l'implémentation)
    Comportement similaire à la fonction intégrée filter :
    - Applique function_or_none à chaque élément de iterable.
    - Retourne les éléments pour lesquels la fonction renvoie True.
    - Si function_or_none est None, on filtre les éléments qui sont "True" intrinsèquement.
    """
    if function_or_none is None:
        # equivalent de filter(None, iterable)
        # on renvoie seulement les éléments "truthy"
        return (item for item in iterable if item)
    else:
        return (item for item in iterable if function_or_none(item))


def main():
    """
    Si on exécute ft_filter.py directement, on ne fait rien de spécial.
    """
    pass


if __name__ == "__main__":
    main()
