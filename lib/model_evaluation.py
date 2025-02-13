from dataclasses import dataclass
from typing import Any

import matplotlib.pyplot as plt
import mlflow
import numpy as np
import pandas as pd
import shap
from fairlearn.metrics import MetricFrame, count, selection_rate
from fairlearn.reductions import EqualizedOdds, ExponentiatedGradient
from loguru import logger
from shap import TreeExplainer
from shap.plots._force import AdditiveForceArrayVisualizer
from sklearn.metrics import (
    ConfusionMatrixDisplay,
    accuracy_score,
    f1_score,
    precision_score,
    recall_score,
    roc_auc_score,
)
from sklearn.pipeline import Pipeline

from lib.modelling import init_pipeline


def calculate_metrics(y_pred: pd.DataFrame, y_test: pd.DataFrame) -> dict[str, Any]:
    """Calculate evaluation metrics for the given predictions and true labels.

    Agrs:
        y_pred (pd.DataFrame): Predicted labels.
        y_test (pd.DataFrame): True Labels.

    Returns:
        dict: A dictionary containing accuracy, precision, recall, and F1 score.
    """
    metrics = {
        "accuracy": round(float(accuracy_score(y_test, y_pred)), 2),
        "precision": round(float(precision_score(y_test, y_pred)), 2),
        "recall": round(float(recall_score(y_test, y_pred)), 2),
        "f1": round(float(f1_score(y_test, y_pred)), 2),
        "roc_auc": round(float(roc_auc_score(y_test, y_pred)), 2),
        "cm": ConfusionMatrixDisplay.from_predictions(y_test, y_pred),
    }
    logger.info("Successfully calculated evaluation metrics.")
    return metrics


def calculate_feature_importances(pipeline: Pipeline) -> dict:
    """Calculate and return feature importances from the model"""
    preprocessor = pipeline.named_steps["preprocessor"]
    model = pipeline.named_steps["model"]
    feature_labels = preprocessor.get_feature_names_out()
    feature_importances = model.feature_importances_
    feature_importances_dict = dict(zip(feature_labels, feature_importances, strict=False))
    return feature_importances_dict


def plot_feature_importances(feature_importances_dict: dict, top_n: int = 100) -> plt.Figure:
    """Plot a horizontal bar chart of the top N feature importances."""
    categories = list(feature_importances_dict.keys())
    counts = list(feature_importances_dict.values())
    sorted_indices = np.argsort(counts)[::-1][:top_n]
    top_categories = [categories[i] for i in sorted_indices]
    top_counts = [counts[i] for i in sorted_indices]
    fig = plt.figure(figsize=(12, 8))
    plt.barh(top_categories[::-1], top_counts[::-1])
    plt.xlabel("Importance")
    plt.ylabel("Feature")
    plt.title("Top Feature Importances")
    plt.tight_layout()
    plt.close()
    return fig


def calculate_shap_values(pipeline: Pipeline, x_test: pd.DataFrame) -> tuple:
    """Calculate and return shap values from the model"""
    preprocessor = pipeline.named_steps["preprocessor"]
    model = pipeline.named_steps["model"]
    x_transformed = preprocessor.transform(x_test).toarray()
    explainer = shap.TreeExplainer(model)
    shap_values = explainer.shap_values(x_transformed)
    return shap_values, explainer


def plot_shap_summary_plot(
    pipeline: Pipeline, shap_values: np.ndarray, x_test: pd.DataFrame, plot_type: str
) -> plt.gcf:
    """Generate and return a SHAP summary plot"""
    preprocessor = pipeline.named_steps["preprocessor"]
    x_transformed = preprocessor.transform(x_test).toarray()
    feature_names = preprocessor.get_feature_names_out()
    plt.figure(figsize=(10, 6))
    shap.summary_plot(shap_values, x_transformed, plot_type=plot_type, feature_names=feature_names, show=False)
    summary_plot = plt.gcf()
    plt.tight_layout()
    plt.close()
    return summary_plot


def plot_force_plot(
    pipeline: Pipeline,
    explainer: TreeExplainer,
    shap_values: np.ndarray,
    x_test: pd.DataFrame,
    prediction_id: int = 0,
) -> AdditiveForceArrayVisualizer:
    """Generate and return a SHAP force plot for a single prediction"""
    preprocessor = pipeline.named_steps["preprocessor"]
    x_transformed = preprocessor.transform(x_test).toarray()
    feature_names = preprocessor.get_feature_names_out()
    shap.force_plot(
        explainer.expected_value,
        shap_values[prediction_id],
        x_transformed[prediction_id],
        feature_names=feature_names,
        matplotlib=True,
        show=False,
    )
    force_plot = plt.gcf()
    plt.close()
    return force_plot


