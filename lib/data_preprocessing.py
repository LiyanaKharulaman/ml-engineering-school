import pandas as pd
from loguru import logger
from sklearn.model_selection import train_test_split


def create_target(df: pd.DataFrame, target_col_name: str) -> pd.DataFrame:
    """Create a target column in the DataFrame based on 'Numtppd' column.

    This function adds a new column called 'target_col_name' to the DataFrame,
    where the value is 1 if 'Numtppd' value is not 0 and 0 if otherwise.

    Args:
        df (pd.DataFrame): The input of DataFrame.
        target_col_name (str): The name of the new target column to be added to the DataFrame.

    Returns:
        pd. DataFrame: The DataFrame with the added target column named "target_col_name".

    Raises:
        KeyError: If "Numtppd" column is not found in the DataFrame.
    """
    if "Numtppd" not in df.columns:
        logger.error("Column 'Numtppd' not found in DataFrame.")
        raise KeyError("Column 'Numtppd' not found in DataFrame")
    df[target_col_name] = df["Numtppd"].apply(lambda x: 1 if x != 0 else 0)
    logger.info("Successfully created Target Column.")
    return df


def most_common_dtype(column: pd.DataFrame) -> type:
    """Return the most common data type in a column."""
    return column.apply(type).mode()[0]


def remove_uncommon_datatype(df: pd.DataFrame) -> pd.DataFrame:
    """Remove uncommon data types from DataFrame.

    This function removes uncommon data types from the DataFrame.

    Args:
        df (pd.DataFrame): The input DataFrame.

    Returns:
        pd.DataFrame: The DataFrame with uncommon data types removed.
    """
    # Function to filter rows with inconsistent data types in the entire DataFrame
    for column in df.columns:
        common_dtype = most_common_dtype(df[column])
        df = df[df[column].apply(type) == common_dtype]
    return df


def drop_cols(df: pd.DataFrame, columns_to_drop: list, target_col_name: str) -> tuple[pd.DataFrame, pd.DataFrame]:
    """Drop specific columns from DataFrame and separate from target column.

    This function drops specific columns from DataFrame (including target column) to create an x variable.
    This function also creates a specific columns (target column) from DataFrame to create a y variable.

    Args:
        df (pd. DataFrame): The input DataFrame.
        columns_to_drop (list): The list of columns to drop, not including the target column.
        target_col_name (str): The name of the target column to separate.

    Returns:
        tuple: A tuple containing the DataFrame with the specified columns dropped (x) and the target column (y).

    Raises:
        KeyError: If the required columns or the target column are not found in the DataFrame.
    """
    columns_to_drop = [*columns_to_drop, target_col_name]
    if not all(column in df.columns for column in columns_to_drop):
        logger.error("Some of the columns {columns_to_drop} not found in DataFrame.")
        raise KeyError("DataFrame must contain the following columns: {columns_to_drop}")
    x = df.drop(columns=columns_to_drop)
    y = df[target_col_name]
    logger.info("Successfully created x (features) and y (labels) columns.")
    return x, y


def preprocess_data(df: pd.DataFrame, columns_to_drop: list, target_col_name: str) -> tuple[pd.DataFrame, pd.DataFrame]:
    """Preprocess the input DataFrame by creating a target column and dropping specific columns.

    This function creates a target column based on "Numtppd" column and drops specific columns.
    Then, this function separates the target column into a separate variable.

    Args:
        df (pd.DataFrame): The input DataFrame.
        columns_to_drop (list): The list of columns to drop, not including the target column.
        target_col_name (str): The name of the target column to separate.

    Returns:
    tuple: A tuple containing the preprocessed DataFrame without the dropped columns (x) and the target column (y).
    """
    df = create_target(df, target_col_name)
    df = remove_uncommon_datatype(df)
    logger.info("Successfully removed uncommon datatype.")
    x, y = drop_cols(df, columns_to_drop, target_col_name)
    logger.info("Successfully preprocessed data.")
    return x, y


def split_data(
    x: pd.DataFrame,
    y: pd.DataFrame,
    train_size: float,
    random_state: int,
) -> tuple[pd.DataFrame, pd.Series, pd.DataFrame, pd.Series]:
    """Split the input DataFrame into training and testing sets based on the provided ratio.

    This function splits the input features (x) and the corresponding target values (y) into training and testing sets
    according to the specified train_size and random_state parameters.

    Args:
        x (pd.DataFrame): The input features.
        y (pd.DataFrame): The target values,
        train_size (float, optional): The proportion of the dataset to include in the train split.
        random_state (int, optional): Controls the shuffling applied to the data before applying the split.

    Returns:
        tuple: A tuple containing the training features (x_train), testing features (x_test),
        training target values (y_train), and testing target values (y_test).
    """
    x_train, x_test, y_train, y_test = train_test_split(x, y, train_size=train_size, random_state=random_state)
    logger.info("Successfully separated train and test data")
    return x_train, x_test, y_train, y_test
