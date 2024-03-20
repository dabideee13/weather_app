import os
from typing import Any

import requests
from django.shortcuts import render
from django.http import JsonResponse, HttpRequest
from django.conf import settings

from weather_api.services import get_geolocation


# def get_weather(request, city_name: str) -> dict[str, Any]:
#     lat, lon = get_geolocation(city_name)
#     url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={settings.OPENWEATHERMAP_API_KEY}"
#     response = requests.get(url)
#     print(f'status: {response.status_code}')

#     if response.status_code == 200:
#         data = response.json()
#         weather = data['weather'][0]['description']
#         temperature = data['main']['temp']
#         return JsonResponse({
#             "city": city_name,
#             "weather": weather,
#             "temperature": f"{temperature} °C"
#         })
#     else:
#         return JsonResponse({"error": "Weather data not found"}, status=404)


def get_weather(request: HttpRequest):
    if request.method == "POST":
        city_name = request.POST.get('city_name', '')
        lat, lon = get_geolocation(city_name)
        url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={settings.OPENWEATHERMAP_API_KEY}"
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()
            weather = data['weather'][0]['description']
            temperature = data['main']['temp']
            context = {
                "city": city_name,
                "weather": weather,
                "temperature": f"{temperature} °C"
            }
            return render(request, 'weather_result.html', context)
        else:
            return render(request, 'weather_form.html', {"error": "Weather data not found"})
    else:
        return render(request, 'weather_form.html')