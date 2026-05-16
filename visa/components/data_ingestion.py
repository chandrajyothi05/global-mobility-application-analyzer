import os,sys
from pandas import DataFrame
from sklearn.model_selection import train_test_split
from visa.entity.config_entity import DataIngestionConfig
from visa.entity.artifact_entity import DataIngestionArtifact
from visa.exception import USVisaException
from visa.logger import logging
from visa.data_access.visa_data import VisaData

class DataIngestion:
    def __init__(self,data_ingestion_config:DataIngestionConfig=DataIngestionConfig()):
        try:
            self.data_ingestion_config=data_ingestion_config
        except Exception as e:
            raise USVisaException(e,sys)

    def export_data_into_feature_store(self)->DataFrame:
        #exports data from mongodb to csv file
        #output: data is returned as artifact of data ingestion components

        try:
            logging.info(f"Exporting data from mongodb")
            usvisa_data=VisaData()
            dataframe=usvisa_data.export_collection_as_dataframe(collection_name=self.data_ingestion_config.collection_name)
            logging.info(f"Shape of dataframe: {dataframe.shape}")
            feature_store_file_path=self.data_ingestion_config.feature_store_file_path
            dir_path=os.path.dirname(feature_store_file_path)
            os.makedirs(dir_path,exist_ok=True)
            logging.info(f"Saving exported data into feature store file path: {feature_store_file_path}")
            dataframe.to_csv(feature_store_file_path,index=False,header=True)
            return dataframe
        except Exception as e:
            raise USVisaException(e,sys)

    def split_data_as_train_test(self,dataframe:DataFrame)->None:
        #this method splits the dataframe into train set nd test set based on the split ratio defined in the data ingestion config
        #output: folder is created in s3 bucket

        logging.info("Entered split_data_as_train_test method of DataIngestion class")
        try:
            train_set, test_set=train_test_split(dataframe, test_size=self.data_ingestion_config.train_test_split_ratio)
            logging.info("Performed train test split on the dataframe")
            logging.info("Exited split_data_as_train_test method of DataIngestion class")
            dir_path=os.path.dirname(self.data_ingestion_config.training_file_path)
            os.makedirs(dir_path,exist_ok=True)

            logging.info("Exporting train and test data to file path")
            train_set.to_csv(self.data_ingestion_config.training_file_path,index=False,header=True)
            test_set.to_csv(self.data_ingestion_config.testing_file_path,index=False,header=True)

            logging.info("Exporting train and test path")
        except Exception as e:
            raise USVisaException(e,sys)

    def initiate_data_ingestion(self)->DataIngestionArtifact:
        # method  initiates the data ingestion components of training pipeline
        # output : train set and test set are returned as the artifacts of data ingestion components
        logging.info("Entered initiate_data_ingestion method of DataIngestion class")

        try:
            dataframe= self.export_data_into_feature_store()
            logging.info("Got the data from mongodb")
            self.split_data_as_train_test(dataframe)
            logging.info("Performed train test split on the dataset")
            logging.info("Exited initiate_data_ingestion method of DataIngestion class")
            data_ingestion_artifact=DataIngestionArtifact(training_file_path=self.data_ingestion_config.training_file_path,
                                                        testing_file_path=self.data_ingestion_config.testing_file_path)
            logging.info(f"Data Ingestion artifact: {data_ingestion_artifact}")
            return data_ingestion_artifact
        except Exception as e:
            raise USVisaException(e,sys) from e
        



    