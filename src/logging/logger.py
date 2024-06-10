import logging
import logging.config
import os
import yaml


def load_config_yaml(config_path: str):
    """
    Load config from config.yaml and return dict of config.
    """
    try:
        with open(config_path, "r", encoding="utf-8") as config_file:
            config = yaml.safe_load(config_file)
            return config
    except FileNotFoundError:
        print(f"Error: The file {config_path} does not exist.")
    except yaml.YAMLError as exc:
        print(f"Error parsing YAML file {config_path}: {exc}")
    except Exception as exc:
        error_message = (
            f"An unexpected error occurred while loading the config file: {exc}"
        )
        print(error_message)


def init_logger(
    default_path="./src/logging/log_config.yaml",
    default_level=logging.INFO,
    env_key="LOG_CONFIG_PATH",
):
    """
    Setup logging configuration.
    """
    path = default_path
    value = os.getenv(env_key, None)
    if value:
        path = value
    if os.path.exists(path):
        with open(path, "rt", encoding="utf-8") as config_file:
            config = yaml.safe_load(config_file)
        logging.config.dictConfig(config)
    else:
        logging.basicConfig(level=default_level)


# 初始化 logging 配置
init_logger()

# Export logger
train_logger = logging.getLogger("train_logger")
app_logger = logging.getLogger("app_logger")
