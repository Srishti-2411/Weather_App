import requests

def get_weather(city):
    api_key = '5b44d8aa03f4d6119c62d40921288971'  
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'
    response = requests.get(url)
    data = response.json()
    if response.status_code == 200:
        weather = {
            'city': data['name'],
            'temperature': data['main']['temp'],
            'description': data['weather'][0]['description']
        }
        return weather
    else:
        print("Failed to retrieve weather data.")
        return None

def main():
    city = input("Enter city name: ")
    weather = get_weather(city)
    if weather:
        print(f"Weather in {weather['city']}:")
        print(f"Temperature: {weather['temperature']}°C")
        print(f"Description: {weather['description']}")
    else:
        print("No weather data available.")

if __name__ == "__main__":
    main()
