import requests

def get_weather(lat, lon):
    """Getting data from Open-Meteo API"""
    url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current_weather=true"
    response = requests.get(url)
    return response

def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32