import pandas as pd
import requests
import sys
from src.logger import logging
from src.exception import CustomException
import os

def load_data(c1, c2, h):
    """Load data from API endpoints into Pandas DataFrames."""
    try:
        def create_dataframe_from_json(url): # Helper function
            response = requests.get(url)
            response.raise_for_status()  # Check for HTTP errors
            json_data = response.json()

            if isinstance(json_data, list): # Check if it is a list of dictionary
                df = pd.json_normalize(json_data) # Normalize the JSON data
            elif isinstance(json_data, dict): # Check if it is a dictionary
                df = pd.DataFrame([json_data]) # Create a DataFrame with one row
            else:
                raise ValueError("JSON data is neither a list nor a dictionary")

            return df

        c1_data = create_dataframe_from_json(c1)
        c2_data = create_dataframe_from_json(c2)
        h_data = create_dataframe_from_json(h)

        logging.info('Data is loaded from JSON URL and stored in data folder')

        return c1_data, c2_data, h_data

    except requests.exceptions.RequestException as e:
        raise CustomException(f"Error fetching data: {e}", sys)
    except (ValueError, TypeError) as e:
        raise CustomException(f"Error processing JSON: {e}", sys)
    except Exception as e:
        raise CustomException(e, sys)



if __name__ == '__main__':
    c1= r'https://www.jsonkeeper.com/b/LLQT'
    c2= r'https://api.jsonserve.com/rJvd7g'
    h= r'https://api.jsonserve.com/XgAgFJ'
    
    try:    
        c_end_data, c_sub_data, prev_5 = load_data(c1, c2, h)
        output_dir = 'data'
        os.makedirs(output_dir, exist_ok=True)
        c_end_data.to_csv(os.path.join(output_dir, 'c_end_data.csv'), index=False)
        c_sub_data.to_csv(os.path.join(output_dir, 'c_sub_data.csv'), index=False)
        prev_5.to_csv(os.path.join(output_dir, 'prev_5.csv'), index=False)

    except CustomException as e:
        logging.error(f'Error:{e}')
    except Exception as e:
        logging.error(f'General error:{e}')
        




# # def fetch_data_from_api(api_url):
# #     """Fetch data from a given API endpoint."""
# #     try:
# #         response = requests.get(api_url)
# #         response.raise_for_status()  # Raises HTTPError for bad responses
# #         return response.json()
# #     except Exception as e:
# #         raise CustomException(e, sys)
