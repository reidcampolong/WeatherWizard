
from django.views.decorators.http import require_http_methods
from django.shortcuts import render
from django.http import HttpResponse

def homepage(request):
  return HttpResponse("Signup here!")

@require_http_methods(["POST"])
def subscribe(request):
  return HttpResponse("Awesome, you're subscribed now")