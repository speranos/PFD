import matplotlib.pyplot as plt
from load_csv import load
import pandas as pd
import numpy as np


def aff_life(path: str) -> None:
    """
    Load a CSV file and plot the life expectancy data.

    Args:
        path (str): The path to the CSV file.
    """
    try:
        df: np.ndarray = load(path).all()
        print("Loading dataset of dimensions ", df)
        if df is not None:
            # years = df.columns[1:]
            # print("years  > = ", years)
            raw, col = np.where(df == "Morocco")
            ages = df[raw:, col:].astype(float)
            print("ages  > = ", ages)
            print("raw  > = ", raw)
            print("data loc  > = ", df[raw])
    except Exception as e:
        print(f"An error occurred: {e}")


def main():
    """
    Main function to load a CSV file and plot the life expectancy data.
    """
    path = "life_expectancy_years.csv"
    aff_life(path)


if __name__ == "__main__":
    main()
