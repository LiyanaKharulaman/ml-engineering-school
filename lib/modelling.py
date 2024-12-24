from typing import Any

import pandas as pd
from lightgbm import LGBMClassifier
from loguru import logger
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder


def init_preprocessor(df: pd.DataFrame) -> ColumnTransformer:
    """Initialize a preprocessor for the given DataFrame.

    This function creates a ColumnTransformer object that applies OneHotEncoder to all categories columns
    and leaves the other columns unchanged.

    Args:
        df (pd.DataFrame): The input DataFrame

    Returns:
        ColumnTransformer: A preprocessor that applies OneHotEncoder to categorical columns.
    """
    categorical_columns = df.select_dtypes(include=["object"]).columns.tolist()
    preprocessor = ColumnTransformer(
        transformers=[("cat", OneHotEncoder(handle_unknown="ignore"), categorical_columns)],
        remainder="passthrough",
    )
    logger.info("Successfully initialized preprocessor with categorical columns: {}", categorical_columns)
    return preprocessor


def init_pipeline(df: pd.DataFrame, lgbm_params: dict[str, Any] = None) -> Pipeline:
    """Initialize a machine learning pipeline with preprocessing and model.

    This function creates a pipeline that first applies preprocessing to the input
    DataFrame and then fits a LightGBM classifier with the given parameters.

    Args:
        df (pd.DataFrame): The input DataFrame.
        lgbm_params (dict | None): Parameters for LightGBM classifier. Defaults to None.

    Returns:
        Pipeline: A scikit-learn Pipeline object with preprocessing and model steps.
    """
    if lgbm_params is None:
        lgbm_params = {}
    preprocessor = init_preprocessor(df)
    model = LGBMClassifier(**lgbm_params)
    pipeline = Pipeline(steps=[("preprocessor", preprocessor), ("model", model)])
    logger.info("Pipeline successfully initialized with lgbm_params: {}", lgbm_params)
    return pipeline


def train_pipeline(
    x_train: pd.DataFrame,
    y_train: pd.DataFrame,
    model_objectives: str,
    verbose: int,
    n_estimators: int,
    learning_rate: float,
    max_depth: int,
    random_state: int,
) -> Pipeline:
    """Train a machine learning pipeline with preprocessing and a LightGBM classifier.

    This function takes the training data along with LightGBM parameters,
    initializes a pipeline with preprocessing, and fits a LightGBM classifier to the training data.

    Args:
        x_train (pd.DataFrame): The training input samples.
        y_train (pd.DataFrame): The target values (class labels) as a DataFrame.
        model_objectives (str): The objective function of LightGBM model.
        verbose (int): The verbosity for LightGBM model training.
        n_estimators (int): The number of boosted trees to fit.
        learning_rate (float): The boosting learning rate.
        max_depth (int): The maximum tree depth.
        random_state (int): The seed of the pseudo random number generator to use when shuffling the data.

    Returns:
        Pipeline: A scikit-learn Pipeline object that hs been fitted to the training data.
    """
    logger.info("Starting to train pipeline with LightGBM classifier.")
    lgbm_params = {
        "objective": model_objectives,
        "verbose": verbose,
        "n_estimators": n_estimators,
        "learning_rate": learning_rate,
        "max_depth": max_depth,
        "random_state": random_state,
    }
    pipeline = init_pipeline(x_train, lgbm_params)
    pipeline.fit(x_train, y_train)
    logger.info("Pipeline succesfully trained.")
    return pipeline
