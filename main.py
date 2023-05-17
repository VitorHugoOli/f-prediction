import requests
from bs4 import BeautifulSoup
import pandas as pd


# Accessing data from Ergast API
def get_api_data(url):
    response = requests.get(url)
    data = response.json()
    return data


# Scraping data from Formula 1 website
def get_web_data(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    return soup


def get_driver_data(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    driver_data = []

    # Assuming each driver is in a div with class 'driver'
    drivers = soup.find_all('div', class_='driver')
    for driver in drivers:
        driver_info = {}

        # Assuming name is in a span with class 'name'
        name = driver.find('span', class_='name')
        if name:
            driver_info['name'] = name.text

        # Assuming nationality is in a span with class 'nationality'
        nationality = driver.find('span', class_='nationality')
        if nationality:
            driver_info['nationality'] = nationality.text

        # Assuming team is in a span with class 'team'
        team = driver.find('span', class_='team')
        if team:
            driver_info['team'] = team.text

        # Add to list of driver data
        driver_data.append(driver_info)

    return driver_data


def get_racing_reference_data(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Get the table
    table = soup.find('table', {'class': 'tb standingsTbl'})

    # Get the headers
    headers = []
    for th in table.find_all('th'):
        headers.append(th.text.strip())

    # Get the data
    data = []
    for row in table.find_all('tr')[1:]:  # Skip the first row (header)
        cols = row.find_all('td')
        cols = [ele.text.strip() for ele in cols]
        data.append([ele for ele in cols if ele])  # Remove empty values

    headers.pop(0)
    headers.pop(-1)
    headers.pop(-1)
    print(data)


    # Convert to DataFrame
    df = pd.DataFrame(data, columns=headers)
    return df


url = 'https://www.racing-reference.info/standings/2022/F/'
data = get_racing_reference_data(url)
print(data)

web_url = 'https://www.formula1.com/'
# web_data = get_web_data(web_url)
# print(web_data.prettify())

api_url = 'http://ergast.com/api/f1/2023/driverStandings.json'
api_data = get_api_data(api_url)
print(api_data)

url = 'https://www.formula1.com/en/drivers.html'
driver_data = get_driver_data(url)

for driver in driver_data:
    print(driver)
