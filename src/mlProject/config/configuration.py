from mlProject.constants import *
from mlProject.utils.common import read_yaml,create_directories
from mlProject.entity.config_entity import (DataIngestionConfig,
                                           DataValidationConfig,
                                           DataTransformationConfig,
                                           ModelTrainerConfig,
                                           ModelEvaluationConfig,
                                           DataPredictionConfig)


class ConfigurationManager:
    def __init__ (
            self,
            config_filepath = CONFIG_FILE_PATH,
            params_filepath = PARAMS_FILE_PATH,
            schema_filepath = SCHEMA_FILE_PATH,
            label_encoding_filepath = LABEL_ENCODING_FILE_PATH):
        
            self.config = read_yaml(config_filepath)
            self.params = read_yaml(params_filepath)
            self.schema = read_yaml(schema_filepath)
            self.labels = read_yaml(label_encoding_filepath)

            create_directories([self.config.artifacts_root])


    def get_data_ingestion_config(self) -> DataIngestionConfig:
        config = self.config.data_ingestion

        create_directories([config.root_dir])

        data_ingestion_config = DataIngestionConfig(
             root_dir= config.root_dir,
             source_URL=config.source_URL,
             local_data_file=config.local_data_file,
        )

        return data_ingestion_config
    

    def get_data_validation_config(self) -> DataValidationConfig:
        config = self.config.data_validation
        schema = self.schema.COLUMNS
        labels = self.labels

        create_directories([config.root_dir])

        data_validation_config = DataValidationConfig(
             root_dir= config.root_dir,
             STATUS_FILE= config.STATUS_FILE,
             data_dir= config.data_dir,
             all_schema=schema,
             labels = labels
        )

        return data_validation_config
    

    def get_data_transformation_config(self) -> DataTransformationConfig:
        config = self.config.data_transformation
        label_encoders = self.labels

        create_directories([config.root_dir])

        data_transformation_config = DataTransformationConfig(
             root_dir= config.root_dir,
             data_path=config.data_path,
             label_encoders = label_encoders
        )

        return data_transformation_config
    

    def get_model_trainer_config(self) -> ModelTrainerConfig:
            config = self.config.model_trainer
            schema = self.schema.TARGET_COLUMN
            params = self.params.XGBRegressor

            create_directories([config.root_dir])

            model_trainer_config = ModelTrainerConfig(
                    root_dir= config.root_dir,
                    train_data_path=config.train_data_path,
                    test_data_path= config.test_data_path,
                    model_name=config.model_name,
                    learning_rate=params.learning_rate,
                    max_depth=params.max_depth,
                    n_estimators=params.n_estimators,
                    target_column=schema.name

            )

            return model_trainer_config
    
    
    def get_model_evaluation_config(self) -> ModelEvaluationConfig:
                config = self.config.model_evaluation
                schema = self.schema.TARGET_COLUMN
                params = self.params.XGBRegressor

                create_directories([config.root_dir])

                model_evalution_config = ModelEvaluationConfig(
                        root_dir= config.root_dir,
                        test_data_path= config.test_data_path,
                        model_path=config.model_path,
                        all_params=params,
                        metric_file_name=config.metric_file_name,
                        target_column= schema.name

                )

                return model_evalution_config
    


    def get_data_prediction_config(self) -> DataPredictionConfig:
        config = self.config.data_prediction
        label_encoders = self.labels


        data_prediction_config = DataPredictionConfig(
             root_dir= config.root_dir,
             model_path=config.model_path,
             data_path=config.data_path,
             label_encoders = label_encoders
        )

        return data_prediction_config