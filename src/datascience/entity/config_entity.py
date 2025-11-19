from dataclasses import dataclass
from pathlib import Path
from typing import Any, Dict
@dataclass
class DataIngestionConfig:
    root_dir: Path
    source_URL: str
    local_data_files: Path
    unzip_dir: Path
    
    
# src/datascience/entity/config_entity.py

@dataclass
class DataValidationConfig:
    root_dir: Path
    unzip_data_dir: Path          # folder or file path
    STATUS_FILE: str              # path to a status file
    all_schema: Dict[str, Any]    # schema dictionary (e.g. COLUMNS)