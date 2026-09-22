class calculator:
    """A simple calculator class that performs arithmetic operations on a list of values"""
    def __init__(self, values: list) -> None:
        """Initialize the calculator with a list of values"""
        self.values = values

    def __add__(self, object) -> None:
        """Add a number to each value in the calculator"""
        self.values = [x + object for x in self.values]
        print(self.values)

    def __mul__(self, object) -> None:
        """Multiply each value in the calculator by a number"""
        self.values = [x * object for x in self.values]
        print(self.values)

    def __sub__(self, object) -> None:
        """Subtract a number from each value in the calculator"""
        self.values = [x - object for x in self.values]
        print(self.values)

    def __truediv__(self, object) -> None:
        """Divide each value in the calculator by a number"""
        if object == 0:
            print("Error: Division by zero is not allowed.")
            return None
        self.values = [x / object for x in self.values]
        print(self.values)


def main():
    v1 = calculator([0.0, 1.0, 2.0, 3.0, 4.0, 5.0])
    v1 + 5
    print("---")
    v2 = calculator([0.0, 1.0, 2.0, 3.0, 4.0, 5.0])
    v2 * 5
    print("---")
    v3 = calculator([10.0, 15.0, 20.0])
    v3 - 5
    v3/5


if __name__ == "__main__":
    main()
