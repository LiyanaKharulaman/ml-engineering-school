import argparse
from datetime import datetime

import fire
import mlflow
from loguru import logger
from mlflow.models.signature import infer_signature

from lib.data_loading import read_data
from lib.data_preprocessing import preprocess_data, split_data
from lib.data_schema import validate_schemas
from lib.model_card import create_model_card
from lib.model_evaluation import (
    calculate_metrics,
    check_is_model_better,
    run_bias_detector,
    run_explainer,
    train_mitigator,
)
from lib.modelling import train_pipeline
from lib.utils import load_config


def parse_args() -> dict:  # noqa: D103
    parser = argparse.ArgumentParser(description="Greet a person based on their name and age.")

    parser.add_argument("--data-path", type=str, required=True, help="The path of data to use.")
    parser.add_argument("--n-estimators", type=int, required=True, help="The number of boosted trees to fit.")
    parser.add_argument("--learning-rate", type=float, required=True, help="The boosting learning rate")
    parser.add_argument("--max-depth", type=int, required=False, default=10, help="The maximum tree depth")
    parser.add_argument(
        "--experiment-name", type=str, required=False, default="axa-mleng-mlflow", help="The mlflow experiment name"
    )
    parser.add_argument(
        "--run-name",
        type=str,
        required=False,
        default="run" + str(datetime.now().timestamp()),
        help="The mlflow run name",
    )

    args = parser.parse_args()

    params = vars(args)
    logger.info("\n\t".join([f"{k}: {v}" for k, v in params.items()]))
    return params


def training_pipeline(
    data_path: str,
    n_estimators: int,
    learning_rate: float,
    max_depth: int,
    experiment_name: str,
    run_name: str,
    columns_to_drop: list,
    target_col_name: str,
    train_size: float,
    random_state: int,
    model_objective: str,
    verbose: int,
    model_name: str,
    model_stage: str,
    model_card_config: dict,
    sensitive_feature: str,
) -> None:
    """Run the training pipeline on the provided data path."""
    mlflow.set_experiment(experiment_name)

    with mlflow.start_run(
        description="Training pipeline of LightGBM model for binary classification", run_name=run_name
    ) as run:
        mlflow.set_tag("model_type", "LightGBM")
        mlflow.set_tag("data_version", "v1")

        logger.info(f"Data path: {data_path}")
        logger.info(f"Number of estimatos: {n_estimators}")
        logger.info(f"Learning rate: {learning_rate}")
        logger.info(f"Max depth: {max_depth}")

        mlflow.log_param("data_path", data_path)
        mlflow.log_param("n_estimators", n_estimators)
        mlflow.log_param("learning_rate", learning_rate)
        mlflow.log_param("max_depth", max_depth)

        # read data
        data = read_data(data_path)
        # data = data[:100]
        mlflow.log_metric("dataset_size", len(data))

        # data preprocessing
        x, y = preprocess_data(data, columns_to_drop, target_col_name)
        mlflow.log_metric("num_features", x.shape[1])

        validated_x, validated_y = validate_schemas(x, y)

        # model training
        x_train, x_test, y_train, y_test = split_data(validated_x, validated_y, train_size, random_state)
        mlflow.log_metric("train_size", len(x_train))
        mlflow.log_metric("test_size", len(x_test))

        pipeline = train_pipeline(
            x_train, y_train, model_objective, verbose, n_estimators, learning_rate, max_depth, random_state
        )

        # model prediction
        y_pred = pipeline.predict(x_test)

        # model evaluation
        fairness_results = run_bias_detector(x_test, y_test, y_pred, sensitive_feature)
        mlflow.log_metric("disparity", fairness_results["disparity"])
        mlflow.log_figure(fairness_results["fairness_plot"].figure, "fairness_plot.png")

        # mitigation
        mitigator = train_mitigator(x_train, y_train, sensitive_feature)
        if fairness_results["disparity"] > 0.01:
            mitigator = train_mitigator(x_train, y_train, sensitive_feature)
            y_pred_mitigated = mitigator.predict(x_test)
            fairness_results_mitigated = run_bias_detector(x_test, y_test, y_pred_mitigated, sensitive_feature)
            mlflow.log_metric("disparity_mitigated", fairness_results_mitigated["disparity"])
            mlflow.log_figure(fairness_results_mitigated["fairness_plot"].figure, "fairness_plot_mitigated.png")

        # new trained model after mitigation
        y_pred = mitigator.predict(x_test)
        logger.info("Successfully calculated predictions")

        # model metrics
        metrics = calculate_metrics(y_pred, y_test)
        logger.info("\n\t".join([f"{k}: {v}" for k, v in metrics.items()]))
        cm_figure = metrics.pop("cm", None).figure_
        if cm_figure:
            mlflow.log_figure(cm_figure, "testing_confusion_matrix.png")
        for k, v in metrics.items():
            mlflow.log_metric(k, v)

        explanation = run_explainer(pipeline, x_test)
        mlflow.log_params({"importance_" + k: v for k, v in explanation.feature_importances.items()})
        mlflow.log_dict({"shap_values": explanation.shap_values.tolist()}, "shap_values.json")
        mlflow.log_figure(explanation.shap_summary_plot.figure, "shap_summary_plot.png")
        mlflow.log_figure(explanation.shap_force_plot, "shap_force_plot.png")
        mlflow.log_figure(explanation.feature_importances_plot, "feature_importances_plot.png")

        signature = infer_signature(x_test, y_pred)
        mlflow.lightgbm.log_model(mitigator, "lightgbm_model", signature=signature)

        # model registry
        model_uri = f"runs:/{run.info.run_id}/lightgbm_model"
        registered_model = mlflow.register_model(model_uri, model_name)
        logger.info(f"Model registered with name: {registered_model.name}, version: {registered_model.version}")

        client = mlflow.tracking.MlflowClient()
        if metrics["roc_auc"] >= 0.5 and check_is_model_better(
            model_name, model_stage, metrics["accuracy"], "accuracy"
        ):
            client.transition_model_version_stage(registered_model.name, registered_model.version, stage=model_stage)
            client.set_model_version_tag(
                name=registered_model.name, version=registered_model.version, key="validated_ROC_AUC", value=True
            )
            # create a model card
            model_card_md = create_model_card(registered_model.name, model_card_config)
            with open("./lib/model_card/model_cards/model_card_prod.md", "w") as f:
                f.write(model_card_md)
            mlflow.log_artifact("./lib/model_card/model_cards/model_card_prod.md")
        else:
            client.set_model_version_tag(
                name=registered_model.name, version=registered_model.version, key="validated_ROC_AUC", value=False
            )
            logger.info("Model did not pass validation")


