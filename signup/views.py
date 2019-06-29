
import json, datetime
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from django.http import HttpResponse
from .models import Subscriber

def homepage(request):
  return HttpResponse("Signup here!")

@csrf_exempt
@require_http_methods(["POST"])
def subscribe(request):
  print("Received new request")
  request_data = json.loads(request.body)
  print(request_data)
  return request_data