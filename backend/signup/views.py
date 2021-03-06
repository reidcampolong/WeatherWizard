
import json, datetime
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from django.http import HttpResponse
from .models import Subscriber

@csrf_exempt
@require_http_methods(["POST"])
def subscribe(request):
  request_data = json.loads(request.body)
  email = request_data.get('email')

  if Subscriber.objects.filter(user_email=email).count() > 0:
    return HttpResponse(status=406)
  else:
    subscriber = Subscriber(user_email=request_data.get('email'), user_location=request_data.get('location'),
      registered_on=datetime.datetime.now());
    subscriber.save();
    return HttpResponse("Thanks for registering with us!")