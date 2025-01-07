from S1E7 import Baratheon, Lannister


class King(Baratheon, Lannister):
    """Representing the King who inherits from both Baratheon and Lannister."""

    def __init__(self, first_name: str, is_alive: bool = True):
        """Initialize the King with attributes from both Baratheon
                                                    and Lannister.

        Args:
            first_name (str): The king's first name.
            is_alive (bool): The king's living status (default: True).
        """
        # Explicitly initialize Baratheon to resolve inheritance conflicts
        Baratheon.__init__(self, first_name, is_alive)

        # Default physical characteristics (from Baratheon by default)
        self.eyes = "brown"
        self.hairs = "dark"

    def get_eyes(self):
        """Get the color of the king's eyes."""
        return self.eyes

    def set_eyes(self, color: str):
        """Set the color of the king's eyes.

        Args:
            color (str): New color for the eyes.
        """
        self.eyes = color

    def get_hairs(self):
        """Get the color of the king's hair."""
        return self.hairs

    def set_hairs(self, color: str):
        """Set the color of the king's hair.

        Args:
            color (str): New color for the hair.
        """
        self.hairs = color
