import sys
from pandas import DataFrame
from sklearn.pipeline import Pipeline
from visa.exception import USVisaException
from visa.logger import logging

class TargetValueMapping:
    def __init__(self):
        self.Certified:int=0
        self.Denied:int=1
    def _asdict(self):
        return self.__dict__
    def reverse_mapping(self):
        mapping_response=self._asdict()
        return dict(zip(mapping_response.values(),mapping_response.keys()))
    
class VisaModel:
    def __init__(self,preprocessing_object:Pipeline,trained_model_object:object):
        #load the preprocessing object and trained model object
        self.preprocessing_object=preprocessing_object
        self.trained_model_object=trained_model_object

    def predict(self,dataframe:DataFrame)->DataFrame:
        """
        function accepts raw inputs and then transformed raw input using preprocessing_object
        which guarantees that input is in the same format as training data and then it performs prediction using trained_model_object
        """
        logging.info("Entered predict method of VisaModel class")
        try:
            logging.info("Used the trained model to get predictions")
            transformed_feature = self.preprocessing_object.transform(dataframe)
            logging.info("Used the trained model to get predictions")
            return self.trained_model_object.predict(transformed_feature)
        except Exception as e:
            raise USVisaException(e,sys) from e
        
    def __repr__(self):
        return f"{type(self.trained_model_object).__name__}()"
    def __str__(self):
        return f"{type(self.trained_model_object).__name__}()"