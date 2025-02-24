from load_csv import load
import matplotlib.pyplot as plt
import matplotlib.ticker as mtick
import pandas as pd


def projection_life():
    """load file and plot life expectancy data
    """
    life_df = load("../life_expectancy_years.csv")
    gdp_df = load(
        "../income_per_person_gdppercapita_ppp_inflation_adjusted.csv"
    )
    year = "1900"

    gdp = gdp_df.loc[:, year] \
        .replace({"k": "*1e3"}, regex=True) \
        .map(pd.eval) \
        .astype(int)
    life_expectancy = life_df.loc[:, year]

    result = pd.concat([gdp, life_expectancy], axis=1, join='inner')
    result.columns = ['GDP', 'Life expectancy']

    result.plot(x='GDP', y='Life expectancy', kind='scatter', )

    plt.title(f'{year}')
    plt.ylabel('Life expectancy')
    plt.xlabel('Gross domestic product')

    formatter = mtick.FuncFormatter(lambda x, pos: f'{x/1e3:.0f}K')
    plt.gca().xaxis.set_major_formatter(formatter)

    plt.savefig("result.png")


def main():
    projection_life()


if __name__ == '__main__':
    main()
