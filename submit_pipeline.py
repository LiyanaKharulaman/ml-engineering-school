import os

import fire
from dotenv import load_dotenv
from loguru import logger

from azure.ai.ml import Input, MLClient
from azure.ai.ml.entities import (
    CronTrigger,
    JobSchedule,
)
from azure.azure_pipeline import pg15inference_pipeline, pg15training_pipeline
from azure.core.exceptions import ClientAuthenticationError
from azure.identity import DefaultAzureCredential, InteractiveBrowserCredential
from lib.utils import extract_columns_to_drop, load_config


def submit_pipeline(
    config_path: str,
    model_card_config_path: str,
    pipeline_type: str,
) -> None:
    """Submit Azure ML pipeline"""
    load_dotenv()
    pipeline_config = load_config(config_path)

    try:
        credential = DefaultAzureCredential()
        credential.get_token("https://management.azure.com/.default")
    except ClientAuthenticationError as e:
        logger.error(f"Encountered error:\n{e}, \n\nFalling back to InteractiveBrowserCredential")
        credential = InteractiveBrowserCredential()
    ml_client = MLClient.from_config(credentials=credential, path="./azure/.azureml/config.json")

    try:
        pipeline_config = pipeline_config[pipeline_type]
    except KeyError as e:
        raise KeyError(f"pipeline_type should be one of: {list(pipeline_config.keys())}") from e
    data_input = Input(type="uri_file", path=os.getenv(pipeline_config["data_input"]))
    if pipeline_type == "training":
        columns_to_drop, config = extract_columns_to_drop(pipeline_config["ml_config"])
        pipeline_job = pg15training_pipeline(
            input_data=data_input,
            columns_to_drop=columns_to_drop,
            model_cards_config_path=model_card_config_path,
            **config,
        )
    elif pipeline_type == "inference":
        pipeline_job = pg15inference_pipeline(
            input_data=data_input,
            model_name=pipeline_config["ml_config"]["model_name"],
            model_stage=pipeline_config["ml_config"]["model_stage"],
        )
    cron_trigger = CronTrigger(
        expression=pipeline_config["cronjob"],
        time_zone=pipeline_config["time_zone"],
    )
    pipeline_job.settings.default_compute = pipeline_config["default_compute"]
    pipeline_job.experiment_name = pipeline_config["experiment_name"]
    pipeline_job.tags = pipeline_config["tags"]

    job_schedule = JobSchedule(name=pipeline_config["schedule_name"], pipeline=pipeline_job, trigger=cron_trigger)
    ml_client.schedules.begin_create_or_update(schedule=job_schedule)


if __name__ == "__main__":
    fire.Fire(submit_pipeline)
