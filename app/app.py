from flask import Flask, request
import requests

app = Flask(__name__)

API_KEY = "968fa3b37c517b704665f9fb0b3d2fcf"  # replace with your real OpenWeatherMap API key

@app.route("/")
def home():
    return "Welcome to Weather Tracker! Use /weather?city=CityName"

@app.route("/weather")
def weather():
    city = request.args.get("city")
    if not city:
        return "Please provide a city like /weather?city=London"

    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    res = requests.get(url)

    if res.status_code != 200:
        return f"Error: {res.json().get('message', 'Could not fetch data')}"

    data = res.json()
    temp = data['main']['temp']
    desc = data['weather'][0]['description']

    return f"City: {city}, Temp: {temp}°C, Weather: {desc}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5050)
