"""
this script is for training
"""

import os
import yaml
from datasets import load_dataset, DatasetDict, Dataset
from transformers import AutoProcessor

from src.logging.logger import train_logger


def load_config_yaml() -> dict:
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
        raise exc
    return {}


def load_training_data(config: dict) -> Dataset:
    """
    load training data from path
    return loader
    """

    training_json_path: str = config["data"]["train"]["label_json"]
    field_of_training_data: str = config["data"]["train"]["field_to_load"]

    if not training_json_path or not field_of_training_data:
        error_message = (
            "training_json_path or field_of_training_data is not set in config.yaml"
        )
        train_logger.error(error_message)
        raise ValueError(error_message)

    if os.path.exists(training_json_path):
        dataset_dict: DatasetDict = load_dataset(
            "json", data_files=training_json_path, field=field_of_training_data
        )  # type: ignore
        return dataset_dict["train"]

    error_message = f"train file do not exist at : {training_json_path}"
    train_logger.error(error_message)
    raise FileNotFoundError(error_message)


def get_label_from_training_data(dataset: Dataset) -> list:
    """
    to collect all label from training data

    the shape of XFUND dataset is like array of:
    {
        "id": "zh_train_0",
        "uid": "640a0301a1cb24331748b579405502b44d6791883b25ea0eafc8a68126ccdadd",
        "document": [
            "box": [104, 114, 530, 175],
            "text": "滙豐晉信",
            "label": "other",
            "words": [
                {"box": [110, 117, 152, 175], "text": "匯"},
                {"box": [189, 117, 229, 177], "text": "豐"},
                {"box": [385, 117, 426, 177], "text": "晉"},
                {"box": [466, 116, 508, 177], "text": "信"}
            ],
        "linking": [],
        "id": 1
    }
    """
    unique_labels = set()
    for data in dataset:
        documents = data["document"]  # type: ignore
        for document in documents:
            if "label" not in document:
                continue
            label = document["label"]
            unique_labels.add(label)
    label_list = list(unique_labels)
    label_list.sort()
    return label_list


def load_processor_from_hugging_face(config: dict) -> AutoProcessor:
    """
    load processor from hugging face
    """
    model_name: str = config["model"]["pre_train_model_from_hugging_face"]

    if not model_name:
        error_message = (
            "model/pre_train_model_from_hugging_face is not set in config.yaml"
        )
        train_logger.error(error_message)
        raise ValueError(error_message)

    try:
        processor = AutoProcessor.from_pretrained(model_name, apply_ocr=False)
        return processor
    except Exception as exc:
        train_logger.exception(
            "An unexpected error occurred while loading the processor: %s", exc
        )
        raise exc


def start() -> None:
    """
    start training
    """
    train_logger.info("Training started")
    config = load_config_yaml()

    dataset = load_training_data(config)
    print(dataset)
    processor = load_processor_from_hugging_face(config)
    labels = get_label_from_training_data(dataset)
    print(labels)
