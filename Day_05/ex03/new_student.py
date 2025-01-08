import random
import string
from dataclasses import dataclass, field


def generate_id() -> str:
    """
    Génère un ID aléatoire de 15 caractères (lettres minuscules).
    """
    return "".join(random.choices(string.ascii_lowercase, k=15))


@dataclass
class Student:
    name: str
    surname: str
    active: bool = True  # Champ initialisable avec une valeur par défaut
    login: str = field(init=False)  # Champ calculé, exclu de l'initialisation
    id: str = field(init=False)     # Champ calculé, exclu de l'initialisation

    def __post_init__(self):
        """
        Méthode spéciale exécutée après l'initialisation
        automatique de la dataclass.
        Utilisée pour calculer les champs non initialisables.
        """
        self.login = f"{self.name[0].upper()}{self.surname}"  # Login généré
        self.id = generate_id()  # ID aléatoire généré
