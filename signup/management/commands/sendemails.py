from django.core.management.base import BaseCommand, CommandError
from signup.models import Subscriber
from .privateKey import key
import requests
import json
import datetime


class Command(BaseCommand):
    help = 'Send emails to registered users'

    def handle(self, *args, **options):
        subscribers = Subscriber.objects.all()
        for subscriber in subscribers:
            print("Temperature difference in " + str(subscriber))
            print(getTemperatureDifference(subscriber.user_location))


def getTemperatureDifference(location):
    futureData = getJSONFutureWeather(location)
    currentData = getJSONCurrentWeather(location)

    futureTemp = futureData['data'][0]['temp']
    currentTemp = currentData['data'][0]['temp']
    return(float(futureTemp) - float(currentTemp))


def getJSONCurrentWeather(location):
    return requests.get(insertURLParams(_currentWeatherURL, location)).json()


def getJSONFutureWeather(location):
    return requests.get(insertURLParams(_futureWeatherURL, location)).json()


def insertURLParams(url, location):
    return url.replace('CITY', location).replace('KEY', key)


_futureWeatherURL = 'http://api.weatherbit.io/v2.0/forecast/daily?city=CITY&days=1&units=I&key=KEY'
_currentWeatherURL = 'http://api.weatherbit.io/v2.0/current?city=CITY&units=I&key=KEY'
