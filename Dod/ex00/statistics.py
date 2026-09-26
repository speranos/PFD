from typing import Any


def ft_statistics(*args: Any, **kwargs: Any) -> None:
    """Calculates the statistics of a list of numbers."""
    # print("The numbers are:", len(args))
    if (len(kwargs) == 0):
        return
    wanted_values = ["mean", "median", "quartile", "std", "var"]
    values = [v for k, v in kwargs.items() if v in wanted_values]

    if len(args) == 0:
        for value in values:
            print("ERROR")
        return

    for arg in args:
        if not isinstance(arg, (int, float)):
            print("ERROR")
            return

    if "mean" in values:
        mean = sum(args) / len(args)
        print(f"mean: {mean}")

    if "median" in values:
        sorted_args = sorted(args)
        n = len(sorted_args)
        if n % 2 == 0:
            median = (sorted_args[n // 2 - 1] + sorted_args[n // 2]) / 2
        else:
            median = sorted_args[n // 2]
        print(f"median: {median}")

    if "quartile" in values:
        sorted_args = sorted(args)
        n = len(sorted_args)
        q1: float = float(sorted_args[n // 4])
        q3: float = float(sorted_args[3 * n // 4])
        ret: list[float] = [q1, q3]
        print("quartile: ", ret)

    if "std" in values:
        mean = sum(args) / len(args)
        variance = sum((x - mean) ** 2 for x in args) / len(args)
        std_dev = variance ** 0.5
        print(f"std: {std_dev}")

    if "var" in values:
        mean = sum(args) / len(args)
        variance = sum((x - mean) ** 2 for x in args) / len(args)
        print(f"var: {variance}")


def main():
    # ft_statistics(test="dd")
    ft_statistics(1, 42, 360, 11, 64, "test", toto="mean", tutu="median", tata="quartile")
    print("-----")
    ft_statistics(5, 75, 450, 18, 597, 27474, 48575, hello="std", world="var")
    print("-----")
    ft_statistics(5, 75, 450, 18, 597, 27474, 48575, ejfhhe="heheh", ejdjdejn="kdekem")
    print("-----")
    ft_statistics(toto="mean", tutu="median", tata="quartile")


if __name__ == "__main__":
    main()
