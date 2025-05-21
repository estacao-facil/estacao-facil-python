import requests
from requests.exceptions import ConnectionError

from constants import OPEN_WEATHER_API_KEY
from utils import *
import text as t


# MENU: Checar Clima
def check_weather_menu(username, session_messages):
    """
    Menu que permite ao usuário consultar a previsão do tempo para um bairro da cidade de São Paulo.
    """
    while True:
        display_cecilia_message(t.check_weather_menu, session_messages)

        district = request_user_option(t.user_title.format(username), session_messages)
        if district == "":
            display_cecilia_message(t.invalid_value_message, session_messages)
            continue

        try:
            district_data = get_district_data(district)

            if not district_data:
                display_cecilia_message(
                    t.check_weather_district_not_found, session_messages
                )
                break

            lat, lon = district_data
            weather_data = get_weather_by_lat_lon(lat, lon)

            if not weather_data:
                display_cecilia_message(t.check_weather_weather_fail, session_messages)
                break

            show_weather_info(weather_data, session_messages)

        except ConnectionError:
            display_cecilia_message(t.check_weather_connection_error, session_messages)

        break


def get_district_data(district):
    """
    Consulta a API de geolocalização do OpenWeather para obter a latitude e longitude
    do bairro informado dentro da cidade de São Paulo.

    Retorna uma tupla (lat, lon) se encontrado, ou None se houver erro ou o bairro não for localizado.
    """
    loc_url = f"http://api.openweathermap.org/geo/1.0/direct?q={district}, São Paulo,&limit=1&appid={OPEN_WEATHER_API_KEY}"
    loc_response = requests.get(loc_url)

    if loc_response.status_code != 200:
        return None

    loc_data = loc_response.json()
    if not loc_data:
        return None

    return loc_data[0]["lat"], loc_data[0]["lon"]


def get_weather_by_lat_lon(lat, lon):
    """
    Consulta a API do OpenWeather para obter os dados climáticos da região com base na latitude e longitude fornecidas.

    Retorna um dicionário com:
    - Nome do bairro (district)
    - Temperatura atual (temp)
    - Sensação térmica (feels_like)
    - Condição do tempo (condition)
    - Umidade relativa do ar (humidity)

    Em caso de erro na requisição ou na estrutura dos dados, retorna None.
    """
    weather_url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={OPEN_WEATHER_API_KEY}&units=metric&lang=pt_br"
    weather_response = requests.get(weather_url)

    if weather_response.status_code != 200:
        return None

    try:
        data = weather_response.json()
        return {
            "district": data["name"],
            "temp": data["main"]["temp"],
            "feels_like": data["main"]["feels_like"],
            "condition": data["weather"][0]["description"].title(),
            "humidity": data["main"]["humidity"],
        }
    except (KeyError, IndexError, ValueError):
        return None


def show_weather_info(data, session_messages):
    """
    Exibe as informações do clima em uma mensagem formatada.
    """
    display_cecilia_message(
        t.weather_info.format(
            data["district"],
            data["temp"],
            data["feels_like"],
            data["condition"],
            data["humidity"],
        ),
        session_messages,
    )
