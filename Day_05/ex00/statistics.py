from typing import Any, List


def ft_statistics(*args: Any, **kwargs: Any) -> None:
    """
    Calculate statistics (mean, median, quartiles, standard deviation, variance)
    based on the arguments and keyword arguments provided.
    """
    # Tri des arguments numériques
    data = sorted(args)
    n = len(data)

    # Fonctions statistiques
    def mean(data: List[float]) -> float:
        return sum(data) / len(data)

    def median(data: List[float]) -> float:
        mid = len(data) // 2
        if len(data) % 2 == 0:
            return (data[mid - 1] + data[mid]) / 2
        else:
            return data[mid]

    def quartiles(data: List[float]) -> List[float]:
        """Calculate the first and third quartiles (Q1, Q3) of a list of numbers."""
        lower_half = data[:n // 2]
        upper_half = data[n //  2:]

        def calc_median(subset: List[float]) -> float:
            m = len(subset)
            # if m % 2 == 0:
            #     return (subset[m // 2 - 1] + subset[m // 2]) / 2
            # else:
            return subset[m //  2]

        q1 = calc_median(lower_half)
        q3 = calc_median(upper_half)
        return [q1, q3]

    def variance(data: List[float]) -> float:
        m = mean(data)
        return sum((x - m) ** 2 for x in data) / n

    def std(data: List[float]) -> float:
        return variance(data) ** 0.5

    # Mapping des fonctions disponibles
    stats_functions = {
        "mean": mean,
        "median": median,
        "quartile": quartiles,
        "std": std,
        "var": variance,
    }

    # Calcul des statistiques demandées
    for key, value in kwargs.items():
        if value in stats_functions:
            try:
                result = stats_functions[value](data)
                print(f"{value} : {result}")
            except Exception:
                print("ERROR")
