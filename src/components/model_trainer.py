import os
import pandas as pd
import joblib
from sklearn.model_selection import RandomizedSearchCV
import lightgbm as lgb
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
from src.logger import get_logger
from src.exception import CustomException
from config.paths_config import *
from config.model_params import *
from utils.utils import read_yaml, load_data
from scipy.stats import randint

import mlflow
import mlflow.sklearn

logger = get_logger(__name__)

class ModelTraining:
    def __init__(self, train_path, test_path, model_output_path):
        try:
            self.train_path = train_path
            self.test_path = test_path
            self.model_output_path = model_output_path

            self.params_dist = LIGHTGM_PARAMS
            self.random_search_params = RANDOM_SEARCH_PARAMS

            logger.info("ModelTraining class initialized successfully.")
        except Exception as e:
            logger.error(f"Error during ModelTraining initialization: {e}")
            raise CustomException("Error during ModelTraining initialization", e)

    def load_and_split(self):
        try:
            logger.info(f"Loading training data from: {self.train_path}")
            train_df = load_data(self.train_path)

            logger.info(f"Loading testing data from: {self.test_path}")
            test_df = load_data(self.test_path)

            X_train = train_df.drop(columns='booking_status')
            y_train = train_df["booking_status"]

            X_test = test_df.drop(columns='booking_status')
            y_test = test_df["booking_status"]

            logger.info(f"Data successfully split into features and target variables. "
                        f"Training data shape: {X_train.shape}, Testing data shape: {X_test.shape}")
            return X_train, y_train, X_test, y_test

        except Exception as e:
            logger.error(f"Unexpected error while loading and splitting data: {e}")
            raise CustomException("Failed to load and split data", e)
        

    def train_lgbm(self, X_train, y_train):
        try:
            logger.info("Initializing LightGBM model.")
            lgbm_model = lgb.LGBMClassifier(random_state=self.random_search_params['random_state'])

            logger.info("Starting hyperparameter tuning with RandomizedSearchCV.")
            random_search = RandomizedSearchCV(
                estimator = lgbm_model,
                param_distributions = self.params_dist,
                n_iter = self.random_search_params['n_iter'],
                cv = self.random_search_params['cv'],
                verbose = self.random_search_params['verbose'],
                random_state = self.random_search_params['random_state'],
                scoring = self.random_search_params['scoring']
            )

            random_search.fit(X_train, y_train)
            logger.info("Hyperparameter tuning completed successfully.")


            best_params = random_search.best_params_
            best_lgbm_model = random_search.best_estimator_
            logger.info(f"Best parameters found: {best_params}")

            return best_lgbm_model
        
        except Exception as e:
            logger.error(f"Unexpected error during model training: {e}")
            raise CustomException("Failed to train model", e)
        
    def evaluate_model(self, model, X_test, y_test):
        try:
            logger.info("Evaluating the trained model on the test dataset.")

            y_pred = model.predict(X_test)

            accuracy = accuracy_score(y_test,y_pred)
            precision = precision_score(y_test,y_pred)
            recall = recall_score(y_test,y_pred)
            f1 = f1_score(y_test,y_pred)

            logger.info(f"Model evaluation metrics:\n"
                        f"Accuracy: {accuracy:.4f}\n"
                        f"Precision: {precision:.4f}\n"
                        f"Recall: {recall:.4f}\n"
                        f"F1 Score: {f1:.4f}")

            return {
                'accuracy': accuracy,
                'precision': precision,
                'recall': recall,
                'f1': f1
            }
        
        except Exception as e:
            logger.error(f"Unexpected error during model evaluation: {e}")
            raise CustomException("Failed to evaluate model", e)

        
    def save_model(self, model):
        try:
            os.makedirs(os.path.dirname(self.model_output_path), exist_ok=True)

            logger.info(f"Saving the trained model to: {self.model_output_path}")
            joblib.dump(model, self.model_output_path)
            logger.info("Model saved successfully.")
        
        except Exception as e:
            logger.error(f"Unexpected error while saving model: {e}")
            raise CustomException("Failed to save model", e)
        
    def run(self):
        try:
            with mlflow.start_run():
                logger.info("Starting the model training pipeline.")
                logger.info("Starting our mlflow experimentation.")

                logger.info("Logging the training and testing dataset to MLFlow.")
                mlflow.log_artifact(self.train_path, artifact_path="datasets")
                mlflow.log_artifact(self.test_path, artifact_path="datasets")

                X_train, y_train, X_test, y_test = self.load_and_split()
                model = self.train_lgbm(X_train, y_train)
                evaluation_metrics = self.evaluate_model(model, X_test, y_test)
                self.save_model(model)

                logger.info("Logging the model into MLFlow.")
                mlflow.log_artifact(self.model_output_path)

                logger.info("Logging Parameters and Metrices to MLFlow.")
                mlflow.log_params(model.get_params())
                mlflow.log_metrics(metrics=evaluation_metrics)

                logger.info("Model training pipeline completed successfully.")
                return evaluation_metrics

        except Exception as e:
            logger.error(f"Error in the model training pipeline: {e}")
            raise CustomException("Failed to execute model training pipeline", e)

if __name__ == "__main__":
    try:
        trainer = ModelTraining(PROCESSED_TRAIN_FILE_PATH, PROCESSED_TEST_FILE_PATH, MODEL_OUTPUT_PATH)
        metrics = trainer.run()
        logger.info(f"Final evaluation metrics: {metrics}")
    except Exception as e:
        logger.error(f"Fatal error in main execution: {e}")

    


            


