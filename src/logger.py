import logging
import os
from datetime import datetime 
LOG_FILE = f"{datetime.now().strftime('%d_%m_%Y_%H_%M_%S')}.log"  # Generates a string of the specified format and stores in LOG_FILE variable

logs_path = os.path.join(os.getcwd(), "logs", LOG_FILE)

os.makedirs(logs_path, exist_ok = True)

LOG_FILE_PATH = os.path.join(logs_path, LOG_FILE)

logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)
# if __name__ == '__main__':
#     logging.info("Logging has started with small change2")       # To check the working, to be commented out will project running
				
				
