class calculator:
    """A class to perform calculations
    (dot product, addition, subtraction) on vectors."""

    @staticmethod
    def dotproduct(V1: list[float], V2: list[float]) -> None:
        """Calculate the dot product of two vectors.

        Args:
            V1 (list[float]): First vector.
            V2 (list[float]): Second vector.

        Returns:
            None: Prints the result of the dot product.
        """
        result = sum(v1 * v2 for v1, v2 in zip(V1, V2))
        print(f"Dot product is: {result}")

    @staticmethod
    def add_vec(V1: list[float], V2: list[float]) -> None:
        """Calculate the addition of two vectors.

        Args:
            V1 (list[float]): First vector.
            V2 (list[float]): Second vector.

        Returns:
            None: Prints the result of the addition.
        """
        result = [v1 + v2 for v1, v2 in zip(V1, V2)]
        # Ensure .0 is shown
        formatted_result = ", ".join(f"{x:.1f}" for x in result)
        print(f"Add Vector is : [{formatted_result}]")

    @staticmethod
    def sous_vec(V1: list[float], V2: list[float]) -> None:
        """Calculate the subtraction of two vectors.

        Args:
            V1 (list[float]): First vector.
            V2 (list[float]): Second vector.

        Returns:
            None: Prints the result of the subtraction.
        """
        result = [v1 - v2 for v1, v2 in zip(V1, V2)]
        formatted_result = ", ".join(f"{x:.1f}" for x in result)
        print(f"Sous Vector is: [{formatted_result}]")
