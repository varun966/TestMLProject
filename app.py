from src.mlproject.logger import logging
from src.mlproject.exception import CustomException
import sys
from src.mlproject.components.data_ingestion import DataIngestion, DataIngestionConfig



if __name__=="__main__":

    logging.info('The Execution has started')

    try:
        data_ingestion = DataIngestion()
        #data_ingestion_config = DataIngestionConfig()
        data_ingestion.initiate_data_ingestion()



    except Exception as e:
        logging.info("Custom Exception")
        raise CustomException(e, sys)


