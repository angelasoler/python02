from load_csv import load
import matplotlib.pyplot as plt


def aff_life():
    """load file and plot life expectancy data
    """
    df = load("../life_expectancy_years.csv")
    if df is None:
        return
    country = "Brazil"
    br_data = df.loc[country]
    br_data.plot()
    plt.title(f'{country} Life expectancy Projections')
    plt.ylabel('Life expectancy')
    plt.xlabel('Year')
    plt.savefig("result.png")


def main():
    aff_life()


if __name__ == '__main__':
    main()
