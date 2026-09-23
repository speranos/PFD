class calculator:
    """A simple calculator class."""
    @staticmethod
    def dotproduct(V1: list[float], V2: list[float]) -> None:
        """Calculates the dot product of two vectors."""
        print("Dot product is:", sum(x * y for x, y in zip(V1, V2)))

    @staticmethod
    def add_vec(V1: list[float], V2: list[float]) -> None:
        """Calculates the element-wise sum of two vectors."""
        v3: list[float] = [float(x + y) for x, y in zip(V1, V2)]
        print("Add Vector is:", v3)

    @staticmethod
    def sous_vec(V1: list[float], V2: list[float]) -> None:
        """Calculates the element-wise difference of two vectors."""
        v3: list[float] = [float(x - y) for x, y in zip(V1, V2)]
        print("Sous Vector is:", v3)


def main():
    a = [5, 10, 2]
    b = [2, 4, 3]
    calculator.dotproduct(a, b)
    calculator.add_vec(a, b)
    calculator.sous_vec(a, b)


if __name__ == "__main__":
    main()
