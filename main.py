import argparse

from loguru import logger

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

    args = parser.parse_args()

    params = vars(args)
    logger.info("\n\t".join([f"{k}: {v}" for k, v in params.items()]))
    return params


def main(data_path: str, lgbm_params: dict) -> None:  # noqa: D103
    logger.info(f"Data path: {data_path}")
    logger.info(f"LGBM params: {lgbm_params}")
    data = read_data(data_path)
    x, y = preprocess_data(data)
    x_train, x_test, y_train, y_test = split_data(x, y)
    pipeline = train_pipeline(x_train, y_train, lgbm_params)
    y_pred = pipeline.predict(x_test)
    logger.info("Successfully calculated predictions")
    metrics = calculate_metrics(y_pred, y_test)
    logger.info("\n\t".join([f"{k}: {v}" for k, v in metrics.items()]))


if __name__ == "__main__":
    params = parse_args()
    data_path = params.get("data_path")
    lgbm_params = {k: v for k, v in params.items() if k != "data_path"}
    main(data_path, lgbm_params)
