import pandas as pd
from pandas import DataFrame


def load(path: str) -> DataFrame:
    try:
        pd.options.display.max_rows = 1
        data = pd.read_csv(path, index_col='country')
        print(f"Loading dataset of dimensions {data.shape}")
        return data
    except Exception as e:
        print(e)
    return None
