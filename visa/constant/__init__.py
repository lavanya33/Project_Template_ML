import os
from datetime import datetime

def get_current_time_stamp():
    return f"{datetime.now().strftime('%Y-%m-%d-%H-%M-%S')}" # year, month, date, hour, minute, second

CURRENT_TIME_STAMP = get_current_time_stamp() # to get current time stamp
ROOT_DIR = os.getcwd() #to get current working dir
CONFIG_DIR = "config" #folder of config.yaml file
CONFIG_FILE_NAME = "config.yaml" 

CONFIG_FILE_PATH = os.path.join(ROOT_DIR, CONFIG_DIR, CONFIG_FILE_NAME) #joining the config.yaml file to current working directory

# Data Ingested related variable
DATA_INGESTION_CONFIG_KEY = "data_ingestion_config"
DATA_INGESTION_DOWNLOAD_URL_KEY = "dataset_download_url"
DATA_INGESTION_ARTIFACT_DIR = "data_ingestion"
DATA_INGESTION_RAW_DATA_DIR_KEY = "raw_data_dir"
DATA_INGESTION_INGESTED_DIR_NAME_KEY = "ingested_dir"
DATA_INGESTION_TRAIN_DIR_KEY = "ingested_train_dir"
DATA_INGESTION_TEST_DIR_KEY = "ingested_test_dir"

# Training pipeline related variables
TRAINING_PIPELINE_CONFIG_KEY = "training_pipeline_config"
TRAINING_PIPELINE_NAME_KEY = "pipeline"
TRAINING_PIPELINE_ARTIFACT_DIR_KEY = "artifact_dir"


# Company Variable
COLUMN_COMPANY_AGE = "company_age"
COLUMN_YEAR_ESTB = "yr_of_estab"
COLUMN_ID = "case_id"
COLUMN_CASE_STATUS = "case_status"