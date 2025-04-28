from src.components.data_ingestion import DataIngestion
from src.components.data_transformation import DataProcessor
from src.components.model_trainer import ModelTraining
from config.paths_config import *

if __name__ == "__main__":
    # 1. Data Ingestion
    data_ingestion = DataIngestion()
    train_data_path, test_data_path = data_ingestion.run()

    # 2. Data Processing & Transformation
    processor = DataProcessor(TRAIN_FILE_PATH, TEST_FILE_PATH, PROCESSED_DIR, CONFIG_PATH)
    processor.process()

    # 3. Model Training
    trainer = ModelTraining(PROCESSED_TRAIN_FILE_PATH, PROCESSED_TEST_FILE_PATH, MODEL_OUTPUT_PATH)
    metrics = trainer.run()