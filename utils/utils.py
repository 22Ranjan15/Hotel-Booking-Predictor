import os
import pandas as pd
from src.logger import get_logger
from src.exception import CustomException
import yaml

logger = get_logger(__name__)

def read_yaml(file_path):
    try:
        if not os.path.exists(file_path):
            logger.error(f"YAML file not found at path: {file_path}")
            raise FileNotFoundError(f"YAML file not found at the specified path: {file_path}")
        
        with open(file_path, "r") as yaml_file:
            config = yaml.safe_load(yaml_file)
            logger.info(f"Successfully read the YAML file from path: {file_path}")
            return config
    except Exception as e:
        logger.error(f"Unexpected error while reading YAML file at path: {file_path}. Error: {e}")
        raise CustomException(f"An unexpected error occurred while reading the YAML file at path: {file_path}", e)
    

def load_data(path):
    try:
        if not os.path.exists(path):
            logger.error(f"CSV file not found at path: {path}")
            raise FileNotFoundError(f"CSV file not found at the specified path: {path}")
        
        data = pd.read_csv(path)
        logger.info(f"Successfully loaded CSV file from path: {path}. Shape of the data: {data.shape}")
        return data
    except Exception as e:
        logger.error(f"Unexpected error while loading CSV file at path: {path}. Error: {e}")
        raise CustomException(f"An unexpected error occurred while loading the CSV file at path: {path}", e)


