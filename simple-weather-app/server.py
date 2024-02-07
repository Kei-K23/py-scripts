from flask import Flask, render_template, request
from waitress import serve
from weather import get_weather_data

app = Flask(__name__)


@app.get("/")
def home():
    return render_template('index.html')


@app.get("/weather")
def weather():
    city = request.args.get('city').strip(
    ) if request.args.get('city') else 'yangon'
    data = get_weather_data(city)

    if data['cod'] == 200:
        return render_template('weather-result.html',
                               name=data['name'],
                               description=data['weather'][0]['description'],
                               temp=f"{data['main']['temp']:.1f}",
                               feel_like=f"{data['main']['feels_like']:.1f}")
    else:
        return render_template('not-weather-result.html', name=city)


if __name__ == '__main__':
    serve(app, host="0.0.0.0", port=4000)
