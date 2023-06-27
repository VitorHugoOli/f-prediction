import requests
import pandas as pd

# Define the base URL for the API
base_url = "http://ergast.com/api/f1/2023/results.json"

# Define the limit of results per request
limit = 30

# Initialize offset
offset = 0

# Create an empty list to store all race results
all_results = []

while True:
    # Make the API request with the current offset
    response = requests.get(f"{base_url}?limit={limit}&offset={offset}")

    # Convert the JSON response into a Python dictionary
    data = response.json()

    # Extract the race results
    races = data['MRData']['RaceTable']['Races']

    # If there are no races in the response, break the loop
    if not races:
        break

    # Loop through each race
    for race in races:
        # Loop through each result in the race
        for result in race['Results']:
            # Create a dictionary for the result
            result_dict = {
                'raceName': race['raceName'],
                'round': race['round'],
                'date': race['date'],
                'driverId': result['Driver']['driverId'],
                'number': result['Driver']['permanentNumber'],
                'time': result['Time']['time'] if 'Time' in result else None,
                'milliseconds': result['Time']['millis'] if 'Time' in result else None,
                'rank': result['FastestLap']['rank'] if 'FastestLap' in result else None,
                'fastestLap': result['FastestLap']['lap'] if 'FastestLap' in result else None,
                'fastestLapTime': result['FastestLap']['Time']['time'] if 'FastestLap' in result else None,
                'fastestLapSpeed': result['FastestLap']['AverageSpeed']['speed'] if 'FastestLap' in result else None,
                'position': result['position'],
                'points': result['points'],
                'laps': result['laps'],
                'status': result['status'],
                'grid': result['grid'],
                'constructorId': result['Constructor']['constructorId']
            }
            # Add the dictionary to the list of all results
            all_results.append(result_dict)

    # Increase the offset by the limit
    offset += limit

# Convert the list of dictionaries into a DataFrame
df = pd.DataFrame(all_results)

# Save the DataFrame as a CSV file
df.to_csv('f1_2023_results.csv', index=False)