def inference_pipeline(
    data_path: str,
    model_name: str,
    model_stage: str,
) -> None:
    """Run the inference pipeline on the provided data path."""
    data = read_data(data_path)

    # invoke client
    client = mlflow.tracking.MlflowClient()

    # get latest production version
    latest_production_version = client.get_latest_versions(model_name, stages=[model_stage])
    latest_production_version_sorted = sorted(latest_production_version, key=lambda mv: mv.version, reverse=True)
    logger.info(f"Loaded model: {latest_production_version_sorted[0]}")

    # load model
    model_uri = latest_production_version_sorted[0].source
    pipeline = mlflow.lightgbm.load_model(model_uri)

    logger.info("Successfully loaded pipeline")

    # make predictions
    y_pred = pipeline.predict(data)
    logger.info("Successfully predicted target on inference data")
    logger.info(f"Predictions: {y_pred.shape[0]} data points")
    logger.info(f"Predictions: {y_pred}.sum() data points")


def trigger_pipeline(config_path: str, model_cards_config_path: str, pipeline_type: str) -> None:
    """Trigger training or inference pipeline code locally."""
    config = load_config(config_path)[pipeline_type]
    if pipeline_type == "training_config":
        model_card_config = load_config(model_cards_config_path)
        training_pipeline(
            data_path="./dataset/pg15training.csv",
            experiment_name="axa-mleng-mlflow",
            run_name="run" + str(datetime.now().timestamp()),
            model_card_config=model_card_config,
            **config["ml_config"],
        )

    elif pipeline_type == "inference_config":
        inference_pipeline(data_path="./dataset/pg15inference.csv", **config["ml_config"])


if __name__ == "__main__":
    fire.Fire(trigger_pipeline)
