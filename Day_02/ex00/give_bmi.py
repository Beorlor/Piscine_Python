def give_bmi(height: list[int | float], weight: list[int | float]) -> list[int | float]:
    """
    Calcule l'IMC (Indice de Masse Corporelle) pour chaque paire (taille, poids).
    """
    # Vérification que les listes sont de la même taille
    if len(height) != len(weight):
        raise ValueError("Height and weight lists must have the same size.")
    
    # Vérification des types
    if not all(isinstance(h, (int, float)) for h in height):
        raise TypeError("Height list must contain only integers or floats.")
    if not all(isinstance(w, (int, float)) for w in weight):
        raise TypeError("Weight list must contain only integers or floats.")
    
    # zip creer un iterateur qui combine les listes qui sont directement consommer pour creer une liste de tout les IMC
    return [w / (h ** 2) for h, w in zip(height, weight)]


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    """
    Retourne une liste de booléens indiquant si chaque IMC dépasse la limite donnée.
    """
    # Vérification du type de la liste BMI
    if not all(isinstance(b, (int, float)) for b in bmi):
        raise TypeError("BMI list must contain only integers or floats.")
    
    # Vérification du type de la limite
    if not isinstance(limit, int):
        raise TypeError("Limit must be an integer.")
    
    return [b > limit for b in bmi]

def main():
    height = [2.71, 1.15]
    weight = [165.3, 38.4]

    try:
        bmi = give_bmi(height, weight)
        print(bmi, type(bmi))

        print(apply_limit(bmi, 26))
    except (ValueError, TypeError) as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
