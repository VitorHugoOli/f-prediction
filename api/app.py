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
            <title>About</title>
        </head>
        <body>
            <h1>About</h1>
            <p>This is a project trying to predict the probability of driver winning the next f1 race.</p>
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
    app.run()
