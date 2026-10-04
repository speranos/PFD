import numpy as np


def slice_me(family: list, start: int, end: int) -> list:
    """
    Slices the input 2D list (family) from start to end.
    """
    if type(family) is not list:
        raise ValueError('Type is not list!')
    if ((start <= end) and (start != 0)) or (end > len(family)):
        if start <= end:
            print("s <= e")
        else:
            print("e > len")
        raise ValueError('Index out of range!')
    arr = np.array(family)
    print("My shape is : ", arr.shape)
    sliced = arr[start:end]
    print("My new shape is : ", sliced.shape)
    return sliced.tolist()


def main():
    try:
        family = [[1.80, 78.4],
                  [2.15, 102.7],
                  [2.10, 98.5],
                  [1.88, 75.2]]
        print(slice_me(family, 0, 2))
        print(slice_me(family, 1, -2))
    except ValueError as e:
        print(f"Error: {e}")
        return []


if __name__ == "__main__":
    main()
