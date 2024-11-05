import requests

def get_weather(api_key, city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)
    return response.json()

def display_weather(weather_data):
    if weather_data.get("cod") != 200:
        print("City not found!")
        return
    
    city = weather_data["name"]
    temperature = weather_data["main"]["temp"]
    weather_description = weather_data["weather"][0]["description"]
    
    print(f"Weather in {city}:")
    print(f"Temperature: {temperature}°C")
    print(f"Condition: {weather_description.capitalize()}")

def main():
    api_key = ""  # Replace with your actual API key
    city = input("Enter the city name: ")
    weather_data = get_weather(api_key, city)
    display_weather(weather_data)

if __name__ == "__main__":
    main()
