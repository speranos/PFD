import numpy as np


#index validation : to be done
def slice_me(family: list, start: int, end: int) -> list:
    """
    Slices the input 2D list (family) from start to end.
    """
    try:
        # if start < 0 or end > len(family) or start >= end:
        #     raise ValueError("Invalid start or end indices.")
        arr = np.array(family)
        print("My shape is : ", arr.shape)
        sliced = arr[start:end]
        print("My new shape is : ", sliced.shape)
    except ValueError as e:
        print(f"Error: {e}")
        return []
    return sliced.tolist()







def main():
    family = [[1.80, 78.4],
    [2.15, 102.7],
    [2.10, 98.5],
    [1.88, 75.2]]

    print(slice_me(family, 0, 8))
if __name__ == "__main__":
    main()