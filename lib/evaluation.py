import pandas as pd
from loguru import logger
from sklearn.metrics import accuracy_score, f1_score, precision_score, recall_score


def calculate_metrics(y_pred: pd.DataFrame, y_test: pd.DataFrame) -> dict:
    """Calculate evaluation metrics for the given predictions and true labels.

    Args:
        y_pred (pd.DataFrame): Predicted labels.
        y_test (pd.DataFrame): True labels.

    Returns:
        dict: A dictionary containing accuracy, precision, recall, and f1 score.
    """
    metrics = {
        "accuracy": accuracy_score(y_test, y_pred),
        "precision": precision_score(y_test, y_pred),
        "recall": recall_score(y_test, y_pred),
        "f1": f1_score(y_test, y_pred),
    }
    logger.info("Successfully calculated metrics.")
    return metrics
