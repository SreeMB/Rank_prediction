import os
import sys
import re
import pickle
import pandas as pd
from src.exception import CustomException
from src.logger import logging
from src.utils import load_object

class RankPredictor:
    def __init__(self):
        self.model_path = "artifacts/model.pkl"
        self.preprocessor_path = "artifacts/proprocessor.pkl"
        logging.info("Initializing RankPredictor class")
        self.model = self.load_model()
        self.preprocessor = self.load_preprocessor()

    def load_model(self):
        """Load the trained model from file."""
        try:
            logging.info(f"Loading model from {self.model_path}")
            with open(self.model_path, "rb") as file:
                model = pickle.load(file)
            logging.info("Model loaded successfully")
            return model
        except Exception as e:
            logging.error(f"Error loading model: {e}")
            raise CustomException(e, sys)

    def load_preprocessor(self):
        """Load the preprocessing object from file."""
        try:
            logging.info(f"Loading preprocessor from {self.preprocessor_path}")
            preprocessor = load_object(self.preprocessor_path)
            logging.info("Preprocessor loaded successfully")
            return preprocessor
        except Exception as e:
            logging.error(f"Error loading preprocessor: {e}")
            raise CustomException(e, sys)

    def preprocess_input(self, input_data):
        """Preprocess input to match model format."""
        try:
            logging.info("Preprocessing input data")
            df = pd.DataFrame([input_data])  # Convert input dictionary to DataFrame
            processed_input = self.preprocessor.transform(df)  # Apply preprocessing
            logging.info("Input data preprocessed successfully")
            return processed_input
        except Exception as e:
            logging.error(f"Error in preprocessing: {e}")
            raise CustomException(e, sys)

    def predict_rank(self, input_data):
        """Predict NEET rank for given input."""
        try:
            logging.info("Predicting NEET rank")
            processed_input = self.preprocess_input(input_data)
            predicted_rank = self.model.predict(processed_input)[0]  # Get prediction
            logging.info(f"Prediction successful. Predicted NEET Rank: {int(predicted_rank)}")
            return int(predicted_rank)
        except Exception as e:
            logging.error(f"Prediction error: {e}")
            raise CustomException(e, sys)

if __name__ == "__main__":
    logging.info("Starting Rank Prediction")
    predictor = RankPredictor()

    # 🎯 Sample Input Data
    input_data = {
        "quiz_id": 101,
        "score": 32,
        "accuracy": 80.0,
        "speed": 100,
        "final_score": 30.0,
        "negative_score": 2.0,
        "correct_answers": 8,
        "incorrect_answers":2,
        "better_than": 24,
        "total_questions": 128,
        "mistakes_corrected": 6,
        "initial_mistake_count": 18,
        "submitted_at" : "17-01-25 15:30:18",
        'trophy_level': '2', 
        'source': 'live',
        'type': 'topic', 
        'started_at':"17-01-25 15:18:30", 
        'ended_at':  "17-01-25 15:29:00",
        'quiz.title': 'reproduction', 
        'title': 'reproduction', 
        'quiz.topic': 'reproduction'
    }

    predicted_rank = predictor.predict_rank(input_data)
    print(f"Predicted NEET Rank: {predicted_rank}")
