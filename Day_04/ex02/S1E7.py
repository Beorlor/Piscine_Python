from S1E9 import Character


class Baratheon(Character):
    """Representing the Baratheon family."""

    def __init__(self, first_name: str, is_alive: bool = True):
        """Initialize a Baratheon character with specific traits.

        Args:
            first_name (str): The character's first name.
            is_alive (bool): The character's living status (default: True).
        """
        super().__init__(first_name, is_alive)
        self.family_name = "Baratheon"
        self.eyes = "brown"
        self.hairs = "dark"

    def __str__(self):
        """String representation of the character."""
        return f"Vector: ('{self.family_name}', '{self.eyes}', '{self.hairs}')"

    def __repr__(self):
        """Official representation of the character."""
        return self.__str__()

    def die(self):
        """Set the character's living status to False."""
        self.is_alive = False


class Lannister(Character):
    """Representing the Lannister family."""

    def __init__(self, first_name: str, is_alive: bool = True):
        """Initialize a Lannister character with specific traits.

        Args:
            first_name (str): The character's first name.
            is_alive (bool): The character's living status (default: True).
        """
        super().__init__(first_name, is_alive)
        self.family_name = "Lannister"
        self.eyes = "blue"
        self.hairs = "light"

    def __str__(self):
        """String representation of the character."""
        return f"Vector: ('{self.family_name}', '{self.eyes}', '{self.hairs}')"

    def __repr__(self):
        """Official representation of the character."""
        return self.__str__()

    @classmethod
    def create_lannister(cls, first_name: str, is_alive: bool = True):
        """Class method to create a Lannister character.

        Args:
            first_name (str): The character's first name.
            is_alive (bool): The character's living status (default: True).

        Returns:
            Lannister: A new instance of the Lannister class.
        """
        return cls(first_name, is_alive)

    def die(self):
        """Set the character's living status to False."""
        self.is_alive = False
