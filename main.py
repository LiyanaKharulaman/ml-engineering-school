import argparse
from datetime import datetime

import mlflow
from loguru import logger
from mlflow.models.signature import infer_signature

from lib.data_loading import read_data
from lib.evaluation import calculate_metrics
from lib.modelling import train_pipeline
from lib.preprocessing import preprocess_data, split_data


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


def training_pipeline(  # noqa: D103
    data_path: str,
    lgbm_params: dict,
    experiment_name: str,
    run_name: str,
) -> None:
    mlflow.set_experiment(experiment_name)

    with mlflow.start_run(
        description="Training pipeline of a LightGBM model for binary classification", run_name=run_name
    ):
        mlflow.set_tag("model_type", "LightGBM")
        mlflow.set_tag("data_version", "v1")

        logger.info(f"Data path: {data_path}")
        logger.info(f"LGBM params: {lgbm_params}")
        mlflow.log_param("data_path", data_path)
        mlflow.log_param("lgbm_params", lgbm_params)

        data = read_data(data_path)
        mlflow.log_metric("dataset_size", len(data))

        x, y = preprocess_data(data)
        mlflow.log_metric("num_features", x.shape[1])

        x_train, x_test, y_train, y_test = split_data(x, y)
        mlflow.log_metric("train_size", len(x_train))
        mlflow.log_metric("test_size", len(x_test))

        pipeline = train_pipeline(x_train, y_train, lgbm_params)
        y_pred = pipeline.predict(x_test)
        logger.info("Successfully calculated predictions")
        metrics = calculate_metrics(y_pred, y_test)
        logger.info("\n\t".join([f"{k}: {v}" for k, v in metrics.items()]))
        for k, v in metrics.items():
            mlflow.log_metric(k, v)

        signature = infer_signature(x_test, y_pred)
        mlflow.lightgbm.log_model(pipeline, "lightgbm_model", signature=signature)


if __name__ == "__main__":
    params = parse_args()
    data_path = params.get("data_path")
    lgbm_params = {k: v for k, v in params.items() if k != "data_path"}
    training_pipeline(data_path, lgbm_params, params.get("experiment_name"), params.get("run_name"))
