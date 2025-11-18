import os
import yaml
from src.datascience import logger
import json
import joblib
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any
from box.exceptions import BoxValueError, BoxKeyError

@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """Reads a YAML file and returns a ConfigBox object.

    Args:
        path_to_yaml (str): Path like input
        
    Raises:
        ValueError: If the file is empty
        e: empty file
    Returns:
        ConfigBox: ConfigBox type object"""

    try:
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"yaml file: {path_to_yaml} loaded successfully")
            return ConfigBox(content)
    except BoxValueError:
        raise ValueError("yaml file is empty")
    except BoxKeyError as e:
        raise e
    
    
@ensure_annotations
def create_directories(path_to_directories: list, verbose=True):
    """Create list of directories

    Args:
        path_to_directories (list): List of directory paths
        verbose (bool, optional): Whether to log info messages. Defaults to True.
    """
    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f"Created directory at: {path}")
            
            
@ensure_annotations
def save_json(path: Path, data: dict):
    """Saves a dictionary to a JSON file.

    Args:
        path (Path): Path to the JSON file
        data (dict): Data to be saved
    """
    with open(path, "w") as j:
        json.dump(data, f, indent=4)
    logger.info(f"JSON file saved at: {path}")
    
    
@ensure_annotations
def load_json(path: Path) -> ConfigBox:
    """Loads a JSON file and returns a ConfigBox object.

    Args:
        path (Path): Path to the JSON file
    """
    with open(path) as f:
        content = json.load(f)
    logger.info(f"JSON file: {path} loaded successfully")
    return ConfigBox(content)


@ensure_annotations
def save_bin(data: Any, path: Path):
    """Saves data to a binary file using joblib.

    Args:
        data (Any): Data to be saved
        path (Path): Path to the binary file
    """
    joblib.dump(calue=data, filename=path)
    logger.info(f"Binary file saved at: {path}")
    
    
@ensure_annotations
def load_bin(path: Path) -> Any:
    """Loads data from a binary file using joblib.

    Args:
        path (Path): Path to the binary file
    """
    data = joblib.load(path)
    logger.info(f"Binary file: {path} loaded successfully")
    return data