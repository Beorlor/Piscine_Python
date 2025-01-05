def slice_me(family: list, start: int, end: int) -> list:
    """
    Prend un tableau 2D, imprime sa forme initiale et retournée,
    et retourne une version tronquée du tableau
    selon les indices `start` et `end`.
    """
    # Validation des types
    if not isinstance(
        family,
        list) or not all(
        isinstance(
            row,
            list) for row in family):
        raise TypeError("Input must be a 2D list.")

    # Validation que toutes les lignes ont la même taille
    if len(set(len(row) for row in family)) != 1:
        raise ValueError("All rows in the 2D array must have the same size.")

    # Dimensions initiales
    initial_shape = (len(family), len(family[0]) if family else 0)
    print(f"My shape is : {initial_shape}")

    # Truncate
    truncated_family = family[start:end]

    # Dimensions après tranchage
    new_shape = (len(truncated_family), len(
        truncated_family[0]) if truncated_family else 0)
    print(f"My new shape is : {new_shape}")

    return truncated_family


def main():
    family = [
        [1.80, 78.4],
        [2.15, 102.7],
        [2.10, 98.5],
        [1.88, 75.2]
    ]
    try:
        # Test 1
        print(slice_me(family, 0, 2))

        # Test 2
        print(slice_me(family, 1, -2))
    except (ValueError, TypeError) as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
