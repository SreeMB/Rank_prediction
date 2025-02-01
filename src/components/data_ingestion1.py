import os
import sys
from src.exception import CustomException
from src.logger import logging
import pandas as pd
from sklearn.model_selection import train_test_split
from dataclasses import dataclass
import requests
import re
from src.components.data_transformation import DataTransformation, DataTransformationConfig
from src.components.model_trainer import ModelTrainer, ModelTrainerConfig

@dataclass
class DataIngestionConfig:
    train_data_path: str = os.path.join('artifacts', "train.csv")
    test_data_path: str = os.path.join('artifacts', "test.csv")
    raw_data_path: str = os.path.join('artifacts', "data.csv")

class DataIngestion:
    def __init__(self):
        self.ingestion_config = DataIngestionConfig()
      
    def clean_title(title):
        title_lower = re.sub(r'\s*\(.*?\)|\s*pyq', '', title.lower())
        return title_lower
    
    # def clean_title(title):
    #     title_lower = re.sub(r'\s*\(.*?\)|\s*pyq', '', title.lower())
    #     return title_lower
    
    def initiate_data_ingestion(self):
        logging.info("Entered the data ingestion method or component")
        try:
            # Load data from API URLs
            c1 = r'https://www.jsonkeeper.com/b/LLQT'
            c2 = r'https://api.jsonserve.com/rJvd7g'
            h = r'https://api.jsonserve.com/XgAgFJ'
            
            def create_dataframe_from_json(url):
                response = requests.get(url)
                response.raise_for_status()
                json_data = response.json()
                
                if isinstance(json_data, list):
                    df = pd.json_normalize(json_data)
                elif isinstance(json_data, dict):
                    df = pd.DataFrame([json_data])
                else:
                    raise ValueError("JSON data is neither a list nor a dictionary")
                
                return df
            
            c1_data = create_dataframe_from_json(c1)
            c2_data = create_dataframe_from_json(c2)
            h_data = create_dataframe_from_json(h)
            
            df = pd.DataFrame(h_data)
            logging.info('Data loaded and merged into a single DataFrame')
            
            # Apply Data Cleaning & Transformations

            df = df[['quiz_id', 'submitted_at','score', 'trophy_level', 'accuracy', 'speed', 'final_score',
                    'negative_score', 'correct_answers', 'incorrect_answers', 'source',
                    'type', 'started_at', 'ended_at', 'better_than',
                    'total_questions', 'rank_text', 'mistakes_corrected',
                    'initial_mistake_count', 'quiz.title', 'quiz.topic']]


            df['started_at'] = pd.to_datetime(df['started_at']).dt.strftime('%d-%m-%y %H:%M:%S')
            df['ended_at'] = pd.to_datetime(df['ended_at']).dt.strftime('%d-%m-%y %H:%M:%S')
            df['submitted_at'] = pd.to_datetime(df['submitted_at']).dt.strftime('%d-%m-%y %H:%M:%S')

            df['rank'] = df['rank_text'].str.extract(r'#-?(\d+)').astype(int)
            df = df.drop(columns='rank_text', axis=1)


            
            df['title'] = df['quiz.title'].apply(lambda x: re.sub(r'\s*\(.*?\)|\s*pyq', '', x.lower()) if isinstance(x, str) else x)


            df['quiz.topic'].replace('Body Fluids and Circulation ', 'Body fluids and circulation', inplace=True)
            df['quiz.topic'].replace('Body Fluids and Circulation', 'Body fluids and circulation', inplace=True)
            df['quiz.topic'].replace('reproductive health ', 'Reproductive Health', inplace=True)
            
            df['accuracy'] = df['accuracy'].str.replace('%', '').astype(float)
            df['trophy_level'] = df['trophy_level'].astype('object')
            
            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path), exist_ok=True)
            df.to_csv(self.ingestion_config.raw_data_path, index=False, header=True)

            logging.info("Train test split initiated")
            train_set, test_set = train_test_split(df, test_size=0.2, random_state=42)

            train_set.to_csv(self.ingestion_config.train_data_path, index=False, header=True)
            test_set.to_csv(self.ingestion_config.test_data_path, index=False, header=True)

            logging.info("Ingestion of the data is completed")

            return (
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path
            )
        except Exception as e:
            raise CustomException(e, sys)
        


if __name__ == "__main__":
    obj = DataIngestion()
    train_data, test_data = obj.initiate_data_ingestion()

    data_transformation = DataTransformation()
    train_arr, test_arr, _ = data_transformation.initiate_data_transformation(train_data, test_data)

    modeltrainer = ModelTrainer()
    print(modeltrainer.initiate_model_trainer(train_arr, test_arr))
