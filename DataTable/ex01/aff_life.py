import matplotlib.pyplot as plt
from load_csv import load


def aff_life(path: str) -> None:
    """
    Load a CSV file and plot the life expectancy data.

    Args:
        path (str): The path to the CSV file.
    """
    try:
        df = load(path)
        ma = df[df["country"] == "Morocco"]
        print("Raw filter data: > ")
        print(ma)
        ma = ma.drop(columns="country")
        years = ma.squeeze().index.astype(int)
        ages = ma.squeeze().values.astype(float)

        fig, ax = plt.subplots()
        ax.plot(years, ages)
        plt.title("Morocco Life Expectancy Projections")
        plt.xlabel("Year")
        plt.ylabel("Life Expectancy")
        plt.show()
        # ages = ma.values.astype(float)
        # print(ages)
        # print(years)

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
