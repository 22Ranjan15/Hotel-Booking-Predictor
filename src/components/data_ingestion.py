import os
import sys
import pandas as pd
from google.cloud import storage
from sklearn.model_selection import train_test_split
from src.exception import CustomException
from src.logger import get_logger
import yaml

logger = get_logger(__name__)

class DataIngestion:
    def __init__(self, config_path="config/config.yaml"):
        self.config = self.load_config(config_path)
        self.bucket_name = self.config['data_ingestion']['bucket_name']
        self.bucket_file_name = self.config['data_ingestion']['bucket_file_name']
        self.train_ratio = self.config['data_ingestion']['train_ratio']
        
        self.raw_data_path = "artifacts/data"
        os.makedirs(self.raw_data_path, exist_ok=True)

    def load_config(self, config_path):
        with open(config_path, 'r') as file:
            return yaml.safe_load(file)
        
    def download_from_gcp(self):
        try:
            logger.info(f"Attempting to download {self.bucket_file_name} from bucket {self.bucket_name}")
            
            client = storage.Client()
            bucket = client.get_bucket(self.bucket_name)
            blob = bucket.blob(self.bucket_file_name)

            raw_data_file_path = os.path.join(self.raw_data_path, self.bucket_file_name)
            blob.download_to_filename(raw_data_file_path)

            logger.info(f"Downloaded {self.bucket_file_name} from GCP bucket {self.bucket_name} to {raw_data_file_path}")
            
            return raw_data_file_path
        
        except Exception as e:
            raise CustomException(f"Failed to download file '{self.bucket_file_name}' from bucket '{self.bucket_name}'. Error: {str(e)}", sys) from e
        

    def split_data(self, raw_data_file_path):
        try:
            df = pd.read_csv(raw_data_file_path)

            logger.info(f"Loaded data with shape: {df.shape}")

            train_set, test_set = train_test_split(df, test_size=1-self.train_ratio, random_state=42)

            train_file_path = os.path.join(self.raw_data_path, "train.csv")
            test_file_path = os.path.join(self.raw_data_path, "test.csv")

            train_set.to_csv(train_file_path, index=False)
            test_set.to_csv(test_file_path, index=False)

            logger.info(f"Data successfully split into training and testing sets. Training data saved at: {train_file_path}, Testing data saved at: {test_file_path}.")
            logger.info(f"Training set size: {len(train_set)}, Testing set size: {len(test_set)}.")
        
            return train_file_path, test_file_path
        
        except Exception as e:
            raise CustomException(f"Failed to split data into train and test sets. Error: {str(e)}", sys) from e

    def run(self):
        try:
            raw_data_file_path = self.download_from_gcp()
            train_file_path, test_file_path = self.split_data(raw_data_file_path)
            
            return train_file_path, test_file_path
        
        except Exception as e:
            raise CustomException(f"Data ingestion failed: {str(e)}", sys) from e

if __name__ == "__main__":
    try:
        data_ingestion = DataIngestion()
        train_data_path, test_data_path = data_ingestion.run()

    except Exception as e:
        logger.error(f"Data Ingestion failed: {e}")