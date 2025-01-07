class calculator:
    """A class to perform scalar operations
      (addition, subtraction, multiplication, division) on vectors."""

    def __init__(self, vector):
        """Initialize the calculator with a vector.

        Args:
            vector (list): A list of numerical values representing the vector.
        """
        self.vector = vector

    def __add__(self, scalar):
        """Add a scalar to each element of the vector.

        Args:
            scalar (float): The scalar to add.

        Returns:
            calculator: The current calculator object with the updated vector.
        """
        self.vector = [x + scalar for x in self.vector]
        print(self.vector)
        return self

    def __mul__(self, scalar):
        """Multiply each element of the vector by a scalar.

        Args:
            scalar (float): The scalar to multiply.

        Returns:
            calculator: The current calculator object with the updated vector.
        """
        self.vector = [x * scalar for x in self.vector]
        print(self.vector)
        return self

    def __sub__(self, scalar):
        """Subtract a scalar from each element of the vector.

        Args:
            scalar (float): The scalar to subtract.

        Returns:
            calculator: The current calculator object with the updated vector.
        """
        self.vector = [x - scalar for x in self.vector]
        print(self.vector)
        return self

    def __truediv__(self, scalar):
        """Divide each element of the vector by a scalar.

        Args:
            scalar (float): The scalar to divide.

        Returns:
            calculator: The current calculator object with the updated vector.

        Raises:
            ZeroDivisionError: If scalar is 0.
        """
        if scalar == 0:
            raise ZeroDivisionError("Division by zero is not allowed.")
        self.vector = [x / scalar for x in self.vector]
        print(self.vector)
        return self
