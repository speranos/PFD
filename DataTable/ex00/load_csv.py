import pandas as pd
import numpy as np


def load(path: str) -> pd.DataFrame | None:
    """
    Load a CSV file into a numpy array.

    Args:
        path (str): The path to the CSV file.

    Returns:
        A pandas DataFrame containing the data from the CSV file,
        or None if the file is not found.
    """
    try:
        df = pd.read_csv(path)
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
    print(load(path))


if __name__ == "__main__":
    main()
