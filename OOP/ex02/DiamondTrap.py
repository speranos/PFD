from S1E7 import Baratheon, Lannister


class King(Baratheon, Lannister):
    """Representing a King character"""
    def __init__(self, first_name, is_alive=True):
        super().__init__(first_name, is_alive)

    def set_eyes(self, eyes):
        """Set the eye color of the King"""
        self._eyes = eyes

    def get_eyes(self):
        """Get the eye color of the King"""
        return self._eyes

    def set_hairs(self, hairs):
        """Set the hair color of the King"""
        self._hairs = hairs

    def get_hairs(self):
        """Get the hair color of the King"""
        return self._hairs

    hairs = property(get_hairs, set_hairs)
    eyes = property(get_eyes, set_eyes)


def main() -> None:
    """Main function to demonstrate the King class"""
    Joffrey = King("Joffrey")
    print(Joffrey.__dict__)
    Joffrey.set_eyes("blue")
    Joffrey.set_hairs("light")
    print(Joffrey.get_eyes())
    print(Joffrey.get_hairs())
    print(Joffrey.__dict__)


if __name__ == "__main__":
    main()
