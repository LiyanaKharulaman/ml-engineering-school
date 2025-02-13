import os

import yaml

from lib.validate_config import ConfigFile, ModelCardsConfig


def load_config(path: str) -> dict:
    """Load a config file as a dict."""
    with open(path, "r") as config_file:
        config = yaml.safe_load(config_file)
    base_name = os.path.basename(path)
    if base_name == "model_cards.yaml":
        ModelCardsConfig.model_validate(config)
    elif base_name in ["dev.yaml", "prd.yaml"]:
        ConfigFile.model_validate(config)
    return config


def extract_columns_to_drop(config: dict) -> tuple:
    """Extract columns to drop from a config dict."""
    columns_to_drop = config["columns_to_drop"]
    columns_to_drop = ";".join(columns_to_drop)
    config.pop("columns_to_drop", None)
    return columns_to_drop, config
