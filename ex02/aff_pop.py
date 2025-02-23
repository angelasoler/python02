from load_csv import load
import matplotlib.pyplot as plt
import matplotlib.ticker as mtick
import pandas as pd


def format_population(x, pos):
    """format absolute population values to human readable format

    Args:
        x (int): number
        pos (int): position, authomaticaly passed by matplotlib

    Returns:
        string: string formated
    """    
    if x >= 1e9:
        return f'{x/1e9}B'
    elif x >= 1e6:
        return f'{x/1e6:.0f}M'
    elif x >= 1e3:
        return f'{x/1e3:.0f}K'
    return f'{x}'


def aff_pop():
    """load file and plot population data
    """    
    df = load("../population_total.csv")
    my_campus = "Bahamas"
    other = "Vanuatu"
    conversions = {"k": "*1e3", "M": "*1e6", "B": "*1e9"}
    br_data = df.loc[my_campus] \
                .replace(conversions, regex=True) \
                .map(pd.eval) \
                .astype(int)
    other_data = df.loc[other] \
                   .replace(conversions, regex=True) \
                   .map(pd.eval) \
                   .astype(int)

    br_data['1800':'2050'].plot(label=my_campus)
    other_data['1800':'2050'].plot(label=other)

    # plot config
    plt.title('Population Projections')
    plt.ylabel('Population')
    plt.xlabel('Year')
    plt.legend()

    # format limit to custom
    formatter = mtick.FuncFormatter(format_population)
    plt.gca().yaxis.set_major_formatter(formatter)

    plt.savefig("result.png")


def main():
    aff_pop()


if __name__ == '__main__':
    main()
