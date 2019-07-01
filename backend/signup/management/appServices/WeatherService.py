from .privateKey import key
import requests, json

_futureWeatherURL = 'http://api.weatherbit.io/v2.0/forecast/daily?city=CITY&days=1&units=I&key=KEY'
_currentWeatherURL = 'http://api.weatherbit.io/v2.0/current?city=CITY&units=I&key=KEY'

def getWeatherData(location):
    futureData = _getJSONFutureWeather(location)
    currentData = _getJSONCurrentWeather(location)

    futureTemp = futureData['data'][0]['temp']
    currentTemp = currentData['data'][0]['temp']

    # Difference of temperature today vs tomorrow
    temp_diff = float(currentTemp) - float(futureTemp)

    # 800 is the code for sunny!
    tomorrowIsSunny = (futureData['data'][0]['weather']['code'] == 800)

    # Check for precipitation tomorrow
    precipitation = (futureData['data'][0]['precip'] > 0)
    
    # Description string of the current weather
    currentWeather = str(currentTemp) + " degrees, " + str(currentData['data'][0]['weather']['description'])

    return(temp_diff, tomorrowIsSunny, precipitation, currentWeather)

def _getJSONCurrentWeather(location):
    return requests.get(_insertURLParams(_currentWeatherURL, location)).json()

def _getJSONFutureWeather(location):
    return requests.get(_insertURLParams(_futureWeatherURL, location)).json()

def _insertURLParams(url, location):
    return url.replace('CITY', location).replace('KEY', key)

