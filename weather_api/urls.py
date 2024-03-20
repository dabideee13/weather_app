from django.urls import path
from . import views

urlpatterns = [
    # path('weather/<str:city_name>/', views.get_weather, name='get_weather'),
    path('', views.get_weather, name='get_weather'),
]