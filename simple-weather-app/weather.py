import requests
import os
from dotenv import load_dotenv

load_dotenv()


def get_weather_data(city):
    url = f"https://api.openweathermap.org/data/2.5/weather?appid={
        os.getenv('API_KEY')}&q={city}&units=imperial"
    return requests.get(url).json()


if __name__ == '__main___':
    print('run')
