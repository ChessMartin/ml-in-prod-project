from zenml import step

import pandas as pd


@step
def load_data(path: str) -> pd.DataFrame:
    return pd.read_csv(path)
