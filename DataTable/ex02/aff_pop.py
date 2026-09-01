from matplotlib.ticker import FuncFormatter, MultipleLocator
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
        fr = df[df["country"] == "France"]
        print("MA Raw filter data: > ")
        print(ma)
        print("FR Raw filter data: > ")
        print(fr)
        ma = ma.drop(columns="country")
        ma = ma.loc[:, "1800":"2050"]
        fr = fr.drop(columns="country")
        fr = fr.loc[:, "1800":"2050"]
        # //years
        ma_years = ma.squeeze().index.astype(int)
        fr_years = fr.squeeze().index.astype(int)
        # population ma
        ma_population = ma.squeeze().str.replace("M", "").astype(float) * 1e6
        ma_population = ma_population.values
        # population fr
        fr_population = fr.squeeze().str.replace("M", "").astype(float) * 1e6
        fr_population = fr_population.values

        # Create the plot
        fig, ax = plt.subplots()
        ax.plot(ma_years, ma_population, label="Morocco")
        ax.plot(fr_years, fr_population, label="France")
        ax.yaxis.set_major_formatter(FuncFormatter(lambda v,
                                                   pos: f"{v/1e6:g}M"))
        ax.xaxis.set_major_locator(MultipleLocator(40))
        ax.yaxis.set_major_locator(MultipleLocator(20 * 1e6))
        ax.set_title("Population Projections")
        ax.set_xlabel("Year")
        ax.set_ylabel("Population")
        ax.legend(loc="lower right")
        plt.show()

    except Exception as e:
        print(f"An error occurred: {e}")


def main():
    """
    Main function to load a CSV file and plot the life expectancy data.
    """
    path = "population_total.csv"
    aff_life(path)


if __name__ == "__main__":
    main()
