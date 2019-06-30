import yagmail
from .WeatherService import getWeatherData
from .privateKey import mailUsername, mailPassword

def sendEmailTo(subscriberList):
    yag = yagmail.SMTP(mailUsername, mailPassword)
    for subscriber in subscriberList:
        temp_diff, tomorrowIsSunny, precipitation, currentWeather = getWeatherData(subscriber.user_location)
        subject, body = getEmailContents(temp_diff, tomorrowIsSunny, precipitation, currentWeather)
        yag.send(subscriber.user_email, subject, body)
        print("Email sent to " + str(subscriber.user_email))

def getEmailContents(temp_diff, tomorrowIsSunny, precipitation, currentWeather) -> (str, str):
    """ Returns subject, body """
    if tomorrowIsSunny or temp_diff >= 5:
        return "It's nice out! Enjoy a discount on us.", currentWeather
    elif precipitation or temp_diff <= -5:
        return "Not so nice out? That's okay, enjoy a discount on us.", currentWeather
    else:
        return "Enjoy a discount on us.", currentWeather