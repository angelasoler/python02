import pandas as pd
from pandas import DataFrame


def load(path: str) -> DataFrame:
    """load csv file and return DataFrame

    Args:
        path (str)

    Returns:
        DataFrame or None on fail
    """
    if path.endswith(".csv") is False:
        print("Most be .csv file extension!")
        return None
    try:
        pd.options.display.max_rows = 1
        data = pd.read_csv(path, index_col='country')
        print(f"Loading dataset of dimensions {data.shape}")
        return data
    except Exception as e:
        print(e)
    return None
