from . import views
from django.urls import path, include

urlpatterns = [
    path('', views.subscribe),
    path('subscribe/', views.subscribe)
]
