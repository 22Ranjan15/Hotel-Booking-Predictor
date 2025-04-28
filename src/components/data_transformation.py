import os 
import pandas as pd
import numpy as np
from src.logger import get_logger
from src.exception import CustomException
from config.paths_config import *
from utils.utils import read_yaml, load_data

from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
from imblearn.over_sampling import SMOTE

logger = get_logger(__name__)

class DataProcessor:
    def __init__(self, train_path, test_path, processed_dir, config_path):
        try:
            self.train_path = train_path
            self.test_path = test_path
            self.processed_dir = processed_dir

            logger.info(f"Reading configuration from: {config_path}")
            self.config = read_yaml(config_path)

            if not os.path.exists(self.processed_dir):
                os.makedirs(self.processed_dir)
                logger.info(f"Created processed directory at: {self.processed_dir}")
        except Exception as e:
            logger.error(f"Error during DataProcessor initialization: {e}")
            raise CustomException("Error during DataProcessor initialization", e)
    
    def preprocess_data(self, df):
        try:
            logger.info("Starting Data Processing")

            # Dropping Unnecessary Column
            logger.info("Dropping unnecessary columns")
            if 'Booking_ID' in df.columns:
                df.drop(columns=['Booking_ID'], inplace=True)

            # Dropping duplicate rows
            logger.info("Dropping duplicate rows")
            initial_shape = df.shape
            df.drop_duplicates(inplace=True)
            logger.info(f"Dropped {initial_shape[0] - df.shape[0]} duplicate rows")

            # Handling categorical and numerical columns
            cat_cols = self.config['data_processing']['categorical_cols']
            num_cols = self.config['data_processing']['numerical_cols']

            # Label Encoding
            logger.info("Performing label encoding on categorical columns")
            label_encoder = LabelEncoder()
            mappings = {}
            for col in cat_cols:
                if col in df.columns:
                    df[col] = label_encoder.fit_transform(df[col])
                    mappings[col] = {label: code for label, code in zip(label_encoder.classes_, label_encoder.transform(label_encoder.classes_))}
            logger.info(f"Label encoding mappings: {mappings}")

            # Log Transformation to handle skewness
            logger.info("Handling skewness in numerical columns")
            skewness_threshold = self.config['data_processing']['skewness_threshold']
            skewness = df[num_cols].apply(lambda x: x.skew())
            for col in skewness[skewness > skewness_threshold].index:
                df[col] = np.log1p(df[col])
                logger.info(f"Applied log transformation to column: {col}")

            logger.info("Data preprocessing completed successfully")
            return df
        
        except Exception as e:
            logger.error(f"Unexpected error during preprocessing: {e}")
            raise CustomException("Error while preprocessing data", e)
        
    def balance_data(self, df):
        try:
            logger.info("Starting data balancing using SMOTE")

            # Splitting the dataset into features (X) and target (y)
            X = df.drop(columns='booking_status')
            y = df['booking_status']

            smote = SMOTE(random_state=42)
            X_resampled, y_resampled = smote.fit_resample(X, y)

            balanced_df = pd.DataFrame(X_resampled, columns=X.columns)
            balanced_df["booking_status"] = y_resampled

            logger.info(f"Data balancing completed. Resampled dataset shape: {balanced_df.shape}")
            return balanced_df
        
        except Exception as e:
            logger.error(f"Unexpected error during data balancing: {e}")
            raise CustomException("Error while balancing data", e)
        
    def feature_selection(self, df):
        try:
            logger.info("Performing feature selection")

            X = df.drop(columns='booking_status')
            y = df["booking_status"]

            model =  RandomForestClassifier(random_state=42)
            model.fit(X,y)

            feature_importance = model.feature_importances_

            feature_importance_df = pd.DataFrame({
                'feature':X.columns,
                'importance':feature_importance
            })

            top_features_importance_df = feature_importance_df.sort_values(by="importance", ascending=False)
            no_features_to_select = self.config['data_processing']['no_of_features']
            selected_features = top_features_importance_df["feature"].head(no_features_to_select).values

            logger.info(f"Selected top {no_features_to_select} features: {selected_features}")

            new_featured_df = df[selected_features.tolist() + ["booking_status"]]
            logger.info("Feature selection completed successfully")
            return new_featured_df
        
        except Exception as e:
            logger.error(f"Unexpected error during feature selection: {e}")
            raise CustomException("Error while selecting important features", e)
        
    
    def save_data(self, df, file_path):
        try:
            logger.info(f"Saving data to: {file_path}")
            df.to_csv(file_path, index=False)
            logger.info(f"Data saved successfully to: {file_path}")

        except Exception as e:
            logger.error(f"Unexpected error while saving data: {e}")
            raise CustomException("Error during saving processed data", e)
        
    def process(self):
        try:
            logger.info("Starting data processing pipeline")

            # Load raw data
            train_df = load_data(self.train_path)
            test_df = load_data(self.test_path)

            # Preprocess data
            processed_train_df = self.preprocess_data(train_df)
            processed_test_df = self.preprocess_data(test_df)

            # Balance data
            balanced_train_df = self.balance_data(processed_train_df)
            balanced_test_df = self.balance_data(processed_test_df)

            # Feature selection
            final_train_df = self.feature_selection(balanced_train_df)
            final_test_df = balanced_test_df[final_train_df.columns]

            # Save processed data
            self.save_data(final_train_df, PROCESSED_TRAIN_FILE_PATH)
            self.save_data(final_test_df, PROCESSED_TEST_FILE_PATH)

            logger.info("Data processing pipeline completed successfully")

        except Exception as e:
            logger.error(f"Error during data processing pipeline: {e}")
            raise CustomException("Error during data processing pipeline", e)

if __name__ == "__main__":
    try:
        processor = DataProcessor(TRAIN_FILE_PATH, TEST_FILE_PATH, PROCESSED_DIR, CONFIG_PATH)
        processor.process()
    except Exception as e:
        logger.error(f"Fatal error in main execution: {e}")
        










