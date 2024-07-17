from flask import Flask,render_template,request
import os
import pandas as pd
from datetime import datetime
from mlProject.pipeline.stage_06_data_prediction import DataPredictionPipeline


app = Flask(__name__)

@app.route("/")
def homepage():
    return render_template('index.html')


@app.route('/train',methods=['GET'])
def training():
    os.system("python main.py")
    return "Training Successful!"



@app.route('/predict',methods=['POST','GET']) # route to show the predictions in a web UI
def index():
    if request.method == 'POST':
        try:
            airline = str(request.form.get('airline'))
            date_of_journey = request.form.get('date_of_journey')
            source = str(request.form.get('source'))
            destination = str(request.form.get('destination'))
            dep_time = request.form.get('dep_time')
            arrival_time = request.form.get('arrival_time')
            total_stops = str(request.form.get('total_stops'))
            additional_info = str(request.form.get('additional_info'))

            def hours_minutes_calc(start_time, end_time):
                time_format = "%H:%M"
                start = datetime.strptime(start_time, time_format)
                end = datetime.strptime(end_time, time_format)
                total_minutes = (end - start).seconds // 60
                return divmod(total_minutes, 60)
            
            hours,minutes = hours_minutes_calc(dep_time,arrival_time)
            duration = str(hours)+"h"+" " +str(minutes)+"m"

            data = {'Airline': {0: f'{airline}'},
                    'Date_of_Journey': {0: f'{date_of_journey}'},
                    'Source': {0: f'{source}'},
                    'Destination': {0: f'{destination}'},
                    'Route': {0: 'NA'},
                    'Dep_Time': {0: f'{dep_time}'},
                    'Arrival_Time': {0: f'{arrival_time}'},
                    'Duration': {0: f'{duration}'},
                    'Total_Stops': {0: f'{total_stops}'},
                    'Additional_Info': {0: f'{additional_info}'},
                    'Price':{0:'NA'}
                    }
            
           
            df_ = pd.DataFrame(data)
            obj = DataPredictionPipeline()
            predict = obj.main(df_)[0]

            print(predict)

            return render_template('results.html', prediction = predict,source=source,destination=destination,date=date_of_journey)

        except Exception as e:
            print('The Exception message is: ',e)
            return 'something is wrong'

    else:
        return render_template('index.html')


if __name__ == "__main__" :
    app.run(host='0.0.0.0',port=8080)
