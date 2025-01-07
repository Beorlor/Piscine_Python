from abc import ABC, abstractmethod


class Character(ABC):
    """Abstract base class for all characters in GOT S1E9."""

    def __init__(self, first_name: str, is_alive: bool = True):
        """Initialize a character with a first name and living status.

        Args:
            first_name (str): The character's first name.
            is_alive (bool): The character's living status (default: True).
        """
        self.first_name = first_name
        self.is_alive = is_alive

    @abstractmethod
    def die(self):
        pass


class Stark(Character):
    """A class representing the Stark family, inheriting from Character."""

    def __init__(self, first_name: str, is_alive: bool = True):
        """Initialize a Stark character with a first name and living status.

        Args:
            first_name (str): The character's first name.
            is_alive (bool): The character's living status (default: True).
        """
        super().__init__(first_name, is_alive)

    def die(self):
        """Set the character's living status to False."""
        self.is_alive = False
