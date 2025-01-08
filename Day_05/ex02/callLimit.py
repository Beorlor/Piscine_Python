from typing import Any, Callable


def callLimit(limit: int) -> Callable:
    """
    Décorateur pour limiter
    le nombre d'appels d'une fonction.
    """
    def callLimiter(function: Callable) -> Callable:
        count = 0  # Variable pour suivre le nombre d'appels

        def limit_function(*args: Any, **kwargs: Any):
            nonlocal count  # Pour modifier 'count' défini dans 'callLimiter'
            if count >= limit:
                # Bloque l'exécution si la limite est dépassée
                print(f"Error: {function} call too many times")
            else:
                count += 1  # Incrémente le compteur
                return function(*args, **kwargs)  # fonction originale

        return limit_function  # Retourne la fonction décorée

    return callLimiter  # Retourne le décorateur
