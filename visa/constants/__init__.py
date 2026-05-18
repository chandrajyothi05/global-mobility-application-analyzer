import os
from datetime import date

DATABASE_NAME="VISA_APPLICATION_DATA"
COLLECTION_NAME="visa_data"
MONGODB_URL_KEY="MONGODB_URL"

PIPELINE_NAME: str="visa"
ARTIFACT_DIR: str="artifact"

MODEL_FILE_NAME="model.pkl"

TARGET_COLUMN="case_status"

CURRENT_YEAR=date.today().year

PREPRPOCESSING_OBJECT_FILE_NAME="preprocessing.pkl"

FILE_NAME:str="visa.csv"
TRAIN_FILE_NAME:str="train.csv"
TEST_FILE_NAME:str="test.csv"
SCHEMA_FILE_PATH=os.path.join("config","schema.yaml")

AWS_ACCESS_KEY_ID_ENV_KEY="AWS_ACCESS_KEY_ID"
AWS_SECRET_ACCESS_KEY_ENV_KEY="AWS_SECRET_ACCESS_KEY"
REGION_NAME="us-east-1"

#data ingestion related constants
DATA_INGESTION_COLLECTION_NAME:str="visa_data"
DATA_INGESTION_DIR_NAME:str="data_ingestion"
DATA_INGESTION_FEATURE_STORE_DIR:str="feature_store"
DATA_INGESTION_INGESTED_DIR:str="ingested"
DATA_INGESTION_TRAIN_TEST_SPLIT_RATIO:float=0.2

#data validation related constants
DATA_VALIDATION_DIR_NAME:str="data_validation"
DATA_VALIDATION_SCHEMA_FILE_NAME:str="schema.yaml"
DATA_VALIDATION_REPORT_FILE_NAME:str="report.yaml"
DATA_VALIDATION_DRIFT_REPORT_DIR = "drift_report"
DATA_VALIDATION_DRIFT_REPORT_FILE_NAME = "report.yaml"

#data transformation related constants
DATA_TRANSFORMATION_DIR_NAME:str="data_transformation"
DATA_TRANSFORMATION_TRANSFORMED_DATA_DIR:str="transformed"
DATA_TRANSFORMATION_TRANSFORMED_OBJECT_DIR:str="transformed_object"
