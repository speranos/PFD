from typing import Any


def ft_statistics(*args: Any, **kwargs: Any) -> None:
    """Calculates the statistics of a list of numbers."""
    print("The numbers are:", len(args))
    if (len(args) == 0 or len(kwargs) == 0):
        print("ERROR")
        return
    for key, value in kwargs.items():
        print(f"{key}: {value}")


def main():
    ft_statistics(test="dd")
    # ft_statistics(1, 42, 360, 11, 64, toto="mean", tutu="median", tata="quartile")
    # print("-----")
    # ft_statistics(5, 75, 450, 18, 597, 27474, 48575, hello="std", world="var")
    # print("-----")
    # ft_statistics(5, 75, 450, 18, 597, 27474, 48575, ejfhhe="heheh", ejdjdejn="kdekem")
    # print("-----")
    # ft_statistics(toto="mean", tutu="median", tata="quartile")


if __name__ == "__main__":
    main()
