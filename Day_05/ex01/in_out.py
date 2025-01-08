def square(x: int | float) -> int | float:
    """
    Retourne le carré de x.
    """
    return x * x


def pow(x: int | float) -> int | float:
    """
    Retourne x élevé à la puissance de lui-même.
    """
    return x ** x


def outer(x: int | float, function) -> object:
    """
    Retourne un objet (fonction inner) qui calcule des valeurs successives
    en utilisant x et la fonction donnée.
    """
    count = 0  # Variable d'état pour suivre les appels

    def inner() -> float:
        """
        Fonction interne qui effectue le calcul et met à jour x.
        """
        nonlocal x, count  # Permet de modifier les variables de outer
        count += 1
        result = function(x)
        x = result  # Met à jour x pour le prochain calcul
        return result

    return inner
