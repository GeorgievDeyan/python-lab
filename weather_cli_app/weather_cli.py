
---

## 🧠 Python код (`weather_cli.py`):

```python
import requests

def get_weather(city, api_key):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    try:
        response = requests.get(url)
        data = response.json()

        if response.status_code != 200:
            print(f"Error: {data.get('message', 'Failed to fetch weather data.')}")
            return

        weather = data["weather"][0]["description"].title()
        temp = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        wind_speed = data["wind"]["speed"]

        print(f"\nWeather in {city.title()}:")
        print(f"Temperature: {temp}°C")
        print(f"Condition: {weather}")
        print(f"Humidity: {humidity}%")
        print(f"Wind speed: {wind_speed} m/s")

    except Exception as e:
        print("An error occurred:", e)

if __name__ == "__main__":
    city = input("Enter city name: ")
    api_key = "your_api_key_here"  # Replace with your actual API key
    get_weather(city, api_key)
