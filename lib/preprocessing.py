import pandas as pd
from sklearn.model_selection import train_test_split


def create_target(df: pd.DataFrame) -> pd.DataFrame:  # noqa: D103
    if "Numtppd" not in df.columns:
        raise KeyError("Column 'Numtppd' not found in DataFrame")
    df["target"] = df["Numtppd"].apply(lambda x: 1 if x != 0 else 0)
    return df


def drop_cols(df: pd.DataFrame) -> tuple:  # noqa: D103
    required_columns = ["Numtppd", "Numtpbi", "Indtppd", "Indtpbi", "target"]
    if not all(column in df.columns for column in required_columns):
        raise KeyError(f"DataFrame must contain the following columns: {required_columns}")
    x = df.drop(columns=required_columns)
    y = df["target"]
    return x, y


def preprocess_data(df: pd.DataFrame) -> tuple:  # noqa: D103
    df = create_target(df)
    x, y = drop_cols(df)
    return x, y


def split_data(x: pd.DataFrame, y: pd.DataFrame) -> pd.DataFrame:  # noqa: D103
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)
    return x_train, x_test, y_train, y_test
