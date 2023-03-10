import os
from datetime import datetime
from sensor.constant  import training_pipeline


class TrainingPipelineConfig:

    def __init__(self):
        try:
            self.artifact_dir: str = os.path.joi)
        self.timestamp: str = timestamp






class DataIngestionConfig:
    def __init__(self,training_pipeline_config:TrainingPipelineConfig):
        try:
            self.database_name="aps"
            self.collection_name="sensor"
            self.data_ingestion_dir: str = os.path.join(training_pipeline_config.artifact_dir,"data_ingestion")
            self.feature_store_file_path: str = os.path.join(self.data_ingestion_dir,"feature_store",FILE_NAME)
            self.train_file_path: str = os.path.join(self.data_ingestion_dir,"dataset",TRAIN_FILE_NAME)
            self.test_file_path: str = os.path.join(self.data_ingestion_dir,"dataset",TEST_FILE_NAME)
            self.test_size=0.2
        except Exception as e:
            raise SensorException(e,sys)

    def to_dict(self,)->dict:
        try:
            return self.__dict__
        except Exception as e:
            raise SensorException(e,sys)

class DataValidationConfig:...
class DataTransformationConfig:...
class ModelTrainingConfig:...
class ModelEvaluatioConfig:...
class ModelPusherConfig:...
