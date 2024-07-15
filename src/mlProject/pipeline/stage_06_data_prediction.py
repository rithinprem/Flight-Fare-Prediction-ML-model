from mlProject.config.configuration import ConfigurationManager
from mlProject.components.data_prediction import DataPrediction
from mlProject import logger



STAGE_NAME = "Data Prediction stage"

class DataPredictionPipeline:
    def __init__(self):
        pass

    def main(self,df_):
        config = ConfigurationManager()
        data_prediction_config = config.get_data_prediction_config()
        data_prediction_config = DataPrediction(config=data_prediction_config)
        predict = data_prediction_config.data_transformation_for_prediction(df_)
        return predict


if __name__ == '__main__':
    try:
        logger.info(f">>>>>>>>>>>{STAGE_NAME} started <<<<<<<<<<<<<")
        obj = DataPredictionPipeline()
        obj.main()
        logger.info(f">>>>>>>>>> stage {STAGE_NAME} completed <<<<<<<<<<<<<<")

    except Exception as e:
        logger.exception(e)
        raise e

