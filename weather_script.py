import requests

def get_weather(api_key, city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)
    if response.status_code != 200:
        print("Failed to retrieve data. Please check the city name or API key.")
        return

    data = response.json()
    temp = data['main']['temp']
    humidity = data['main']['humidity']
    condition = data['weather'][0]['description']

    print(f"Weather in {city}:")
    print(f"Temperature: {temp}°C")
    print(f"Humidity: {humidity}%")
    print(f"Condition: {condition.capitalize()}")

def main():
    api_key = input("Enter your OpenWeatherMap API key: ")
    city = input("Enter city name: ")
    get_weather(api_key, city)

if __name__ == "__main__":
    main()