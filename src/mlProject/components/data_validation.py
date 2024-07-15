from mlProject.config.configuration import DataValidationConfig
import pandas as pd
import warnings
warnings.filterwarnings('ignore')

class DataValidation:
    def __init__(self,config:DataValidationConfig):
        self.config = config

    def validate_all_columns(self)->bool :
        try:
            validation_status_1 = None
            validation_status_2 = None
            validation_status_3 = None
            data = pd.read_excel(self.config.data_dir)

            # column validation
            all_cols = list(data.columns)
            all_schema = self.config.all_schema.keys()
            for col in all_cols:
                if col not in all_schema:
                    validation_status_1 = False
                    with open(self.config.STATUS_FILE,'w') as f:
                        f.write(f"Columns Validation status:{validation_status_1}")
                    break
                else:
                    validation_status_1 = True
                    with open(self.config.STATUS_FILE,'w') as f:
                        f.write(f"Columns Validation status:{validation_status_1}")

            # Airline data validation for label encoding
            airlines_list = list(dict(self.config.labels.airlines).keys())
            for i in list(data.Airline.unique()):
                if i not in airlines_list:
                    validation_status_2 = False
                    with open(self.config.STATUS_FILE,'a') as f:
                        f.write(f"\nAirline label_encoding Validation status:{validation_status_2}")
                    break
            else:
                validation_status_2 = True
                with open(self.config.STATUS_FILE,'a') as f:
                    f.write(f"\nAirline label_encoding Validation status:{validation_status_2}")
        

            # Destination data validation for label encoding
            destination_schema = list(dict(self.config.labels.destinations).keys())
            destination_list = list(data.Destination.unique())

            if 'New Delhi' in destination_list:
                destination_list.remove('New Delhi')            #Delhi and New Delhi is same for now

            for i in destination_list:
                if i not in destination_schema:
                    validation_status_3 = False
                    with open(self.config.STATUS_FILE,'a') as f:
                        f.write(f"\nDestination label_encoding Validation status:{validation_status_3}")
                    break
            else:
                validation_status_3 = True
                with open(self.config.STATUS_FILE,'a') as f:
                    f.write(f"\nDestination label_encoding Validation status:{validation_status_3}")




            return (validation_status_1,validation_status_2,validation_status_3)
        
        
        
        except Exception as e:
            raise e
         