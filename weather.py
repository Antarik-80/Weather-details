import requests

def get_weather(city_name, api_key):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}&units=metric"
    response = requests.get(url)
    data = response.json()
    return data

def main():
    api_key = "YOUR_API_KEY"  # Replace "YOUR_API_KEY" with your actual API key from OpenWeatherMap
    city_name = input("Enter city name: ")
    weather_data = get_weather(city_name, api_key)

    if weather_data["cod"] == 200:  # Check if the API call was successful
        print(f"Weather in {city_name}:")
        print(f"Temperature: {weather_data['main']['temp']}°C")
        print(f"Description: {weather_data['weather'][0]['description']}")
        print(f"Humidity: {weather_data['main']['humidity']}%")
        print(f"Wind Speed: {weather_data['wind']['speed']} m/s")
    else:
        print("Error fetching weather data.")

if __name__ == "__main__":
    main()
