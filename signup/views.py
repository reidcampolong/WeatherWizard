
import json, datetime
from django.views.decorators.http import require_http_methods
from django.shortcuts import render
from django.http import HttpResponse
from .models import Subscriber

def homepage(request):
  return HttpResponse("Signup here!")

@require_http_methods(["POST"])
def subscribe(request):
  request_data = json.loads(request.body)
  print(request_data)
  newUser = Subscriber(
    user_email = request_data.get("email"),
    user_location = request_data.get("location"),
    registered_on = datetime.datetime.now)
  newUser.save()
  return HttpResponse("Awesome, you're subscribed now!")