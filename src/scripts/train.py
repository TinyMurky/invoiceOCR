"""
this script is for training
"""

import yaml
from src.logging.logger import train_logger

# from datasets import load_dataset


def load_config_yaml():
    """
    Load config from config.yaml and return dict of config.
    """
    config_path = "./src/config/config.yaml"
    try:
        with open(config_path, "r", encoding="utf-8") as config_file:
            config = yaml.safe_load(config_file)
            return config
    except FileNotFoundError:
        train_logger.exception("Error: The file %s does not exist.", config_path)
    except yaml.YAMLError as exc:
        train_logger.exception("Error parsing YAML file %s: %s", config_path, exc)
    except Exception as exc:  # ignore w0718
        train_logger.exception(
            "An unexpected error occurred while loading the config file: %s", exc
        )


# def load_training_data(path: str):
#     """
#     load training data from path
#     return loader
#     """
#     dataset = load_dataset("json", data_files="path/to/your/data.json")


def start() -> None:
    """
    start training
    """
    train_logger.info("Training started")
    app_logger.info("hi!")
    CONFIG = load_config_yaml()
