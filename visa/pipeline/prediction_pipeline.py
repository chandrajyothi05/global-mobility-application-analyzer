import os, sys
import numpy as np
import pandas as pd
from pandas import DataFrame
from visa.entity.config_entity import VisaPredictorConfig
from visa.entity.s3_estimator import VisaEstimator
from visa.exception import USVisaException
from visa.logger import logging

class VisaData:
    def __init__(self, continent,
                 education_of_employee,
                 has_job_experience,
                 requires_job_training,
                 no_of_employees,
                 region_of_employment,
                 prevailing_wage,
                 unit_of_wage,
                 full_time_position,
                 company_age):
        try:
            self.continent=continent
            self.education_of_employee=education_of_employee
            self.has_job_experience=has_job_experience
            self.requires_job_training=requires_job_training
            self.no_of_employees=no_of_employees
            self.region_of_employment=region_of_employment
            self.prevailing_wage=prevailing_wage
            self.unit_of_wage=unit_of_wage
            self.full_time_position=full_time_position
            self.company_age=company_age
        except Exception as e:
            raise USVisaException(e,sys) from e
        
    def get_usvisa_data_as_dict(self):
        # method returns a dictionary from VisaData class
        logging.info("Entered get_usvisa_data_as_dict")
        try:
            input_data={
                "continent":[self.continent],
                "education_of_employee":[self.education_of_employee],
                "has_job_experience":[self.has_job_experience],
                "requires_job_training":[self.requires_job_training],
                "no_of_employees":[self.no_of_employees],
                "region_of_employment":[self.region_of_employment],
                "prevailing_wage":[self.prevailing_wage],
                "unit_of_wage":[self.unit_of_wage],
                "full_time_position":[self.full_time_position],
                "company_age":[self.company_age],
            }
            logging.info("Exited get_usvisa_data_as_dict")
            return input_data
        except Exception as e:
            raise USVisaException(e,sys) from e
         
    def get_usvisa_input_data_frame(self)->DataFrame:
        # method returns a dataframe from visadata class input
        try:
            usvisa_input_dict=self.get_usvisa_data_as_dict()
            return DataFrame(usvisa_input_dict)
        except Exception as e:
            raise USVisaException(e,sys) from e
        
    

class VisaClassifier:
    def __init__(self,prediction_pipeline_config:VisaPredictorConfig=VisaPredictorConfig(),):
        try:
            self.prediction_pipeline_config=prediction_pipeline_config
        except Exception as e:
            raise USVisaException(e,sys)
    
    def predict(self,dataframe)->str:
        try:
            logging.info("Entered predict method")
            model=VisaEstimator(
                bucket_name=self.prediction_pipeline_config.model_bucket_name,
                model_path=self.prediction_pipeline_config.model_file_path,
            )
            result=model.predict(dataframe)
            return result
        except Exception as e:
            raise USVisaException(e,sys) from e
    