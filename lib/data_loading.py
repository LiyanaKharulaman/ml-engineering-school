import pandas as pd
from loguru import logger


def download_data() -> None:  # noqa: D103
    # TODO add code to download data from Azure blob storage into data folder
    pass


def read_data(path: str) -> pd.DataFrame:  # noqa: D103
    """Read data from a CSV file into a DataFrame.

    Args:
        path (str): The file path to the CSV file.

    Returns:
        pd.DataFrame: The DataFrame containing the data from the CSV file.
    """
    df = pd.read_csv("dataset/pg15training.csv")
    logger.info("Successfully read data.")
    logger.info(f"Dataframe contains {df.shape[0]} rows and {df.shape[1]} columns.")
    return df
