from S1E9 import Character


class Baratheon(Character):
    """Representing the Baratheon family"""
    def __init__(self, first_name: str, is_alive: bool = True) -> None:
        """Initialize a Baratheon character"""
        super().__init__(first_name, is_alive)
        self.family_name = "Baratheon"
        self.eyes = "brown"
        self.hairs = "dark"

    def die(self) -> None:
        """Mark the character as dead"""
        self.is_alive = False

    def __str__(self) -> str:
        """Return a string representation of the family character"""
        return f"Vector: ('Baratheon', '{self.eyes}', '{self.hairs}')"

    def __repr__(self) -> str:
        """Return a string representation of the family character"""
        return self.__str__()


class Lannister(Character):
    """Representing the Lannister family"""
    def __init__(self, first_name: str, is_alive: bool = True) -> None:
        """Initialize a Lannister character"""
        super().__init__(first_name, is_alive)
        self.family_name = "Lannister"
        self.eyes = "blue"
        self.hairs = "light"

    def die(self) -> None:
        """Mark the character as dead"""
        self.is_alive = False

    def __str__(self) -> str:
        """Return a string representation of the family character"""
        return f"Vector: ('Lannister', '{self.eyes}', '{self.hairs}')"

    def __repr__(self) -> str:
        """Return a string representation of the family character"""
        return self.__str__()

    @classmethod
    def create_lannister(cls, first_name: str, is_alive: bool = True):
        """Create a Lannister character with a default first name"""
        return cls(first_name, is_alive)
