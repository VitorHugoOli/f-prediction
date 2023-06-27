import requests
import pandas as pd

# Define the base URL for the API
base_url = "http://ergast.com/api/f1/2023"

# Initialize an empty list to store all driver standings
all_standings = []

# Get the total number of rounds in the 2023 season
response = requests.get(f"{base_url}.json")
data = response.json()
total_rounds = len(data['MRData']['RaceTable']['Races'])

# Loop over each round
for round in range(1, total_rounds + 1):
    print(f"{base_url}/{round}/driverStandings.json")

    # Make the API request
    response = requests.get(f"{base_url}/{round}/driverStandings.json")

    # Convert the JSON response into a Python dictionary
    data = response.json()

    if len(data['MRData']['StandingsTable']['StandingsLists']) == 0:
        break

    # Extract the driver standings
    standings = data['MRData']['StandingsTable']['StandingsLists'][0]['DriverStandings']

    # Loop through each standing
    for standing in standings:
        # Create a dictionary for the standing
        standing_dict = {
            'round': round,
            'position': standing['position'],
            'points': standing['points'],
            'wins': standing['wins'],
            'driverId': standing['Driver']['driverId'],
            'constructorId': standing['Constructors'][0]['constructorId']
        }
        # Add the dictionary to the list of all standings
        all_standings.append(standing_dict)

# Convert the list of dictionaries into a DataFrame
df = pd.DataFrame(all_standings)

# Save the DataFrame as a CSV file
df.to_csv('f1_2023_standings_by_round.csv', index=False)