@dataclass
class ExplainabilityResults:
    """Evaluation results dataclass."""

    feature_importances: dict
    feature_importances_plot: plt.Figure
    shap_values: np.ndarray
    shap_summary_plot: plt.Figure
    shap_force_plot: plt.Figure


def run_explainer(pipeline: Pipeline, data: pd.DataFrame) -> ExplainabilityResults:
    """Run the explainer on the given pipeline and data, returning various interpretability outputs"""
    feature_importances = calculate_feature_importances(pipeline)
    feature_importances_plot = plot_feature_importances(feature_importances, 31)
    shap_values, explainer = calculate_shap_values(pipeline, data)
    shap_summary_plot = plot_shap_summary_plot(pipeline, shap_values, data, "bar")
    shap_force_plot = plot_force_plot(pipeline, explainer, shap_values, data)
    return ExplainabilityResults(
        feature_importances=feature_importances,
        feature_importances_plot=feature_importances_plot,
        shap_values=shap_values,
        shap_summary_plot=shap_summary_plot,
        shap_force_plot=shap_force_plot,
    )


def run_bias_detector(
    x_test: pd.DataFrame, y_test: pd.DataFrame, y_test_pred: pd.DataFrame, sensitive_column: str
) -> dict:
    """Run fairness detector to evaluate model fairness.

    Args:
        x_test (pd.DataFrane): Test features.
        y_test (pd.DataFrame): True labels.
        y_test_pred (pd.DataFrame): Predicted labels.
        sensitive_column (str): Sensitive column.

    Returns:
        dict: A dictionary containing the fairness plot.
    """
    metrics = {
        "precision": precision_score,
        "accuracy": accuracy_score,
        "recall": recall_score,
        "F1 score": f1_score,
        "count": count,
        "selection_rate": selection_rate,
    }
    metric_frame = MetricFrame(
        metrics=metrics,
        y_true=y_test,
        y_pred=y_test_pred,
        sensitive_features=x_test[sensitive_column],
    )
    fig = metric_frame.by_group.plot.bar(
        subplots=True,
        layout=(3, 2),
        legend=False,
        figsize=(12, 12),
        sharey=True,
    )
    disparities = metric_frame.by_group["selection_rate"]
    disparity = disparities.max() - disparities.min()
    return {"fairness_plot": fig[0][0], "disparity": disparity}


def train_mitigator(x_train: pd.DataFrame, y_train: pd.DataFrame, sensitive_features: list) -> ExponentiatedGradient:
    """Initialize and return an ExponentiatedGraidtent mitigator with EqualizedOdds as constraints."""
    pipeline = init_pipeline(x_train)
    mitigator = ExponentiatedGradient(
        estimator=pipeline,
        constraints=EqualizedOdds(difference_bound=0.01),
        sample_weight_name="model__sample_weight",
    )
    mitigator = mitigator.fit(x_train, y_train, sensitive_features=x_train[sensitive_features])
    return mitigator


def get_model_metric(model_name: str, model_stage: str, metric: str) -> float:
    """Get metric of a production model from model registry."""
    client = mlflow.MlflowClient()
    latest_production_version = client.get_latest_versions(name=model_name, stages=[model_stage])
    if len(latest_production_version) == 0:
        return 0
    latest_production_version_sorted = sorted(
        latest_production_version, key=lambda x: x.creation_timestamp, reverse=True
    )
    model_run = client.get_run(latest_production_version_sorted[0].run_id)
    try:
        parent_run_id = model_run.data.tags["mlflow.parentRunId"]
        filter_string = f"tags.mlflow.parentRunId = '{parent_run_id}'"
        runs = mlflow.search_runs(
            experiment_ids=model_run.info.experiment_id,
            filter_string=filter_string,
        )
        metric_value = runs[runs["tags.mlflow.runName"] == "evaluate_pred_node"][f"metrics.{metric}"].iloc[0]
    except KeyError:
        metric_value = model_run.data.metrics[metric]
    return metric_value


def check_is_model_better(model_name: str, model_stage: str, current_metric: float, metric_name: str) -> bool:
    """Check if current model better from the current one in production."""
    prod_metric = get_model_metric(model_name, model_stage, metric_name)
    if current_metric >= prod_metric:
        logger.info("Current model is better than production one")
        return True
    logger.info("Production model is better than current one")
    return False
