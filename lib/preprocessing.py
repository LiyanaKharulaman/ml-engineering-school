import pandas as pd
from loguru import logger
from sklearn.model_selection import train_test_split


def create_target(df: pd.DataFrame) -> pd.DataFrame:
    """Create a target column in the DataFrame based on the 'Numtppd' column.

    This function adds a new column 'target' to the DataFrame, where the value is 1 if the 'Numtppd' value is not 0,
    and 0 otherwise.

    Args:
        df (pd.DataFrame): The input DataFrame.

    Returns:
        pd.DataFrame: The DataFrame with the added 'target' column.

    Raises:
        KeyError: If the 'Numtppd' column is not found in the DataFrame.
    """
    if "Numtppd" not in df.columns:
        logger.error("Column 'Numtppd' not found in DataFrame.")
        raise KeyError("Column 'Numtppd' not found in DataFrame")
    df["target"] = df["Numtppd"].apply(lambda x: 1 if x != 0 else 0)
    logger.info("Successfully created Target column.")
    return df


def drop_cols(df: pd.DataFrame) -> tuple:
    """Drop specified columns from the DataFrame and separate the target column.

    This function checks if the required columns are present in the DataFrame, then drops these columns
    and separates the target column into a separate variable.

    Args:
        df (pd.DataFrame): The input DataFrame.

    Returns:
        tuple: A tuple containing the DataFrame with the specified columns dropped (x) and the target column (y).

    Raises:
        KeyError: If the required columns are not found in the DataFrame.
    """
    required_columns = ["Numtppd", "Numtpbi", "Indtppd", "Indtpbi", "target"]
    if not all(column in df.columns for column in required_columns):
        logger.error(f"Some of the columns {required_columns} not found in DataFrame.")
        raise KeyError(f"DataFrame must contain the following columns: {required_columns}")
    x = df.drop(columns=required_columns)
    y = df["target"]
    logger.info("Successfully created x (features) and y (labels) columns.")
    return x, y


def preprocess_data(df: pd.DataFrame) -> tuple:
    """Preprocess the input DataFrame by creating a target column and dropping specified columns.

    This function first creates a target column based on the 'Numtppd' column, then drops specified columns
    and separates the target column into a separate variable.

    Args:
        df (pd.DataFrame): The input DataFrame.

    Returns:
        tuple: A tuple containing the preprocessed DataFrame (x) and the target column (y).
    """
    df = create_target(df)
    x, y = drop_cols(df)
    logger.info("Successfully preprocessed data.")
    return x, y


def split_data(x: pd.DataFrame, y: pd.DataFrame) -> tuple:
    """Split the input DataFrame into training and testing sets.

    This function splits the input features (x) and target (y) into training and testing sets
    using an 80-20 split.

    Args:
        x (pd.DataFrame): The input features.
        y (pd.DataFrame): The target values.

    Returns:
        tuple: A tuple containing the training features (x_train), testing features (x_test),
               training target (y_train), and testing target (y_test).
    """
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)
    logger.info("Successfully seperated train and test data.")
    return x_train, x_test, y_train, y_test
