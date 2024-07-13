from mlProject.config.configuration import ConfigurationManager
from mlProject.components.data_transformation import DataTransformation
from mlProject import logger



STAGE_NAME = "Data Transformation stage"

class DataTransformationTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        data_transformation_config = config.get_data_transformation_config()
        data_transformation = DataTransformation(config=data_transformation_config)
        data =  data_transformation.data_transformation()
        data_transformation.train_test_spliting(data)


if __name__ == '__main__':
    try:
        logger.info(f">>>>>>>>>>>{STAGE_NAME} started <<<<<<<<<<<<<")
        obj = DataTransformationTrainingPipeline()
        obj.main()
        logger.info(f">>>>>>>>>> stage {STAGE_NAME} completed <<<<<<<<<<<<<<")

    except Exception as e:
        logger.exception(e)
        raise e

