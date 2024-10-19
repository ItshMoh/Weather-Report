import requests
import uuid
from client import WeatherAlertsServiceClient
from config import WEATHER_API_KEY

client = WeatherAlertsServiceClient()
def get_weather_data(location):
    WEATHER_API_URL = f'http://api.weatherapi.com/v1/current.json?key={WEATHER_API_KEY}&q=${location}&aqi=yes'
    response = requests.get(WEATHER_API_URL )
    weather_data = response.json()
 
    if response.status_code != 200:
        print(f"Error fetching weather data: {weather_data.get('message')}")
        return None

    return weather_data

def send_weather_alert(location):
    weather_data = get_weather_data(location)
    if weather_data is None:
        return
    
    weather_main = weather_data['current']['condition']['text'].lower()
    temperature = weather_data['current']['temp_c']
    precipitation = weather_data['current'].get('precip_mm', 0)  
    location_name = weather_data['location']['name']
    alert_id = str(uuid.uuid4())  

    if 'rain' in weather_main or precipitation > 0:
        intensity = precipitation  
        client.sendRainAlert(alert_id, location_name, intensity)
        print(f"Rain alert sent for {location_name} with intensity {intensity} mm.")
    elif 'snow' in weather_main:
        intensity = precipitation  
        client.sendSnowAlert(alert_id, location_name, intensity)
        print(f"Snow alert sent for {location_name} with intensity {intensity} mm.")
    elif temperature >= 30:
        client.sendHeatwaveAlert(alert_id, location_name, temperature)
        print(f"Heatwave alert sent for {location_name} with temperature {temperature}°C.")
    else:
        client.sendNormalAlert(alert_id, location_name, temperature)
        print(f"Weather in {location_name} is normal: {weather_main}, {temperature}°C.")

def main():
    location = input("Enter a location (city, address, etc.): ")
    send_weather_alert(location)

if __name__ == "__main__":
    main()
