import pandas as pd
from lightgbm import LGBMClassifier
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder


def init_preprocessor(df: pd.DataFrame) -> ColumnTransformer:  # noqa: D103
    categorical_columns = df.select_dtypes(include=["object"]).columns.tolist()
    preprocessor = ColumnTransformer(
        transformers=[("cat", OneHotEncoder(handle_unknown="ignore"), categorical_columns)], remainder="passthrough"
    )
    return preprocessor


def init_pipeline(df: pd.DataFrame, lgbm_params: dict | None = None) -> Pipeline:  # noqa: D103
    if lgbm_params is None:
        lgbm_params = {}
    preprocessor = init_preprocessor(df)
    model = LGBMClassifier(objective="binary", **lgbm_params)
    pipeline = Pipeline(steps=[("preprocessor", preprocessor), ("model", model)])
    return pipeline


def train_pipeline(x_train: pd.DataFrame, y_train: pd.DataFrame, lgbm_params: dict | None = None) -> Pipeline:  # noqa: D103
    pipeline = init_pipeline(x_train, lgbm_params)
    pipeline.fit(x_train, y_train)
    return pipeline
