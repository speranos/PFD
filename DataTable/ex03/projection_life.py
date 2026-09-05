from matplotlib.ticker import FuncFormatter, NullFormatter
import matplotlib.pyplot as plt
from load_csv import load
import pandas as pd


def _k(v, pos):
    return f"{v/1000:g}k" if v >= 1000 else f"{v:g}"


def projection_life(life_ex, gdp):
    try:
        df_l = load(life_ex).set_index("country")["1900"]
        df_g = load(gdp).set_index("country")["1900"]

        df = pd.concat([df_l, df_g], axis=1, keys=["le", "gdp"])
        df = df.dropna()  # Drop rows with NaN values
        plt.scatter(df["gdp"], df["le"])
        plt.xscale("log")
        plt.xticks([300, 1000, 10000])
        plt.gca().xaxis.set_major_formatter(FuncFormatter(_k))
        plt.gca().xaxis.set_minor_formatter(NullFormatter())
        plt.xlabel("Gross domestic product")
        plt.ylabel("Life Expectancy")
        plt.title("1900")
        plt.show()
        print("DataFrame with life expectancy and GDP:")
        print(df)
    except Exception as e:
        print(f"An error occurred: {e}")


def main():
    """
    Main function to load a CSV file and plot the life expectancy data.
    """
    life_ex = "life_expectancy_years.csv"
    gdp = "income_per_person_gdppercapita_ppp_inflation_adjusted.csv"
    projection_life(life_ex, gdp)


if __name__ == "__main__":
    main()
