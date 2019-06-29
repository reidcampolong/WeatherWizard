from django.core.management.base import BaseCommand, CommandError
from signup.models import Subscriber
from .privateKey import key
import requests, json, datetime

class Command(BaseCommand):
    help = 'Send emails to registered users'

    def handle(self, *args, **options):
        getWeatherForLocation('Boston')
        # subscribers = Subscriber.objects.all()
        # for subscriber in subscribers:
        #     print("Sending email to " + str(subscriber))


baseWeatherURL = 'http://api.weatherbit.io/v2.0/forecast/daily?city=CITY&days=1&key={key}'

def getWeatherForLocation(location):
    response = requests.get(baseWeatherURL.replace('CITY', location)).json()
    print(response)
    # response = json_obj
    # for item in response['list']:
    #   print(item)
    # print(len(response['list']))
    #print(reponse['time'])
