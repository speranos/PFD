import pandas as pd
import numpy as np


def load(path: str) -> np.ndarray:
    """
    Load a CSV file into a numpy array.

    Args:
        path (str): The path to the CSV file.

    Returns:
        np.ndarray: A numpy array containing the data from the CSV file.
    """
    try:
        df: np.ndarray = pd.read_csv(path).to_numpy()
        print("Loading dataset of dimensions ", df.shape)
        return df
    except FileNotFoundError:
        print("File not found.")
        return None


def main():
    """
    Main function to load a CSV file and print its contents.
    """
    path = "life_expectancy_years.csv"
    data = load(path)
    if data is not None:
        print("Data: ", data)
    else:
        print("Failed to load data.")


if __name__ == "__main__":
    main()
