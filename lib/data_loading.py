import pandas as pd


def download_data() -> None:  # noqa: D103
    # TODO add code to download data from Azure blob storage into data folder
    pass


def read_data(path: str) -> pd.DataFrame:  # noqa: D103
    df = pd.read_csv(path)
    return df
