import requests
import json
import click

from dotenv import load_dotenv
import os

load_dotenv()  # Load environment variables from .env file

API_KEY = os.getenv('API_KEY')
BASE_URL = 'http://api.openweathermap.org/data/2.5/weather'


def get_weather_forecast(city_name):
    try:
        url = f"{BASE_URL}?q={city_name}&appid={API_KEY}"
        response = requests.get(url)
        response.raise_for_status()
        data = json.loads(response.text)

        city = data['name']
        temperature = data['main']['temp']
        weather_description = data['weather'][0]['description']

        print(f"Weather forecast for {city}:")
        print(f"Temperature: {temperature}°C")
        print(f"Description: {weather_description}")
    
    except requests.exceptions.HTTPError as error:
        print(f"HTTP error occurred: {error}")
    
    except KeyError:
        print("Unable to retrieve weather forecast. Please check the city name.")

@click.command()
@click.option("--city_name", prompt="Enter the city name: ", help="The city name for weather")
def main(city_name):
    
    get_weather_forecast(city_name)

if __name__ == '__main__':
    main()
