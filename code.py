import requests
from bs4 import BeautifulSoup

def get_weather(city):
    url = f"https://www.weather.com/weather/today/l/{city}"
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers)
    
    if response.status_code != 200:
        print("Failed to retrieve weather data.")
        return
    
    soup = BeautifulSoup(response.text, "html.parser")
    temp = soup.find("span", class_="CurrentConditions--tempValue--3KcTQ")
    condition = soup.find("div", class_="CurrentConditions--phraseValue--2xXSr")
    
    if temp and condition:
        print(f"Current Temperature: {temp.text}")
        print(f"Condition: {condition.text}")
    else:
        print("Could not fetch weather details.")

if __name__ == "__main__":
    city_code = input("Enter city code (e.g., USCA0987 for San Francisco): ")
    get_weather(city_code)
