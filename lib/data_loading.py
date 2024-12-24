import pandas as pd
from loguru import logger


def download_data() -> None:
    """Download data from Azure blob storage into data folder."""
    # TODO add code to download data from Azure blob storage into data folder
    pass


def read_data(path: str) -> pd.DataFrame:
    """Read data from a CSV file into a DataFrame.

    Args:
        path (str): The file path to the CSV file.

    Returns:
        pd.DataFrame: The DataFrame containing the data from the CSV file.
    """
    df = pd.read_csv(path)
    logger.info("Successfully read data.")
    logger.info("Dataframe contains {df.shape[0]} rows and {df.shape[1]} columns")
    return df
