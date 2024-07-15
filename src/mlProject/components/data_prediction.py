import pandas as pd
import numpy as np
import joblib
import warnings
warnings.filterwarnings('ignore')
from mlProject.config.configuration import DataPredictionConfig


class DataPrediction:
    def __init__(self,config:DataPredictionConfig):
        self.config = config
        

    def data_transformation_for_prediction(self,df_):

        #creating columns for month,year,day of journey

        df_.Date_of_Journey = pd.to_datetime(df_.Date_of_Journey)
        df_['Journey_month'] = df_.Date_of_Journey.dt.month
        df_['Journey_year'] = df_.Date_of_Journey.dt.year
        df_['Journey_day'] = df_.Date_of_Journey.dt.day


        # creating columns for hours,min for depature and arrival time
        df_.Dep_Time = pd.to_datetime(df_.Dep_Time)
        df_['Dep_Time_hours'] = df_.Dep_Time.dt.hour
        df_['Dep_Time_mins'] = df_.Dep_Time.dt.minute
        df_.Arrival_Time = pd.to_datetime(df_.Arrival_Time)
        df_['Arrival_Time_hours'] = df_.Arrival_Time.dt.hour
        df_['Arrival_Time_mins'] = df_.Arrival_Time.dt.minute


        df_ = df_.drop(['Date_of_Journey','Dep_Time','Arrival_Time'],axis=1)

        def duration_hours(x):
            if 'h' in x:
                return int(x.split('h')[0])
            else:
                return 0


        def duration_mins(x):
            if 'h' in x and 'm' in x:
                return int(x.split(' ')[1].split('m')[0])

            elif 'm' in x:
                return int(x.split('m')[0])

            else:
                return 0


        df_['Duration_hours'] = df_['Duration'].apply(duration_hours)
        df_['Duration_minutes'] = df_['Duration'].apply(duration_mins)


        def total_mins(x):
            total = x['Duration_hours']*60 + x['Duration_minutes']
            return total

        df_['Duration_total_minutes'] = df_.apply(total_mins,axis=1)

        df_ = df_.drop('Duration',axis=1)

        sources = pd.read_excel(self.config.data_path).Source.unique()


        # Applying One-Hot encoder in sources column
        for source in sources:
            df_['Source_'+source] = np.nan
            df_['Source_'+source] = np.where(df_['Source']==source,1,0)


        df_['Airline label'] = np.nan

        airlines = dict(self.config.label_encoders.airlines)
        
        # Applying Label encoding in airline column
        df_['Airline label'] = df_['Airline'].map(airlines)
        df_ = df_.drop('Airline',axis=1)


        destinations = dict(self.config.label_encoders.destinations)

        # df_.Destination = df_.Destination.replace('Delhi','New Delhi')

        # Applying Label encoding in destination column
        df_['Destination label'] = df_.Destination.map(destinations)

        # Dropping unncessary columns
        df_ = df_.drop(['Source','Destination','Additional_Info'],axis=1)

        stops_labels = {'non-stop':0,'1 stop':1,'2 stops':2,'3 stops':3,'4 stops':4}

        # Applying label encoding in total_stops column
        df_['Total_Stops_label'] = df_['Total_Stops'].map(stops_labels)

        df_['Total_Stops_label'] = df_['Total_Stops_label'].astype('int')

        df_ = df_.drop('Total_Stops',axis=1)

        df_ = df_.drop('Route',axis=1)

        df_ = df_.drop('Journey_year',axis=1)   # only 2019 year exists

        df_ = df_.drop('Price',axis=1)


        # changing float values to int
        for col in df_.columns:
            if df_[col].dtype == 'float64':
                df_[col]= df_[col].astype('int')


        model = joblib.load(self.config.model_path)

        predict = model.predict(df_)

        return predict