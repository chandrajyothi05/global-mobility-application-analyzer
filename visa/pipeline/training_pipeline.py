import sys
from visa.logger import logging
from visa.exception import USVisaException
from visa.components.data_ingestion import DataIngestion
from visa.entity.config_entity import DataIngestionConfig
from visa.entity.artifact_entity import DataIngestionArtifact


class TrainingPipeline:
    def __init__(self):
        self.data_ingestion_config=DataIngestionConfig()
    def start_data_ingestion(self)->DataIngestionArtifact:
        # method responsible for starting the data ingestion component of training pipeline
        try:
            logging.info("Entered start_data_ingestion method of TrainingPipeline class")
            logging.info("Getting the data from mongodb")
            data_ingestion=DataIngestion(data_ingestion_config=self.data_ingestion_config)
            data_ingestion_artifact=data_ingestion.initiate_data_ingestion()
            logging.info("Got the train_set and test_set from mongodb")
            logging.info("Exited start_data_ingestion method of TrainingPipeline class")
            return data_ingestion_artifact
        except Exception as e:
            raise USVisaException(e,sys) from e
    
    def run_pipeline(self, )->None:
        # method responsible for running the complete pipeline
        try:
            data_ingestion_artifact=self.start_data_ingestion()
        except Exception as e:
            raise USVisaException(e,sys) from e