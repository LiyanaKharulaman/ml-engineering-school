from typing import List

import yaml
from loguru import logger
from pydantic import BaseModel as PydanticBaseModel


class BaseModel(PydanticBaseModel):
    """Base model for all models"""

    class Config:
        """Pydantic configuration"""

        arbitrary_types_allowed = True  # allow any type to be used
        extra = "forbid"  # ensure no extra fields are allowed
        protected_namespaces = ()  # ensure "model*" params can be used


class MLConfigTraining(BaseModel):
    """Model configuration for training"""

    random_state: int
    columns_to_drop: List[str]
    target_col_name: str
    train_size: float
    model_objective: str
    verbose: int
    model_name: str
    model_stage: str
    n_estimators: int
    learning_rate: float
    max_depth: int
    sensitive_feature: str


class MLConfigInference(BaseModel):
    """Model configuration for inference"""

    model_name: str
    model_stage: str


class TrainingConfig(BaseModel):
    """Training configuration"""

    cronjob: str
    timezone: str
    scheduler_name: str
    data_path_var: str
    default_compute: str
    experiment_name: str
    tags: dict
    ml_config: MLConfigTraining


class InferenceConfig(BaseModel):
    """Inference configuration"""

    cronjob: str
    timezone: str
    scheduler_name: str
    data_path_var: str
    default_compute: str
    experiment_name: str
    tags: dict
    ml_config: MLConfigInference


class ConfigFile(BaseModel):
    """Config file"""

    training_config: TrainingConfig
    inference_config: InferenceConfig


class BusinessDetails(BaseModel):
    """Business details"""

    business_problem: str
    business_domain: str
    business_stakeholders: str
    business_kpis: List[str]
    business_owners: List[str]


class IntendedUses(BaseModel):
    """Intended uses"""

    purpose_of_model: str
    model_benefits: str
    intended_uses: str
    factors_affecting_model_efficiency: str
    limits: str
    risk_level: str
    model_output: str


class ModelCardsConfig(BaseModel):
    """Model cards configuration"""

    business_details: BusinessDetails
    intended_uses: IntendedUses


def validate_configurations() -> ConfigFile:
    """Validate the config file"""
    with open("./config/dev.yaml", "r") as file:
        config = yaml.safe_load(file)

    ConfigFile.model_validate(config)
    logger.info("Config file dev.yaml has been validated")

    with open("./config/model_cards.yaml", "r") as file:
        config = yaml.safe_load(file)

    ModelCardsConfig.model_validate(config)
    logger.info("Config file model_cards.yaml has been validated")


if __name__ == "_main_":
    validate_configurations()
