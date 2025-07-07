from dotenv import load_dotenv
from pprint import pprint
import requests
import os

load_dotenv()


def get_current_weather(city="Cairo"):
    OpenWeather_url = f"https://api.openweathermap.org/data/2.5/weather?&appid={os.getenv('OpenWeather_API_KEY')}&q={city}&units=metric"

    weather_data = requests.get(OpenWeather_url).json()

    return weather_data


if __name__ == "__main__":
    print("\n*** Get Current Weather Conditions ***\n")
    city = input("Pleas enter a city name: ").strip()
    # check for empty strings
    if not city:
        city = "Cairo"

    weather_data = get_current_weather(city)
    print("\n")
    pprint(weather_data)
