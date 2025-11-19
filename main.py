from src.datascience import logger
from src.datascience.pipeline.data_ingestion_pipeline import DataIngestionTrainingPipeline
from src.datascience.pipeline.data_validation_pipeline import DataValidationTrainingPipeline
from src.datascience.pipeline.data_transformation_pipeline import DataTransformationPipeline

STAGE_NAME="Data Ingestion Stage"
try:
    logger.info(f">>>>>>>>>> Stage {STAGE_NAME} started <<<<<<<<<<")
    data_ingestion=DataIngestionTrainingPipeline()
    data_ingestion.initiate_data_ingestion()
    logger.info(f">>>>>>>>>> Stage {STAGE_NAME} completed <<<<<<<<<<\n\nx==========x")
except Exception as e:
        logger.exception(e)
        raise e
    
    
STAGE_NAME="Data Validation Stage"
try:
    logger.info(f">>>>>>>>>> Stage {STAGE_NAME} started <<<<<<<<<<")
    data_validation_pipeline=DataValidationTrainingPipeline()
    data_validation_pipeline.initiate_data_validation()
    logger.info(f">>>>>>>>>> Stage {STAGE_NAME} completed <<<<<<<<<<\n\nx==========x")
except Exception as e:
        logger.exception(e)
        raise e
    
    
STAGE_NAME="Data Transformation Stage"
try:
    logger.info(f">>>>>>>>>> Stage {STAGE_NAME} started <<<<<<<<<<")
    data_transformation_pipeline = DataTransformationPipeline()
    data_transformation_pipeline.initiate_data_transformation()
    logger.info(f">>>>>>>>>> Stage {STAGE_NAME} completed <<<<<<<<<<\n\nx==========x")
except Exception as e:
        logger.exception(e)
        raise e 