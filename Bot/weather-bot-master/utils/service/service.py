import json
import requests as requests
from settings import setting


def get_weather() -> json:
    city_id = 511196
    api_key = setting.api_key.get_secret_value()
    url = f"https://api.openweathermap.org/data/2.5/weather?id={city_id}&lang=ru&appid={api_key}&units=metric"
    response = requests.get(url)
    return response.json()
