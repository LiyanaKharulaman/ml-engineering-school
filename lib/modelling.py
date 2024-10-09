import pandas as pd
from lightgbm import LGBMClassifier
from loguru import logger
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder


def init_preprocessor(df: pd.DataFrame) -> ColumnTransformer:
    """Initialize a preprocessor for the given DataFrame.

    This function creates a ColumnTransformer that applies OneHotEncoder to all categorical columns
    and leaves the other columns unchanged.

    Args:
        df (pd.DataFrame): The input DataFrame.

    Returns:
        ColumnTransformer: A preprocessor that applies OneHotEncoder to categorical columns.
    """
    categorical_columns = df.select_dtypes(include=["object"]).columns.tolist()
    preprocessor = ColumnTransformer(
        transformers=[("cat", OneHotEncoder(handle_unknown="ignore"), categorical_columns)], remainder="passthrough"
    )
    logger.info("Successfully initialized preprocessor with categorical columns: {}", categorical_columns)
    return preprocessor


def init_pipeline(df: pd.DataFrame, lgbm_params: dict | None = None) -> Pipeline:
    """Initialize a machine learning pipeline with preprocessing and model.

    This function creates a pipeline that first applies preprocessing to the input DataFrame
    and then fits a LightGBM classifier with the given parameters.

    Args:
        df (pd.DataFrame): The input DataFrame.
        lgbm_params (dict | None): Parameters for the LightGBM classifier. Defaults to None.

    Returns:
        Pipeline: A scikit-learn Pipeline object with preprocessing and model steps.
    """
    if lgbm_params is None:
        logger.warning("lgbm_params is None, using default parameters.")
        lgbm_params = {}
    preprocessor = init_preprocessor(df)
    model = LGBMClassifier(objective="binary", verbose=-1, **lgbm_params)
    pipeline = Pipeline(steps=[("preprocessor", preprocessor), ("model", model)])
    logger.info("Pipeline successfully initialized with lgbm_params: {}", lgbm_params)
    return pipeline


def train_pipeline(x_train: pd.DataFrame, y_train: pd.DataFrame, lgbm_params: dict | None = None) -> Pipeline:
    """Train a machine learning pipeline with preprocessing and model.

    This function initializes a pipeline with preprocessing and a LightGBM classifier,
    then fits the pipeline to the training data.

    Args:
        x_train (pd.DataFrame): The training input samples.
        y_train (pd.DataFrame): The target values (class labels) as a DataFrame.
        lgbm_params (dict | None): Parameters for the LightGBM classifier. Defaults to None.

    Returns:
        Pipeline: A scikit-learn Pipeline object that has been fitted to the training data.
    """
    logger.info("Starting to train pipeline with LightGBM classifier.")
    pipeline = init_pipeline(x_train, lgbm_params)
    pipeline.fit(x_train, y_train)
    logger.info("Pipeline successfully trained.")
    return pipeline
