from flask import Flask
from flask import jsonify, request
import json
import pandas as pd

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


@app.route('/about')
def about():
    # return a html explaining about hte project
    return """
    <!DOCTYPE html>
    <html>
        <head>
            <title>About The Project</title>
            <style>
                body {
                    font-family: Arial, sans-serif;
                    background-color: #f4f4f4;
                    margin: 0;
                    padding: 0;
                }
                .container {
                    width: 80%;
                    margin: auto;
                    overflow: hidden;
                }
                header {
                    background: #50b3a2;
                    color: white;
                    padding-top: 30px;
                    min-height: 70px;
                    border-bottom: #e8491d 3px solid;
                }
                header h1 {
                    padding: 5px 0;
                    color: #fff;
                    text-transform: uppercase;
                    text-align: center;
                    margin: 0;
                    font-size: 36px;
                }
                main {
                    margin: 20px;
                    padding: 20px;
                    background-color: #fff;
                    box-shadow: 0px 0px 10px #bbb;
                    font-size: 18px;
                    line-height: 1.6em;
                }
            </style>
        </head>
        <body>
            <header>
                <div class="container">
                    <h1>About Our Project</h1>
                </div>
            </header>
            <main>
                <div class="container">
                    <p>The project is dedicated to utilizing data science for predicting the potential outcomes of future Formula 1 races. By analyzing various factors and previous performance data, we are working towards a system capable of estimating a driver's chances of success in the upcoming races. This, we believe, can revolutionize the sport by adding an additional layer of excitement and anticipation.</p>
                </div>
            </main>
        </body>
    </html>
    """







# constructorId, position, laps, nationality, round, circuitId, country_circuit, height, nationality_constructors, points_season, position_season, wins_season, age, weather_condition, humidity, temperature, AvgGrid, AvgFn, wins_cum
@app.route('/actual_prediction')
def actual_prediction():
    races_df = pd.read_csv('static/races.csv')
    races_df.date = pd.to_datetime(races_df['date'])
    next_race = races_df.loc[races_df['date'] > pd.Timestamp.now()].iloc[0]
    race_id = next_race['raceId']

    with open('static/prediction.json', 'r') as f:
        predictions = json.load(f)

    if str(race_id) in predictions:
        return jsonify(predictions[str(race_id)]), 200
    else:
        with open('drivers.json', 'r') as f:
            drivers = json.load(f)
        for driver in drivers:
            # pass driver to model and get prediction.json
            prediction = 0.5  # replace with actual prediction.json
            predictions[race_id][driver['driverId']] = prediction
        with open('prediction.json.json', 'w') as f:
            json.dump(predictions, f)
        return jsonify({'message': 'Predictions saved successfully.'}), 200


if __name__ == '__main__':
    app.run(host='0.0.0.0')
